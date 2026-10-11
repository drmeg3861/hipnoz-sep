#!/usr/bin/env python3
"""Birleşik paket PDF'inden yalnızca metin içeren (görselsiz) NotebookLM sürümü üretir.

Her kaynak için ayraç sayfası ve yer imi korunur; asıl kitap sayfaları
"— s. N —" işaretiyle metin içinde belirtilir. OCR katmanları da metne dahildir.
Kullanım: python3 metin_surumu.py girdi.pdf cikti.pdf
          python3 metin_surumu.py --kitap-basina girdi.pdf cikti_klasoru/   (her kaynak ayrı PDF)
          python3 metin_surumu.py --parca 2 girdi.pdf cikti_klasoru/ [ilk_harf]
              [--ad "Paket Adı"]  (kaynakları kelime sayısı dengeli N dosyaya böler: K1a, K1b ...;
              kitap bölünmez)
"""
import functools, html, itertools, re, sys, unicodedata
import pymupdf as fitz
sys.path.insert(0, __import__("os").path.dirname(__file__))
import notebooklm_birlestir as nb
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.platypus import PageBreak, Paragraph, SimpleDocTemplate, Spacer

fitz.TOOLS.mupdf_display_errors(False)


@functools.lru_cache(maxsize=None)
def _gecersiz(ch):
    """NUL vb. kontrol karakterleri, özel kullanım alanı, U+FFFD ve yazı tipinde glifi olmayan
    karakterler (çıktıda NUL olarak çıkıyor; NotebookLM ayrıştırıcısını bozabiliyor)."""
    if ch in "\n\t":
        return False
    if unicodedata.category(ch) in ("Cc", "Co", "Cs", "Cn") or ch == "\ufffd":
        return True
    return not ch.isspace() and not _font().has_glyph(ord(ch))


@functools.lru_cache(maxsize=1)
def _font():
    return fitz.Font(fontfile=nb.FONT_YOLU)


def temiz(t):
    t = "".join(ch for ch in t if not _gecersiz(ch))
    t = t.replace("­", "").replace("\r", "")
    t = re.sub(r"-\n(?=\w)", "", t)              # satır sonu tirelemesi
    t = re.sub(r"(?<![.!?:;\"”»])\n(?!\n)", " ", t)  # paragraf içi satır kırılmaları
    t = re.sub(r"[ \t]+", " ", t)
    return t.strip()


def main(girdi, cikti, secim=None, baslik=None):
    """secim: yalnızca bu sıra numaralı kaynakları al (0 tabanlı); baslik: kapak/metadata başlığı."""
    nb.FONT_YOLU = nb.font_kaydet(None)
    st = nb.stiller()
    src = fitz.open(girdi)
    tum = src.get_toc()
    sinir = [e[2] for e in tum] + [len(src) + 1]
    secim = list(range(len(tum))) if secim is None else secim
    toc = [tum[i] for i in secim]
    baslik = baslik or src.metadata.get("title") or "Paket"
    hikaye = [Paragraph(html.escape(baslik), st["baslik"]),
              Paragraph("İçindekiler (yalnızca metin sürümü)", st["alt"]), Spacer(1, 12)]
    for e in toc:
        hikaye.append(Paragraph(html.escape(e[1]), st["madde"]))
    hikaye.append(PageBreak())
    for i, e in zip(secim, toc):
        bas, son = sinir[i], sinir[i + 1] - 1   # e[2]: ayraç sayfası (1 tabanlı)
        ayrac = "".join(ch for ch in src[bas - 1].get_text() if not _gecersiz(ch)).strip().split("\n")
        hikaye += [Spacer(1, 5 * cm), Paragraph(html.escape(e[1]), st["baslik"])]
        hikaye += [Paragraph(html.escape(s), st["alt"]) for s in ayrac[1:] if s.strip()]
        hikaye.append(PageBreak())
        for n, p in enumerate(range(bas, son), 1):   # kaynak sayfaları: bas .. son-1 (0 tabanlı)
            t = temiz(src[p].get_text())
            if not t:
                continue
            hikaye.append(Paragraph(f"<b>— s. {n} —</b>", st["govde"]))
            for parca in re.split(r"\n{2,}", t):
                hikaye.append(Paragraph(html.escape(parca), st["govde"]))
        hikaye.append(PageBreak())
    gecici = cikti + ".tmp.pdf"
    SimpleDocTemplate(gecici, pagesize=A4, leftMargin=2 * cm, rightMargin=2 * cm,
                      topMargin=1.8 * cm, bottomMargin=1.8 * cm,
                      title=baslik if secim != list(range(len(tum))) else baslik + " (metin)").build(hikaye)
    # Yer imleri: ayraç başlıklarının geçtiği sayfaları bul
    out = fitz.open(gecici)
    yeni_toc = []
    for e in toc:
        anahtar = " ".join(e[1].split()[:4])  # satır kaymasına dayanıklı kısa anahtar
        for i, pg in enumerate(out):
            if i > 0 and anahtar in " ".join(pg.get_text().split()) and (not yeni_toc or i + 1 > yeni_toc[-1][2]):
                yeni_toc.append([1, e[1], i + 1])
                break
    out.set_toc(yeni_toc)
    out.save(cikti, garbage=4, deflate=True)
    import os
    os.remove(gecici)
    w = sum(len(re.findall(r"\w+", pg.get_text())) for pg in out)
    print(f"{cikti}: {len(out)} sayfa, {w:,} kelime, {os.path.getsize(cikti)/1048576:.1f} MB, yer imi {len(yeni_toc)}/{len(toc)}")


