#!/usr/bin/env python3
"""Birleşik paket PDF'inden yalnızca metin içeren (görselsiz) NotebookLM sürümü üretir.

Her kaynak için ayraç sayfası ve yer imi korunur; asıl kitap sayfaları
"— s. N —" işaretiyle metin içinde belirtilir. OCR katmanları da metne dahildir.
Kullanım: python3 metin_surumu.py girdi.pdf cikti.pdf
          python3 metin_surumu.py --kitap-basina girdi.pdf cikti_klasoru/   (her kaynak ayrı PDF)
"""
import html, re, sys
import pymupdf as fitz
sys.path.insert(0, __import__("os").path.dirname(__file__))
import notebooklm_birlestir as nb
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.platypus import PageBreak, Paragraph, SimpleDocTemplate, Spacer

fitz.TOOLS.mupdf_display_errors(False)


def temiz(t):
    t = t.replace("­", "").replace("\r", "")
    t = re.sub(r"-\n(?=\w)", "", t)              # satır sonu tirelemesi
    t = re.sub(r"(?<![.!?:;\"”»])\n(?!\n)", " ", t)  # paragraf içi satır kırılmaları
    t = re.sub(r"[ \t]+", " ", t)
    return t.strip()


def main(girdi, cikti):
    nb.FONT_YOLU = nb.font_kaydet(None)
    st = nb.stiller()
    src = fitz.open(girdi)
    toc = src.get_toc()
    sinir = [e[2] for e in toc] + [len(src) + 1]
    hikaye = [Paragraph(html.escape(src.metadata.get("title") or "Paket"), st["baslik"]),
              Paragraph("İçindekiler (yalnızca metin sürümü)", st["alt"]), Spacer(1, 12)]
    for e in toc:
        hikaye.append(Paragraph(html.escape(e[1]), st["madde"]))
    hikaye.append(PageBreak())
    for i, e in enumerate(toc):
        bas, son = sinir[i], sinir[i + 1] - 1   # e[2]: ayraç sayfası (1 tabanlı)
        ayrac = src[bas - 1].get_text().strip().split("\n")
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
                      title=(src.metadata.get("title") or "") + " (metin)").build(hikaye)
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


if __name__ == "__main__":
    if sys.argv[1] == "--kitap-basina":
        kitap_basina(sys.argv[2], sys.argv[3])
    else:
        main(sys.argv[1], sys.argv[2])
