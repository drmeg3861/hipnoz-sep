#!/usr/bin/env python3
"""NotebookLM için kaynak birleştirici.

PDF, Word (.docx), PowerPoint (.pptx), metin (.txt/.md) ve görselleri
(.jpg/.jpeg/.png) tek bir ya da birkaç PDF'te birleştirir. Her çıktı,
NotebookLM'in kaynak başına sınırının (yaklaşık 500.000 kelime, 200 MB)
altında kalacak şekilde doldurulur; sınır aşılacaksa yeni cilt açılır.

Her kaynağın önüne bir ayraç sayfası konur ve PDF'e yer imi eklenir;
her cildin başında içindekiler sayfası olur. Metin katmanı olmayan
(taranmış) PDF sayfaları ve görseller OCR ile aranabilir hâle getirilir:
önce Tesseract (Türkçe karakterlerde iyi), o yoksa RapidOCR denenir.

Kurulum:
    python3 -m pip install pymupdf reportlab
    # OCR (önerilir):
    #   Mac:    brew install tesseract tesseract-lang
    #   Linux:  sudo apt install tesseract-ocr tesseract-ocr-tur
    #   Yedek:  python3 -m pip install rapidocr-onnxruntime

Kullanım:
    # Bir klasördeki tüm dosyaları tek pakette birleştir
    python3 notebooklm_birlestir.py --girdi ~/Desktop/Modul7 --ad "Modül 7" --cikti ~/Desktop/NotebookLM

    # Paket tanımı (JSON) ile birden çok paket üret
    python3 notebooklm_birlestir.py --tanim paketler.json --cikti ~/Desktop/NotebookLM

paketler.json biçimi:
    [{"ad": "Soru Bankaları",
      "ogeler": [{"yol": "soru_bankasi.pdf", "baslik": "Hipnoz soru bankası"},
                 {"yol": "medipol_2026.txt"}]}]
"""
import argparse
import hashlib
import html
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import zipfile
from concurrent.futures import ThreadPoolExecutor

try:
    import pymupdf as fitz
except ImportError:  # eski PyMuPDF sürümleri
    import fitz

from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import cm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import PageBreak, Paragraph, SimpleDocTemplate, Spacer

MAX_KELIME = 450_000          # NotebookLM sınırı ~500.000; güvenlik payı
MAX_BAYT = 180 * 1024 * 1024  # NotebookLM sınırı 200 MB; güvenlik payı
TARANMIS_ESIK = 20            # sayfa başına bundan az kelime = taranmış sayfa

GORSEL = {".jpg", ".jpeg", ".png"}
METIN = {".txt", ".md"}

FONT_ADAYLARI = [
    "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    "/Library/Fonts/Arial Unicode.ttf",
    "/System/Library/Fonts/Supplemental/Arial Unicode.ttf",
    "/System/Library/Fonts/Supplemental/Arial.ttf",
    "C:/Windows/Fonts/arial.ttf",
    "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf",
]

_ocr = None
OCR_DIL = "tur+eng"


def kelime_say(metin):
    return len(re.findall(r"\w+", metin))


def font_kaydet(yol=None):
    for aday in ([yol] if yol else []) + FONT_ADAYLARI:
        if aday and os.path.exists(aday):
            pdfmetrics.registerFont(TTFont("Govde", aday))
            return aday
    sys.exit("Türkçe karakter destekli bir TTF font bulunamadı; --font ile yol verin.")


def ocr_motoru():
    """'tesseract', bir RapidOCR nesnesi ya da False döndürür."""
    global _ocr
    if _ocr is None:
        if shutil.which("tesseract"):
            _ocr = "tesseract"
        else:
            try:
                from rapidocr_onnxruntime import RapidOCR
                _ocr = RapidOCR()
            except ImportError:
                _ocr = False
    return _ocr


OCR_ZAMAN_ASIMI = 180  # saniye; takılan sayfa olduğu gibi bırakılır
_TEK_CEKIRDEK = dict(os.environ, OMP_THREAD_LIMIT="1")


