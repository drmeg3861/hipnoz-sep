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

## C. 2. yükleme partisi (11 Ekim 2026)

| # | Yeni dosya | Arşivdeki karşılığı | Sonuç | Karar |
|---|---|---|---|---|
| C1 | `adli-hipnoz.pdf.pdf` (29 sayfa, Dumanlı–Karadeniz–Hancı) | `03_Kaynak_Dosyalar/03_Kitaplar_ve_Makaleler/adli-hipnoz_pdf.pdf` (+ `04/Adli_Hipnoz_makalesi.txt`, 7.094 kelime) | Birebir aynı dosya (md5 eşit) | **Yenisini at.** Notlarda özeti zaten var (Modül 7 → Makale Özeti — Adli Hipnoz) |

## D. Drive "hipnoz sep" klasörü (11 Ekim 2026, 95 dosya — katalog: `drive_katalog.tsv`)

Yöntem notu: Küçük ders dosyalarının metni Drive bağlantısıyla okundu ve arşivle ifade düzeyinde karşılaştırıldı. Büyük kitaplar indirilemedi (ağ izni yok); bunlar ad + bayt boyutu + arşivdeki metin karşılığıyla değerlendirildi.

### D1. Arşivde zaten olanlar → NotebookLM'e yeniden yükleme

| Drive dosyası | Arşivdeki karşılığı | Kanıt |
|---|---|---|
| 3 SEVİYE GEVŞEME BULUT ADA MASÖR (1).pdf | 03/07_Scriptler/… | Bayt boyutu eşit (150.006) — B1 ile aynı |
| adli-hipnoz.pdf.pdf | 03/03_Kitaplar… | md5 eşit — C1 |
| 4 Duygular kitabı (1).docx | 03/06_5PATH… | Bayt boyutu eşit (27.498) — B2 |
| 90-01 DERS ÇALIŞMA GEMİ ALİ EŞREF hoca (1).docx | 56-modül 5 Karav notlar | Bayt boyutu eşit (18.717) — B3 |
| Gary H. Craig - EFT Duygusal Özgürlük Teknikleri.pdf | 03/03_Kitaplar… + `Gary_Craig_EFT_El_Kitabi.txt` | Bayt boyutu eşit (1.045.351) |
| document_compress.pdf | 53-document_compress (= Gary Craig EFT metni) | Ad eşleşmesi; A7 |
| Charles Duhigg Alışkanlıkların Gücü.pdf | 03/03_Kitaplar… | Bayt boyutu eşit (4.317.193) |
| Tüm Hastalıkların Zihinsel Nedenleri - Louise L. Hay.pdf | 44-… | Ad eşleşmesi; A2 |
| DOC-20210129-WA0056_241111_115035.pdf | 11-… (= Louise Hay) | Ad eşleşmesi; A2 |
| TIBBİ HİPNOZ HİPNOTERAPİ HASTA BİLGİLENDİRME VE ONAM FORMU.pdf | 42-… | Ad eşleşmesi; A3 |
| Zihin Okuma Teknikleri - Stan B. Walters.pdf | 50-… (40.790 kelime) | Ad eşleşmesi |
| İmgesel Görüntü Yaşantısı - Ali Nahit Babaoğlu.pdf | 21-… (29.656 kelime) | Ad eşleşmesi |
| Rob Brotherton - Şüpheci Zihinler.pdf | 38-… (77.906 kelime) | Ad eşleşmesi |
| Clinical_EFT_Blueprint.pdf + Clinical_EFT_Blueprint2.pdf | 04/slayt_setleri_OCR/13- ve 14-Clinical_EFT_Blueprint | İkisi aynı boyutta (12.904.823) → birbirinin kopyası; görsel slayt, metni OCR ile arşivde var |
| ERICSON-SESIM_SENINLE.pdf | 35-Milton H. Erickson Sesim Seninle Her Yerde (54.798 kelime) | Aynı kitap; farklı dosya — indirilince metin karşılaştırılacak |
| dave-elman-hypnotherapy (1).pdf | 52-… | **Metin katmanı yok (arşivde 0 kelime) → taranmış; OCR gerekir.** OCR'sız yüklenirse NotebookLM okuyamayabilir |

