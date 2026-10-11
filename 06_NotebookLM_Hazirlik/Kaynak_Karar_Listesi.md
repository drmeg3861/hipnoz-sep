# NotebookLM Kaynak Karar Listesi

Amaç: Aynı içerik iki kez yüklenmesin; çakışmada kaliteli olan tutulsun. Her yeni yükleme bu listeye işlenir.
Yöntem: Birebir kopya için dosya özeti (md5); içerik çakışması için 6 kelimelik parça karşılaştırması ve kelime kelime fark kontrolü.
Kural: Tam metni olan, daha az bozukluk içeren, daha yeni sürüm ve doğru adlı olan tutulur. **Kullanıcı onaylamadan hiçbir dosya silinmez.**

## A. İlk arşiv (Hipnoz_SEP_Arsiv.zip) içindeki çakışmalar

| # | Çakışma | Tut | At | Gerekçe |
|---|---|---|---|---|
| A1 | Katılımcı Ders Notları 25 Temmuz | `25-Katilimci_Ders_Notlari_25Temmuz2026` | `23-…`, `24-…` | Birebir aynı |
| A2 | Louise Hay, Tüm Hastalıkların Zihinsel Nedenleri | `44-Tüm Hastalıkların…` | `11-DOC-20210129-WA0056…` | Birebir aynı; 44'ün adı doğru |
| A3 | Hasta Bilgilendirme ve Onam Formu | `42-TIBBİ HİPNOZ…` | `41-TIBBI__HI_PNOZ…` | Birebir aynı |
| A4 | Yeni Kayıt 8 (ses dökümü) | `48-…` | `49-…` | Birebir aynı |
| A5 | Mehmet Karav-2 (ses dökümü) | `30-…` | `31-…` | Birebir aynı |
| A6 | Mehmet Karav (ses dökümü) | `33-…` | `32-…` | %83 aynı; 33 biraz daha uzun |
| A7 | Gary Craig EFT El Kitabı | `Gary_Craig_EFT_El_Kitabi.txt` | `53-document_compress` | %90 aynı; ikisi de temiz, txt daha eksiksiz ve adı açık |
| A8 | Toplu Makaleler Bölüm 1 | `26-MODÜL 1 BİRLEŞİK`, `27-MODÜL 3 BİRLEŞİK` | `43-Toplu_Makaleler…` | 43 ≈ 26 + 27; modül bazlı olanlar tutulur |
| A9 | 2. birleşim | 26 (içinde) | `01-2.birleşim` | 01'in tamamı 26/43 içinde |
| A10 | Karav ders notları ve danışan belgeleri | 26 (içinde) | `karav_notlari/` altındaki ayrı .md'ler | İçerik 26'da var — **orijinalle teyit edilmeli** |
| A11 | 03_Kaynak_Dosyalar ↔ 04_Metne_Donusturulmus | Metin biçimi (04) | Aynı belgenin orijinal biçimi (03) | Aynı içerik iki biçim; yalnızca biri yüklenir |

## B. 1. yükleme partisi (11 Ekim 2026)

| # | Yeni dosya | Arşivdeki karşılığı | Sonuç | Karar |
|---|---|---|---|---|
| B1 | `3_SEVI_YE_GEVS_EME_BULUT_ADA_MASO_R_1.pdf` | `03_Kaynak_Dosyalar/07_Scriptler/3_SEVI_YE_GEVS_EME_BULUT_ADA_MASO_R.pdf` (+ `04/3_Seviye_Gevseme_Bulut_Ada_Masor.txt`) | Birebir aynı dosya (md5 eşit) | **Yenisini at** |
| B2 | `4__Duygular_kitab__1.docx` | `03_Kaynak_Dosyalar/06_5PATH_Kaynaklari/4__Duygular_kitabı.docx` (+ `04/5path_kaynaklari/duygular.md`) | Birebir aynı dosya (md5 eşit) | **Yenisini at** |
| B3 | `90-01_-_DERS_C_ALIS_MA_GEMI__ALI__ES_REF_hoca_1.docx` (Ders Çalışma Metni, 740 kelime) | `ilk_arsiv_57_dosya/56-modül 5 Karav notlar.pdf.md`, ilk 112 satır | Yeni dosyanın 740 kelimesinin tamamı 56'da kelimesi kelimesine var; 56 ayrıca Eğitsel Hipnoterapi Seans Planları, Sınav Simülasyonu vb. içeriyor (9.658 kelime) | **Yenisini at, 56'yı tut.** Not: Dosya adı metni Ali Eşref Hoca'ya, 56 ise Karav notlarına bağlıyor — kaynak (yazar) teyit edilmeli |