def ocr_gorsel(gorsel_bayt):
    motor = ocr_motoru()
    if not motor:
        return ""
    if motor == "tesseract":
        try:
            r = subprocess.run(["tesseract", "stdin", "stdout", "-l", OCR_DIL, "--psm", "3"],
                               input=gorsel_bayt, capture_output=True, timeout=OCR_ZAMAN_ASIMI)
        except subprocess.TimeoutExpired:
            return ""
        return r.stdout.decode("utf-8", "replace")
    sonuc, _ = motor(gorsel_bayt)
    return "\n".join(satir[1] for satir in (sonuc or []))


def tesseract_pdf_sayfasi(png_yolu):
    """PNG'den yalnızca görünmez metin katmanı içeren tek sayfalık PDF üretir."""
    taban = png_yolu[:-4]
    try:
        subprocess.run(["tesseract", png_yolu, taban, "-l", OCR_DIL, "--psm", "3",
                        "-c", "textonly_pdf=1", "pdf"], capture_output=True,
                       timeout=OCR_ZAMAN_ASIMI, env=_TEK_CEKIRDEK)
    except subprocess.TimeoutExpired:
        return None
    return taban + ".pdf" if os.path.exists(taban + ".pdf") else None


# --- Metin çıkarma -------------------------------------------------------

def temizle(metin):
    metin = metin.replace("\r\n", "\n").replace("\r", "\n")
    metin = re.sub(r"\\([\\*#\-!\[\]_.()>`|])", r"\1", metin)       # markdown kaçışları
    metin = re.sub(r"^\s*#\s*index\.html\s*$", "", metin, flags=re.M)
    metin = re.sub(r"^\s*Image labels:.*$", "", metin, flags=re.M)  # Drive OCR etiketleri
    metin = re.sub(r"\*\*(.+?)\*\*", r"\1", metin)
    metin = re.sub(r"\n{3,}", "\n\n", metin)
    return metin.strip()


def docx_metni(yol):
    with zipfile.ZipFile(yol) as z:
        xml = z.read("word/document.xml").decode("utf-8")
    paragraflar = []
    for p in re.findall(r"<w:p[ >].*?</w:p>", xml, flags=re.S):
        p = re.sub(r"<w:tab/>", "\t", p)
        p = re.sub(r"<w:br/>", "\n", p)
        t = "".join(re.findall(r"<w:t[^>]*>(.*?)</w:t>", p, flags=re.S))
        paragraflar.append(html.unescape(t))
    return "\n".join(paragraflar)


def pptx_metni(yol):
    with zipfile.ZipFile(yol) as z:
        slaytlar = sorted(
            (n for n in z.namelist() if re.match(r"ppt/slides/slide\d+\.xml$", n)),
            key=lambda n: int(re.findall(r"\d+", n)[-1]))
        parcalar = []
        for i, ad in enumerate(slaytlar, 1):
            xml = z.read(ad).decode("utf-8")
            satirlar = []
            for p in re.findall(r"<a:p>.*?</a:p>", xml, flags=re.S):
                t = "".join(re.findall(r"<a:t>(.*?)</a:t>", p, flags=re.S))
                if t.strip():
                    satirlar.append(html.unescape(t))
            parcalar.append(f"— Slayt {i} —\n" + "\n".join(satirlar))
    return "\n\n".join(parcalar)


def metin_dosyasi(yol):
    ham = open(yol, "rb").read()
    for kod in ("utf-8-sig", "cp1254", "latin-1"):
        try:
            return ham.decode(kod)
        except UnicodeDecodeError:
            continue
    return ham.decode("utf-8", "replace")


# --- PDF üretimi ----------------------------------------------------------

def stiller():
    return {
        "govde": ParagraphStyle("govde", fontName="Govde", fontSize=10.5, leading=14.5, spaceAfter=5),
        "baslik": ParagraphStyle("baslik", fontName="Govde", fontSize=20, leading=26,
                                 alignment=TA_CENTER, spaceAfter=14),
        "alt": ParagraphStyle("alt", fontName="Govde", fontSize=11, leading=15, alignment=TA_CENTER),
        "madde": ParagraphStyle("madde", fontName="Govde", fontSize=10.5, leading=14.5, leftIndent=12),
    }


def paragraf(metin, stil):
    return Paragraph(html.escape(metin).replace("\n", "<br/>"), stil)