### D2. 56-modül 5 Karav notlar'ın parçaları (56 = bu 6 dosyanın birleşimi)

| Drive dosyası | 56'daki yeri |
|---|---|
| 90-01 DERS ÇALIŞMA GEMİ ALİ EŞREF hoca (1).docx | Satır 1–~100 |
| egitsel metin (gemi zaman kapısı şelale) (1).txt | Satır ~100–112 (gemi, zaman, arındırıcı şelale) |
| EĞİTSEL HİPNOTERAPİ SEANS PLANLARI (1).pptx | Satır 113–~209 |
| eğitsel hipnoz ışık topu kütüphane (1).txt | Satır 210–218 |
| Hafıza kütüphanesi (1).docx | Satır 220–~376 |
| sinav_korkusu (1).docx | Satır 377–498 |

**Karar:** Ya 56 ya bu 6 dosya — ikisi birden değil. Birleşik "Eğitsel Hipnoz" kaynağında **orijinaller** kullanılacak (PDF'ten çıkarılmış 56'ya göre daha temiz metin, satır kırılması yok), 56 atlanacak.

### D3. Soru dosyaları

| Dosya | İçerik | Karar |
|---|---|---|
| Hipnoz soru bankası_260805_120729.pdf | 23 soru | **TUT (yeni)** |
| sorulasar.docx | İlk 11 soru = soru bankasındakiler; "8 — Kendini Sınama" bölümü = Katılımcı Ders Notları Bölüm 8 (arşivde) | AT |
| sorular.pdf | 2 soru = soru bankası 22–23 | AT |

### D4. Yeni ders materyali (arşivde yok)

| Dosya | Not | Karar |
|---|---|---|
| eğitsel hipnoz script.docx / eğitsel script.pdf | Aynı metin (Eğitsel Hipnoz Klinik Uygulama Protokolü, 6 bölüm + 90 saniye kuralı). PDF'in son kelimesi kesik; docx'te markdown işaretleri var | **Birini tut** (docx; birleştirmede işaretler temizlenecek) |
| Karav 2 EFT parts five path - 03.10.2026 13.51.51.docx | Modül 7 ders dökümü (konuşmadan yazıya, hatalı). Karav Hoca'nın 5-PATH + EFT tek seans protokolü, Parts terapiye geçiş ölçütü, seans sonrası 1/3–4/4–6 hafta takip | **TUT** — ayrıca ders notlarına işlenmeli |

### D5. Aynı kitabın birden çok sürümü

| Kitap | Sürümler | Karar |
|---|---|---|
| Nossrat Peseschkian — Doğu Hikayeleriyle Psikoterapi | (1) 633.829 B, (2) Anna's Archive 202.972 B, (3) ilide.info 388.684 B | Biri tutulacak; indirilince sayfa/kelime sayısıyla en eksiksizi seçilecek (ilide.info genelde önizleme sürümüdür) |

### D6. Arşivde karşılığı olmayan kitap/makaleler (kopya değil)

Klinik Hipnozun Esasları (Lynn & Kirsch) · Sıradışı Terapi (Jay Haley) · Hipnoz Telkinleri (Bülent Uran) · Kendi Kendine Hipnoz (Elaine Sheehan) · 101 Healing Stories (G. W. Burns) · Pozitif Psikoterapiye Giriş (Peseschkian) · 101 Oyun Terapisi Tekniği (Kaduson & Schaefer) · BDT Kongresi — Çocuk ve Ergenlerde · Bilinçli Farkındalık Temelli BT — Obsesif · NEFES ve GEVŞEME EGZERSİZLERİ · enerji kilit noktaları meridyenler notlar · Plasebo Sensin (Joe Dispenza) · Daha İyi Bir Beyin (Perlmutter) · Madde ve Bilinç (Churchland) · Bilinçaltı Zihninizin Gücü (C. James Jensen) · Stres Altında Başarılı Olmak (Loehr) · Açıklanan Bilinç Haritası (Hawkins) · Babanın Adları (Lacan) · Enneagram'ın Spiritüel Boyutu (Maitri) · Teosofi ve Yeni Psikoloji (Besant) · Doğa Üstü Olmak (Nisargadatta) · İbn Sina Metafiziği (Altıntaş) · İbn-i Sina Şifa Kitabı