def kitap_basina(girdi, klasor):
    """Paketteki her kaynağı ayrı, yalnızca metin içeren bir PDF olarak yazar."""
    import os
    nb.FONT_YOLU = nb.font_kaydet(None)
    st = nb.stiller()
    os.makedirs(klasor, exist_ok=True)
    src = fitz.open(girdi)
    paket = re.sub(r"\s*-\s*Cilt \d+$", "", src.metadata.get("title") or "Paket")
    kod = paket.split(" - ")[0]
    toc = src.get_toc()
    sinir = [e[2] for e in toc] + [len(src) + 1]
    for i, e in enumerate(toc):
        baslik = re.sub(r"^\d+\.\s*", "", e[1])
        bas, son = sinir[i], sinir[i + 1] - 1
        hikaye = [Spacer(1, 5 * cm), Paragraph(html.escape(baslik), st["baslik"]),
                  Paragraph(html.escape(f"{paket} paketinden"), st["alt"]), PageBreak()]
        for n, p in enumerate(range(bas, son), 1):
            t = temiz(src[p].get_text())
            if not t:
                continue
            hikaye.append(Paragraph(f"<b>— s. {n} —</b>", st["govde"]))
            for parca in re.split(r"\n{2,}", t):
                hikaye.append(Paragraph(html.escape(parca), st["govde"]))
        ad = nb.guvenli_ad(f"{kod} - {baslik}")[:120] + ".pdf"
        hedef = os.path.join(klasor, ad)
        SimpleDocTemplate(hedef, pagesize=A4, leftMargin=2 * cm, rightMargin=2 * cm,
                          topMargin=1.8 * cm, bottomMargin=1.8 * cm, title=f"{kod} - {baslik}").build(hikaye)
        d = fitz.open(hedef)
        w = sum(len(re.findall(r"\w+", pg.get_text())) for pg in d)
        print(f"{ad}: {len(d)} sayfa, {w:,} kelime, {os.path.getsize(hedef)/1048576:.1f} MB")


# Yazarı olmayan kaynaklar için elle verilmiş kısa etiketler (başlık başı → etiket)
ETIKET = {"Bilişsel Davranışçı Psikoterapiler Kongresi": "BDT Kongresi",
          "Bilinçli Farkındalık Temelli": "Farkındalık-OKB",
          "European Society of Hypnosis": "ESH Bülteni"}


def kisa_etiket(baslik):
    """Kaynak başlığından dosya adı için kısa etiket: yazar soyadı(ları) ya da ilk kelime."""
    t = re.sub(r"\s*\(.*?\)", "", re.sub(r"^\d+\.\s*", "", baslik)).strip()
    for bas, etiket in ETIKET.items():
        if t.startswith(bas):
            return etiket
    if " — " in t:
        sol, sag = t.split(" — ", 1)
        kisiler = [k.strip() for k in sag.split("&")]
        if all(k and all(w[0].isupper() for w in k.split()) for k in kisiler):
            return " & ".join(k.split()[-1] for k in kisiler)
        return " ".join(sol.split()[:2])
    return t.split()[0]


def parcala(girdi, klasor, n=2, ilk_harf="a", paket_adi=None):
    """Paketi kitap bölmeden, kelime sayısı en dengeli n dosyaya ayırır (K1a, K1b ...).
    paket_adi: dosya adında kullanılacak Türkçe karakterli paket adı (verilmezse PDF başlığı)."""
    import os
    os.makedirs(klasor, exist_ok=True)
    src = fitz.open(girdi)
    toc = src.get_toc()
    sinir = [e[2] for e in toc] + [len(src) + 1]
    kelime = [sum(len(re.findall(r"\w+", src[p].get_text())) for p in range(sinir[i], sinir[i + 1] - 1))
              for i in range(len(toc))]
    paket = re.sub(r"\s*-\s*Cilt \d+$", "", src.metadata.get("title") or "Paket")
    kod, _, ad = paket.partition(" - ")
    ad = paket_adi or ad
    # En büyük parçayı küçülten atama (kaynak sayısı az: kaba kuvvet yeterli)
    en_iyi = min((a for a in itertools.product(range(n), repeat=len(toc)) if len(set(a)) == n),
                 key=lambda a: (max(sum(k for k, g in zip(kelime, a) if g == j) for j in range(n)), a))
    gruplar = sorted(([i for i, g in enumerate(en_iyi) if g == j] for j in range(n)), key=lambda g: g[0])
    for j, grup in enumerate(gruplar):
        harf = chr(ord(ilk_harf) + j)
        if len(grup) == 1:
            t = re.sub(r"\s*\(.*?\)", "", re.sub(r"^\d+\.\s*", "", toc[grup[0]][1]))
            kitap, _, yazar = t.partition(" — ")
            isim = f"{kod}{harf} - {kitap.strip()}" + (f" ({kisa_etiket(toc[grup[0]][1])})" if yazar else "")
        else:
            isim = f"{kod}{harf} - {ad} ({', '.join(kisa_etiket(toc[i][1]) for i in grup)})"
        main(girdi, os.path.join(klasor, nb.guvenli_ad(isim)[:150] + ".pdf"), secim=grup, baslik=isim)


if __name__ == "__main__":
    if sys.argv[1] == "--kitap-basina":
        kitap_basina(sys.argv[2], sys.argv[3])
    elif sys.argv[1] == "--parca":
        a = sys.argv[2:]
        ad = a[a.index("--ad") + 1] if "--ad" in a else None
        a = [x for i, x in enumerate(a) if x != "--ad" and (i == 0 or a[i - 1] != "--ad")]
        parcala(a[1], a[2], int(a[0]), a[3] if len(a) > 3 else "a", ad)
    else:
        main(sys.argv[1], sys.argv[2])