def metinden_pdf(metin, hedef):
    st = stiller()
    hikaye = [paragraf(b, st["govde"]) for b in re.split(r"\n\s*\n", metin) if b.strip()]
    if not hikaye:
        hikaye = [paragraf("(Bu kaynakta metin bulunamadı.)", st["govde"])]
    SimpleDocTemplate(hedef, pagesize=A4, leftMargin=2 * cm, rightMargin=2 * cm,
                      topMargin=2 * cm, bottomMargin=2 * cm).build(hikaye)


def ayrac_pdf(hedef, baslik, satirlar):
    st = stiller()
    hikaye = [Spacer(1, 7 * cm), paragraf(baslik, st["baslik"])]
    hikaye += [paragraf(s, st["alt"]) for s in satirlar]
    SimpleDocTemplate(hedef, pagesize=A4).build(hikaye)


def icindekiler_pdf(hedef, paket_adi, cilt, ogeler):
    st = stiller()
    hikaye = [paragraf(f"{paket_adi} — Cilt {cilt}", st["baslik"]),
              paragraf("İçindekiler", st["alt"]), Spacer(1, 0.6 * cm)]
    for i, o in enumerate(ogeler, 1):
        hikaye.append(paragraf(f"{i}. {o['baslik']}  ({o['kelime']:,} kelime)".replace(",", "."), st["madde"]))
    hikaye.append(PageBreak())
    SimpleDocTemplate(hedef, pagesize=A4).build(hikaye)


def kaydet(doc, hedef):
    # garbage=4: tekrarlanan nesne ve akışları (fontlar, görseller) birleştirir
    doc.save(hedef, garbage=4, deflate=True, deflate_images=True, deflate_fonts=True)


# --- Öğe hazırlama --------------------------------------------------------