### D7. Görseller (WhatsApp, 11 Ekim)

| Görsel | İçerik | Karar |
|---|---|---|
| 13.40.41, 13.40.41 (1), 13.40.42, 13.40.42 (1), (2), (3), (4) | Plasebo Sensin (Dispenza) kitap sayfası fotoğrafları (Vance Vanders vakası, Şekil 6.4–6.8) | AT — kitabın PDF'i klasörde var |
| 13.40.48 | David Snyder — bilinçaltından gelen cevapların 6 özelliği | AT — ders notlarında (Modül 7) birebir var |
| 13.40.47 | Dan Siegel — Beynin El Modeli (İngilizce) | TUT (küçük; birleşik pakete metin olarak eklenebilir) |
| 13.40.48 (1) | Metin çıkmadı | Gözle bakılmalı |

### D8. Ses kayıtları

| Durum | Dosyalar |
|---|---|
| Arşivde dökümü var (yeniden yüklemeye gerek yok) | AUD-20260714-WA0023/0024 · AUD-20260822-WA0009/0010/0011 · AUD-20260823-WA0001/0002 · Eft · İkna için · Self hipnoz · Mehmet karav · Mehmet karav hipnoz |
| Kendi aralarında birebir kopya | "Mehmet karav 1.5 mb olan", "Mehmet karav 3.1mb 2.si", "Mehmet karav 3.1 mb" — üçü de 3.051.601 bayt → birini tut (ad yanıltıcı) |
| Arşivde karşılığı belirsiz | Mehmet karav 1.1 mb (arşivdeki 29-/30- Mehmet_karav-1/-2 ile eşleşebilir — dinleyerek teyit) |
| Dökümü yok (yeni) | AUD-20260802-WA0011 · AUD-20260809-WA0055/0056 · AUD-20260824-WA0003…WA0011 (9 dosya) · Ses 260906_112515 · Ses 260906_134526 · Zeynep · Safi · Bülent seans |
| **Gizlilik** | "Zeynep", "Safi", "Bülent seans" kişi adı taşıyor; seans kaydıysa kişilerin onamı olmadan paylaşılmamalı |

## E. Semih Emre Ayyıldız'ın paylaştığı Drive klasörleri (11 Ekim 2026 — katalog: `semih_hoca_katalog.tsv`)

7 klasör (Modül 1, seans metinleri, Modül 2, Modül 3, Medya ve Kaynaklar, kitap tavsiyeleri [boş], film-video tavsiyeleri) + kökte 1 doküman; **49 dosya, 111 MB.** Metin içeren 30 dosyanın metni okunup arşivle 6 kelimelik parça karşılaştırmasıyla eşleştirildi.

### E1. Arşivde birebir olanlar (aynı bayt boyutu) — 16 dosya
temel hipnoz eğitimi ders notları.docx · Danışan Formu.docx · 6.Danışan Bilgi Notu.doc · 7.Hipnoz Terapisi Aydınlatılmış Onam Formu.docx · 5.Hipnozun Anayasası.doc · 2.Hipnoz Olmaya Hazır mısınız.docx · 4.Kolay Hipnoz Olma Rehberi.doc · Randevular hakkında REVİZE.docx · SUNUM 1.pptx · SUNUM 2.pptx · hipnozun Derinlikleri.pptx · beyin dalgaları.pptx (yalnızca görsel, metin yok) · ANA SUNUM temel HİPNOZ EĞİTİMİ.pptx · 5-Path Kullanma Klavuzu.docx · ESHNSL2024 Autumn.pdf (89 MB; metni `ESH_Bulten_2024_Sonbahar.txt`) · PHOTO-2024-10-25-18-35-59.jpg

**Yazar notu:** Arşivde "Dr. Mehmet Karav Notları" klasöründe duran bu belgeler Drive'da Semih Hoca'nın "Modül 1" klasöründe. Hangisinin hazırladığı teyit edilmeli (ders notlarındaki atıflar buna göre düzeltilir).