def oge_hazirla(yol, baslik, gecici):
    """Öğeyi PDF'e çevirir; (pdf_yolu, kelime, not) döndürür."""
    uzanti = os.path.splitext(yol)[1].lower()
    hedef = os.path.join(gecici, hashlib.md5(yol.encode()).hexdigest() + ".pdf")
    not_ = ""
    if uzanti == ".pdf":
        kaynak = fitz.open(yol)
        kelimeler = [kelime_say(sayfa.get_text()) for sayfa in kaynak]
        # Taranmış sayfa: az kelime + görsel (görselsiz kısa sayfa taranmış sayılmaz)
        taranan = [i for i, sayfa in enumerate(kaynak)
                   if kelimeler[i] < TARANMIS_ESIK and sayfa.get_images()]
        ocr_pdf = {}  # sayfa no -> görünmez metin katmanı PDF'i (Tesseract)
        ocr_metin = {}  # sayfa no -> OCR metni (RapidOCR yedeği)
        if taranan and ocr_motoru() == "tesseract":
            pngler = {}
            for i in taranan:  # PyMuPDF iş parçacığı güvenli değil: görüntüleri önce üret
                pngler[i] = os.path.join(gecici, f"ocr_{i}.png")
                kaynak[i].get_pixmap(dpi=250, colorspace=fitz.csGRAY).save(pngler[i])
            with ThreadPoolExecutor(max_workers=os.cpu_count() or 2) as havuz:
                for i, sonuc in zip(taranan, havuz.map(tesseract_pdf_sayfasi, [pngler[i] for i in taranan])):
                    if sonuc:
                        ocr_pdf[i] = sonuc
                    os.remove(pngler[i])
        elif taranan and ocr_motoru():
            for i in taranan:
                ocr_metin[i] = ocr_gorsel(kaynak[i].get_pixmap(dpi=200).tobytes("png"))
        cikti = fitz.open()
        kelime = ocr_sayfa = 0
        i = 0
        while i < len(kaynak):
            if i not in ocr_pdf and not kelime_say(ocr_metin.get(i, "")):
                j = i  # değişmeyen ardışık sayfaları tek seferde ekle (ortak kaynaklar bir kez kopyalanır)
                while j + 1 < len(kaynak) and j + 1 not in ocr_pdf and not kelime_say(ocr_metin.get(j + 1, "")):
                    j += 1
                cikti.insert_pdf(kaynak, from_page=i, to_page=j)
                kelime += sum(kelimeler[i:j + 1])
                i = j + 1
                continue
            sayfa = kaynak[i]
            yeni = cikti.new_page(width=sayfa.rect.width, height=sayfa.rect.height)
            # Sayfada düşük çözünürlüklü görüntü saklanır, OCR metni görünmez katman olur
            yeni.insert_image(yeni.rect, stream=sayfa.get_pixmap(dpi=90, colorspace=fitz.csGRAY).tobytes("jpeg", jpg_quality=40))
            if i in ocr_pdf:
                katman = fitz.open(ocr_pdf[i])
                kelime += kelime_say(katman[0].get_text())
                yeni.show_pdf_page(yeni.rect, katman, 0)
                katman.close()
                os.remove(ocr_pdf[i])
            else:
                metin = ocr_metin[i]
                # Metin kutuya sığana kadar puntoyu küçült (sığmazsa PyMuPDF hiç yazmaz)
                for punto in (7, 6, 5, 4, 3, 2.5, 2, 1.5, 1):
                    if yeni.insert_textbox(yeni.rect + (15, 15, -15, -15), metin, fontsize=punto,
                                           fontname="Govde", fontfile=FONT_YOLU, render_mode=3) >= 0:
                        break
                kelime += kelime_say(metin)
            ocr_sayfa += 1
            i += 1
        if taranan:
            not_ = f"{len(taranan)} taranmış sayfa; {ocr_sayfa} sayfa OCR ile metne çevrildi"
            if not ocr_motoru():
                not_ += " (OCR kurulu değil — bu sayfalar NotebookLM'de okunamayabilir)"
        kaydet(cikti, hedef)
        return hedef, kelime, not_
    if uzanti in GORSEL:
        ocr = ocr_gorsel(open(yol, "rb").read())
        doc = fitz.open()
        sayfa = doc.new_page(width=A4[0], height=A4[1])
        sayfa.insert_image(sayfa.rect + (30, 30, -30, -30), filename=yol, keep_proportion=True)
        if ocr.strip():
            metin_yol = hedef + ".metin.pdf"
            metinden_pdf("Görseldeki metin (OCR):\n\n" + ocr, metin_yol)
            doc.insert_pdf(fitz.open(metin_yol))
        else:
            not_ = "görselden metin çıkmadı"
        kaydet(doc, hedef)
        return hedef, kelime_say(ocr), not_
    if uzanti == ".docx":
        metin = docx_metni(yol)
    elif uzanti == ".pptx":
        metin = pptx_metni(yol)
    elif uzanti in METIN:
        metin = metin_dosyasi(yol)
    else:
        raise ValueError(f"desteklenmeyen dosya türü: {uzanti}")
    metin = temizle(metin)
    metinden_pdf(metin, hedef)
    return hedef, kelime_say(metin), not_


# --- Paketleme ------------------------------------------------------------

def guvenli_ad(ad):
    return re.sub(r'[\\/:*?"<>|]+', "-", ad).strip()