### E2. Arşivdeki birleşik PDF'lerin (26-MODÜL 1 / 27-MODÜL 3) içinde olanlar — 15 dosya
- **Modül 3 (katatim/ileri regresyon metinleri), %97–100'ü 27'de:** 1. Zincir Güven · 2. Hayat Bahçesi Af Öfke · 3. Gri Oda ve Tiyatro · 4. Kumdan Kale Ego Havuz ve Şelale · Bağışıklık Sistemi Koruyucu Kalkan · 154-02 İçsel Rehber Tekniği
- **seans metinleri, %100'ü 26'da:** 1) Mental Konfüzyon (Aç-Kapa) · 2) Asansörle İniş 10. Kat · 02) 10 Basamaklı Merdiven · 02) 20 Basamaklı Merdiven · 03) Ağırlaşma Telkini · 4) Z'den Geriye Sayma · 4) 99'dan Geriye Sayma · 3. Dave Elman Öğrenciler İçin
- linkler - bağlantılar (%91, 43 ve 01'de)

**Karar:** Bu dosyalar yeniden yüklenmez; 26 ve 27 tutulur. (Drive'daki Google Docs sürümleri daha temiz metin verdiği için birleşik pakette 26/27 yerine bunlar kullanılabilir — içerik aynı.)

### E3. Yeni — 1 dosya
| Dosya | İçerik | Karar |
|---|---|---|
| Medipol 2026 Hipnoz Eğitimi Soru Bankası (Google Doc) | ~46 soru (Pygmalion/Golem etkisi, pacing–leading, Sarbin & Coe rol kuramı, telkin edilebilirlik…). Arşivle örtüşme %1; kullanıcının "Hipnoz soru bankası" PDF'iyle (23 soru) de ayrı sorular | **TUT** — Soru bankası paketine |

### E4. Görseller ve video
| Dosya | İçerik | Karar |
|---|---|---|
| seans metinleri: PHOTO-2024-10-25-11-12-42/43, 2024-11-15-13-38-22, 2024-11-15-13-38-23 (iki farklı foto), 2024-11-23-10-36-05 | Semih Hoca'nın **el yazısı seans akışları**: dere–kaynak–iş makinesi, mağara ödülü ve fotoğraf çapası, hamak + 41 sihirli sandık + yanardağ, "geçmişe örtü çek / komşunun hikayesi" telkinleri. Bir kısmı arşivde yazılı hâlde yok | **TUT ama** OCR el yazısında çok bozuk → elle yazıya dökülmesi önerilir |
| Medya ve Kaynaklar: 10 foto | Kitap/film önerileri (Ters Yüz; Güçlü Sorular — Sobel & Panas; Hipnoterapi ve Hipnoanaliz — Brown & Fromm; Hipnoz: Bütüncül Tıbba Genel Bakış — ed. Dr. Mehmet Karav), meridyen saati şeması, bir zaman algısı esprisi, Louise Hay "Uçuklar" sayfası (kitap arşivde var); 3 fotodan metin çıkmadı | Kaynak olarak yüklemeye değmez; öneri listesi tek sayfa metin olarak pakete eklenebilir |
| VIDEO-2024-11-29-15-26-18.mp4 (11 MB) | film-video tavsiyesi | İzlenip karar verilmeli |

## F. İndirilen PDF'lerin tam metin analizi (11 Ekim 2026)

"hipnoz sep" klasöründeki 54 belge (44 PDF + Word/sunu/txt) indirildi; hepsi Drive'daki bayt boyutuyla aynı. Her PDF'in sayfa, kelime ve taranmış sayfa sayısı çıkarıldı; metinler arşivle tam (6 kelimelik parça) karşılaştırıldı.

### F1. D bölümündeki tahminlerin doğrulanması
| Eşleşme | Sonuç | Karar |
|---|---|---|
| Gary H. Craig EFT.pdf ↔ document_compress.pdf | %100 aynı metin | Biri tutulur |
| Louise Hay.pdf ↔ DOC-20210129-WA0056.pdf | Aynı kelime sayısı (13.219), aynı kitap | Louise Hay adı olan tutulur |
| Clinical_EFT_Blueprint ↔ Blueprint2 | md5 aynı; ikisi de tamamen görsel (11 sayfa, 0 kelime) | Arşivdeki OCR metni kullanılır |
| Peseschkian Doğu Hikayeleri ×3 | (1) ↔ ilide.info %100 aynı metin; Anna's Archive %98–99 aynı | **(1) tutulur** (105 sayfa, temiz ad); diğer ikisi atılır |
| ERICSON-SESIM_SENINLE ↔ arşiv 35 | Aynı kitap, farklı baskı/çıkarım (%68–78 örtüşme); Drive sürümü %20 daha uzun (64.991 / 54.210 kelime) | **Drive sürümü tutulur** |
| Zihin Okuma Teknikleri / Brotherton / İmgesel Görüntü ↔ arşiv | %72–98 örtüşme, aynı kitaplar | Biri tutulur (Drive PDF'leri orijinal düzende) |

### F2. Yeni bulgu: arşivdeki "02-3.birleşim" sizin önceki birleştirmeniz
140.707 kelimelik bu dosya şu Drive kitaplarını büyük ölçüde içeriyor: Açıklanan Bilinç Haritası (Hawkins) %100 · Bilinçli Farkındalık Temelli BT (Obsesif) %97 · BDT Kongresi Çocuk-Ergen %96 · Babanın Adları (Lacan) %89 · Bilinçaltı Zihninizin Gücü (Jensen) %45. **Ya 02 ya bu kitaplar — ikisi birden değil.**

### F3. Tamamen taranmış (metin katmanı yok) PDF'ler — OCR gerekli
| Dosya | Sayfa | Not |
|---|---|---|
| dave-elman-hypnotherapy (1).pdf | 352 | İngilizce; OCR kalitesi iyi |
| 101 oyun terapisi tekniği (Kaduson & Schaefer) | 202 | Türkçe; Tesseract (tur) ile ç/ğ/ı/ş doğru tanındı |
| "DOĞA ÜSTÜ OLMAK SRİ NİSARGADATTA.pdf" | 199 | **Dosya adı yanlış: içerik Joe Dispenza'nın "Doğaüstü Olmak" kitabı** (ilk sayfalar ve içindekiler OCR ile doğrulandı). Nisargadatta değil |
| Clinical_EFT_Blueprint (×2) | 11 | Arşivde OCR metni var |

OCR, görünmez metin katmanlı aranabilir sayfa olarak yapılır (sayfa başına ~150 KB, ~4–5 sn).

### F4. Metin katmanı olan ama arada taranmış sayfa içeren kitaplar
Çoğu kitapta 1–27 sayfa (kapak, görsel, tablo) metinsiz; betik bu sayfaları otomatik OCR'lar. En çok: BDT Kongresi (27), Lacan (22), Jensen (19), Brotherton (13), Zihin Okuma (10).

## G. Üretilen NotebookLM paketleri — yeni not defteri (11 Ekim 2026)

Betik: `arac/notebooklm_birlestir.py` (Tesseract tur+eng OCR, her kaynak için ayraç sayfası + yer imi, cilt başına ≤450.000 kelime). Eski birleşik dosyalar (01, 02, 26, 27, 43, 56) kullanılmadı: içeriklerinin %90–99'u tek tek kaynaklardan alındı, kalan kısım bozuk el yazısı OCR'ı ve satır kırılması farkıydı. Kitap PDF'leri telifli olduğu için repoya konmadı.

| # | PDF | Kaynak | Sayfa | Kelime | MB |
|---|---|---|---|---|---|
| 1 | D1 - Kurs Sunumları ve Ders Notları | 34 | 477 | 161.656 | 8,5 |
| 2 | D2 - Seans Metinleri, Telkinler ve Klinik Protokoller | 31 | 268 | 61.112 | 1,7 |
| 3 | D3 - Regresyon, 5-PATH, EFT ve Adli Hipnoz | 11 | 188 | 69.245 | 1,9 |
| 4 | D4 - Soru Bankaları | 3 | 36 | 5.755 | 1,3 |
| 5 | D5 - Ders Ses Kayıtları - Yazılı Dökümler | 20 | 75 | 20.111 | 0,6 |
| 6 | D6 - Formlar ve Danışan Belgeleri | 9 | 24 | 4.500 | 0,9 |
| 7 | K1 - Klinik Hipnoz ve Teknik | 6 | 1.276 | 292.842 | 22,3 |
| 8 | K2 - Erickson, Metafor ve Hikaye | 5 | 1.394 | 359.058 | 16,4 |
| 9 | K3 - Çocuk, BDT ve Oyun | 3 | 414 | 107.326 | 19,1 |
| 10 | K4 - Beyin, Zihin ve Beden - Cilt 1 | 2 | 576 | 202.252 | 26,9 |
| 11 | K4 - Beyin, Zihin ve Beden - Cilt 2 | 4 | 1.030 | 241.438 | 12,4 |
| 12 | K5 - Felsefe, Psikanaliz ve Spiritüel - Cilt 1 | 5 | 1.079 | 273.026 | 23,6 |
| 13 | K5 - Felsefe, Psikanaliz ve Spiritüel - Cilt 2 | 1 | 690 | 180.214 | 6,6 |
| 14 | K6 - Diğer Kitaplar ve Yayınlar | 7 | 1.426 | 350.261 | 27,1 |

K1, K3, K4 ve K5-Cilt 1'de OCR'lanmış/taranmış sayfa görüntüleri gri tonlamaya çevrilip küçültüldü (gönderim sınırı 30 MB); metin katmanı ve kelime sayıları birebir korundu.

### Yeni not defterine ayrıca yüklenecek ses kayıtları (dökümü olmayan 17 kayıt, Drive "hipnoz sep")
AUD-20260802-WA0011 · AUD-20260809-WA0055 · AUD-20260809-WA0056 · AUD-20260824-WA0003 · WA0004 · WA0005 · WA0006 · WA0007 · WA0008 · WA0009 · WA0010 · WA0011 · Ses 260906_112515 · Ses 260906_134526 · Zeynep · Safi · Bülent seans (son üçü kişi adlı — onam kontrolü)

### Pakete girmeyenler
El yazısı seans fotoğrafları (Semih Hoca, 6 adet — elle yazıya dökülmeli) · Modül 7 sınıf fotoğrafları (OCR okunamadı; içerik ders notlarında) · kitap/film öneri kapak fotoğrafları · VIDEO-2024-11-29 (film tavsiyesi) · ses kayıtlarının kendisi (dökümleri D5'te).

## H. Hocaların paylaştıkları — 2. Drive yüklemesi (11 Ekim 2026, "hipnoz sep" klasörü, 30 dosya)

Yöntem: md5 (birebir), parmak izi veritabanı (`parmak_izi.json.gz`, 198 kaynak) ile içerik karşılaştırması; eski .doc/.ppt için catdoc ve PowerPoint metin kayıtları doğrudan okundu.

### H1. Birebir kopya (16) — atla
3.5 PATH metinli özet · 5-Path Kullanma Klavuzu · 5 PATH Basamaklar · 1. 5 PATH ileri hipnoz sistemi · EĞİTSEL HİPNOTERAPİ SEANS PLANLARI (2) · egitsel metin gemi (2) · ışık topu kütüphane (2) ve (3) · Hafıza kütüphanesi (2) · sinav_korkusu (2) · 90-01 Ders Çalışma (2) · Milton H. Erickson Sesim Seninle Her Yerde (= ERICSON-SESIM_SENINLE, K2'de) · Louise Hay (1) · Tıbbi Hipnoz Onam Formu (1) · Using_Medical_Hypnosis…EFT (1) (= kendi eşi)

### H2. İçerik aynı (dosya farklı) — atla
| Dosya | Karşılığı | Örtüşme |
|---|---|---|
| HGSHS-A Puanlama Formu.pdf | arşiv 14 (D1) | %96/%100 |
| sözsüz indüksiyon adımları.pdf / yazıları.pdf | arşiv 57/58 (D1) | %100 |
| İndüksiyon ve Derinleştirme.pdf (Canva, 107 slayt) | arşiv 22 (D1) | %90/%97 |
| İndüksiyon ve derinleştirme teknikleri anlatılan.pptx | arşiv 51 (D1) | %89/%86 |
| 3.DAVE ELMAN Öğrenciler için.docx | Semih Hoca seans metinleri (D2) | %100 |
| SB MEDİPOL sunu 11-12 Temmuz.ppt (eski format) | arşiv 39 (D1) | %90 (metin, slayt kayıtlarından çıkarıldı) |
| David J. Lieberman — Zihin Okuma Oyunları.pdf | arşiv 12 metni (K6) | %70 — aynı kitap; **PDF daha düzgün**, K6 yeniden üretilirse bu kullanılabilir |
| Peseschkian — Doğu Hikayeleriyle Psikoterapi [Beyaz] (225 s) | K2'deki sürüm | Aynı kitap ve çeviri (Hürol Fışıloğlu); bu baskının OCR'ı daha hatalı → K2 sürümü tutuldu |

### H3. Yeni veya daha iyi sürüm → **H1 - Hocaların Paylaştıkları (Ekim 2026).pdf** (6 kaynak, 163 sayfa, 7.704 kelime, 5,5 MB)
| Kaynak | Not |
|---|---|
| Hipnoz Eğitimi Ders Programı 2026 (resmî PDF) | Yeni |
| medipol-hipnoz-program-katilimci.xlsx → ders ders tablo | Arşiv 54'ün PDF'inde konu/modül/eğitmen sütunları kaybolmuştu; tablo tam hâli |
| KATATİMİ.pdf (63 slayt) | Yeni; 19 görsel sayfa OCR'landı |
| Tıbbi Hipnoz Uygulamalarının EFT ile Birlikte Kullanımı — Dr. Semih Emre Ayyıldız (70 slayt) | Yeni; 21 görsel sayfa OCR'landı |
| 4.Hipnozun Anayasası.doc | Farklı sürüm: "Kendimi affetmeyi istiyorum" maddesi eklenmiş, affetme maddeleri yeniden sıralanmış |
| 5.Kolay Hipnoz Olma Rehberi.doc | Genişletilmiş sürüm (+~40 kelime: reklamcılar örneği, "trying is lying", "ben şimdi hipnozda mıyım?") |

### H4. Ek ses kayıtları (11 Ekim 2026)
| Dosya | Sonuç |
|---|---|
| WhatsApp Audio 2026-10-11 at 18.15.44.opus | md5 = AUD-20260714-WA0023.opus (3 dk 31 sn) — birebir aynı; dökümü D5'te |
| WhatsApp Audio 2026-10-11 at 18.15.44 2.opus | Aynı dosyanın ikinci kopyası |

### G2. NotebookLM'in reddettiği paketler ve çözüm (11 Ekim 2026)
NotebookLM K1, K3, K4 (Cilt 1–2), K5 Cilt 1 ve K6'yı yüklemedi (K2, K5 Cilt 2, D1–D6, H1 yüklendi). Boyut, kelime ve sayfa sayısı ortak neden değil. Çözüm: `arac/metin_surumu.py` ile **yalnızca metin** sürümleri (görselsiz; OCR katmanları dahil; her kaynak için ayraç + yer imi; asıl sayfa no "— s. N —" işaretiyle):

| PDF (metin) | Sayfa | Kelime | MB |
|---|---|---|---|
| K1 - Klinik Hipnoz ve Teknik | 518 | 295.033 | 1,5 |
| K3 - Çocuk, BDT ve Oyun | 209 | 107.874 | 0,6 |
| K4 - Beyin, Zihin ve Beden - Cilt 1 | 372 | 203.740 | 1,2 |
| K4 - Beyin, Zihin ve Beden - Cilt 2 | 467 | 243.625 | 1,5 |
| K5 - Felsefe, Psikanaliz ve Spiritüel - Cilt 1 | 509 | 273.949 | 1,6 |
| K6 - Diğer Kitaplar ve Yayınlar | 662 | 351.674 | 2,1 |

Ses: Zeynep.m4a aslında 3GPP kapsayıcısı (".m4a" uzantılı) → MP3'e çevrildi (22 dk, 10,1 MB). "Ses 260906_134526.m4a"nın kırmızı satırı aynı kaydın ikinci yüklemesi (ilki başarılı).

### G3. Yedek: kitap başına yalnızca-metin PDF'ler (27 dosya, toplam 9 MB)
Metin sürümleri de NotebookLM'de uzun süre işlenince (200–350 bin kelime/kaynak) aynı 6 paket `metin_surumu.py --kitap-basina` ile kitap başına bölündü: K1 (6), K3 (3), K4 (6), K5 Cilt 1 (5), K6 (7). Her dosya 2.600–127.000 kelime, 0,02–0,7 MB; dosya adları "K1 - Kitap adı — Yazar" biçiminde (hangi pakete ait olduğu korunur).

### G4. Kullanılacak sürüm: ikiye bölünmüş paketler (12 dosya, toplam 9,5 MB) — G2 ve G3'ün yerine
Kullanıcı 27 küçük dosya yerine her paketin ikiye bölünmesini istedi. `metin_surumu.py --parca 2` ile hata veren 6 dosyanın her biri kelime sayısı dengeli 2 parçaya ayrıldı. Kitaplar ortadan bölünmedi. Yalnızca metin var, her kaynağın ayracı ve yer imi duruyor.

**Ek bulgu:** Hata veren paketlerin metninde NUL (U+0000) karakterleri ve yazı tipinde karşılığı olmayan bozuk glifler vardı (ör. U+08F0). Bunlar çıktıda NUL olarak görünüyordu. Çalışan K2 ve K5 Cilt 2'de NUL yoktu. Bu karakterler artık temizleniyor; 12 dosyada geçersiz karakter sayısı 0.

| Dosya | İçerik | Sayfa | Kelime |
|---|---|---|---|
| K1a - Klinik Hipnoz ve Teknik (Lynn & Kirsch, Uran, Nefes, Enerji) | Lynn & Kirsch, Bülent Uran, Nefes egz., Enerji noktaları | 300 | 148.629 |
| K1b - Klinik Hipnoz ve Teknik (Elman, Sheehan) | Dave Elman (OCR), Elaine Sheehan | 219 | 146.418 |
| K3a - 101 Oyun Terapisi Tekniği (Kaduson & Schaefer) | 101 Oyun Terapisi (OCR) | 161 | 87.535 |
| K3b - Çocuk, BDT ve Oyun (BDT Kongresi, Farkındalık-OKB) | BDT Kongresi, Bilinçli Farkındalık–OKB | 49 | 20.354 |
| K4a - Plasebo Sensin (Dispenza) | Plasebo Sensin | 178 | 94.096 |
| K4b - Doğaüstü Olmak (Dispenza) | Doğaüstü Olmak (OCR) | 195 | 109.649 |
| K4c - Beyin, Zihin ve Beden (Perlmutter, Jensen) | Daha İyi Bir Beyin, Bilinçaltı Zihninizin Gücü | 234 | 121.737 |
| K4d - Beyin, Zihin ve Beden (Churchland, Loehr) | Madde ve Bilinç, Stres Altında Başarılı Olmak | 234 | 121.891 |
| K5a - Felsefe, Psikanaliz ve Spiritüel (Hawkins, Altıntaş) | Bilinç Haritası, İbn Sina Metafiziği | 239 | 133.612 |
| K5b - Felsefe, Psikanaliz ve Spiritüel (Lacan, Maitri, Besant) | Babanın Adları, Enneagram, Teosofi | 271 | 140.349 |
| K6a - Diğer Kitaplar ve Yayınlar (Duhigg, Lieberman, Hay) | Alışkanlıkların Gücü, Zihin Okuma Oyunları, Louise Hay | 326 | 174.695 |
| K6b - Diğer Kitaplar ve Yayınlar (Brotherton, Walters, Babaoğlu, ESH Bülteni) | Şüpheci Zihinler, Zihin Okuma Teknikleri, İmgesel Görüntü Yaşantısı, ESH Bülten | 337 | 176.966 |

K5 Cilt 2 (çalışıyor) eski adıyla kalır. NotebookLM'de G2 "metin" paketleri, G3 kitap başına dosyalar ve eski kırmızı K satırları **yüklenmemeli veya silinmeli**. Aynı kitaplar iki kez girmesin.