def paket_uret(paket, cikti_klasoru, rapor):
    gecici = tempfile.mkdtemp(prefix="nblm_")
    hazir, goruldu = [], {}
    for oge in paket["ogeler"]:
        yol = os.path.expanduser(oge["yol"])
        baslik = oge.get("baslik") or os.path.splitext(os.path.basename(yol))[0]
        ozet = hashlib.md5(open(yol, "rb").read()).hexdigest()
        if ozet in goruldu:
            rapor.append([paket["ad"], "-", baslik, 0, f"ATLANDI: '{goruldu[ozet]}' ile birebir aynı"])
            continue
        goruldu[ozet] = baslik
        pdf, kelime, not_ = oge_hazirla(yol, baslik, gecici)
        hazir.append({"baslik": baslik, "pdf": pdf, "kelime": kelime, "not": not_,
                      "kaynak": os.path.basename(yol), "bayt": os.path.getsize(pdf)})
        print(f"  + {baslik}: {kelime:,} kelime {('— ' + not_) if not_ else ''}")

    # Ciltlere dağıt (sıra korunur; sınırı aşacak öğe yeni cilde geçer)
    ciltler, mevcut, k_top, b_top = [], [], 0, 0
    for o in hazir:
        if mevcut and (k_top + o["kelime"] > MAX_KELIME or b_top + o["bayt"] > MAX_BAYT):
            ciltler.append(mevcut)
            mevcut, k_top, b_top = [], 0, 0
        mevcut.append(o)
        k_top += o["kelime"]
        b_top += o["bayt"]
    if mevcut:
        ciltler.append(mevcut)

    for n, cilt in enumerate(ciltler, 1):
        ad = guvenli_ad(paket["ad"]) + (f" - Cilt {n}" if len(ciltler) > 1 else "")
        hedef = os.path.join(cikti_klasoru, ad + ".pdf")
        doc = fitz.open()
        ic = os.path.join(gecici, f"ic_{n}.pdf")
        icindekiler_pdf(ic, paket["ad"], n, cilt)
        doc.insert_pdf(fitz.open(ic))
        toc = []
        for i, o in enumerate(cilt, 1):
            ay = os.path.join(gecici, f"ayrac_{n}_{i}.pdf")
            satirlar = [f"Kaynak dosya: {o['kaynak']}", f"Kelime: {o['kelime']:,}".replace(",", ".")]
            if o["not"]:
                satirlar.append("Not: " + o["not"])
            ayrac_pdf(ay, f"{i}. {o['baslik']}", satirlar)
            toc.append([1, f"{i}. {o['baslik']}", len(doc) + 1])
            doc.insert_pdf(fitz.open(ay))
            doc.insert_pdf(fitz.open(o["pdf"]))
            rapor.append([paket["ad"], ad, o["baslik"], o["kelime"], o["not"]])
        doc.set_toc(toc)
        doc.set_metadata({"title": ad, "subject": "NotebookLM kaynağı"})
        kaydet(doc, hedef)
        toplam = sum(o["kelime"] for o in cilt)
        print(f"=> {hedef}  ({len(cilt)} kaynak, {toplam:,} kelime, {os.path.getsize(hedef)/1048576:.1f} MB)")


def main():
    global FONT_YOLU, MAX_KELIME, OCR_DIL
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--tanim", help="paket tanımı JSON dosyası")
    ap.add_argument("--girdi", help="tek paket için girdi klasörü")
    ap.add_argument("--ad", help="--girdi ile paket adı")
    ap.add_argument("--cikti", required=True, help="çıktı klasörü")
    ap.add_argument("--font", help="Türkçe destekli TTF font yolu")
    ap.add_argument("--max-kelime", type=int, default=MAX_KELIME)
    ap.add_argument("--dil", default=OCR_DIL, help="Tesseract dil kodları (varsayılan tur+eng)")
    a = ap.parse_args()
    MAX_KELIME = a.max_kelime
    OCR_DIL = a.dil
    FONT_YOLU = font_kaydet(a.font)
    os.makedirs(a.cikti, exist_ok=True)
    if a.tanim:
        tanim_klasoru = os.path.dirname(os.path.abspath(a.tanim))
        paketler = json.load(open(a.tanim, encoding="utf-8"))
        for p in paketler:
            for o in p["ogeler"]:
                if not os.path.isabs(os.path.expanduser(o["yol"])):
                    o["yol"] = os.path.join(tanim_klasoru, o["yol"])
    elif a.girdi:
        desteklenen = {".pdf", ".docx", ".pptx"} | METIN | GORSEL
        dosyalar = sorted(f for f in os.listdir(a.girdi)
                          if os.path.splitext(f)[1].lower() in desteklenen)
        paketler = [{"ad": a.ad or os.path.basename(os.path.normpath(a.girdi)),
                     "ogeler": [{"yol": os.path.join(a.girdi, f)} for f in dosyalar]}]
    else:
        ap.error("--tanim ya da --girdi verin")
    if not ocr_motoru():
        print("Uyarı: OCR kurulu değil (Tesseract/RapidOCR); taranmış sayfalar ve görseller metne çevrilmeyecek.")
    rapor = []
    for p in paketler:
        print(f"[{p['ad']}]")
        paket_uret(p, a.cikti, rapor)
    with open(os.path.join(a.cikti, "birlestirme_raporu.tsv"), "w", encoding="utf-8") as f:
        f.write("paket\tcikti_pdf\tkaynak\tkelime\tnot\n")
        for r in rapor:
            f.write("\t".join(str(x) for x in r) + "\n")


FONT_YOLU = None

if __name__ == "__main__":
    main()
