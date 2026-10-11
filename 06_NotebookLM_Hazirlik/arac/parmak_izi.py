#!/usr/bin/env python3
"""Kaynak parmak izi veritabanı: kopya/çakışma tespiti için.

Her kaynağın metninden 6 kelimelik parçaların özetleri (hash) çıkarılır;
yalnızca 1/16'lık bir örnek saklanır (metnin kendisi saklanmaz).
Kullanım:
  python3 parmak_izi.py ekle  --db parmak_izi.json.gz --etiket "paket/kaynak" --metin dosya.txt [--dosya orijinal.pdf]
  python3 parmak_izi.py karsilastir --db parmak_izi.json.gz --metin yeni.txt
"""
import argparse, gzip, hashlib, json, os, re, sys

ORNEK = 16


def parcalar(metin, k=6):
    w = re.findall(r"\w+", metin.lower())
    for i in range(max(len(w) - k + 1, 0)):
        h = int.from_bytes(hashlib.blake2b(" ".join(w[i:i + k]).encode(), digest_size=8).digest(), "big")
        if h % ORNEK == 0:
            yield h


def oku_db(yol):
    if not os.path.exists(yol):
        return {}
    with gzip.open(yol, "rt", encoding="utf-8") as f:
        return json.load(f)


def yaz_db(yol, db):
    with gzip.open(yol, "wt", encoding="utf-8") as f:
        json.dump(db, f, ensure_ascii=False)


def karsilastir(db, metin, en_az=0.05):
    yeni = set(parcalar(metin))
    sonuc = []
    for etiket, kayit in db.items():
        eski = set(kayit["h"])
        if not yeni or not eski:
            continue
        ortak = len(yeni & eski)
        if ortak / len(yeni) >= en_az or ortak / len(eski) >= en_az:
            sonuc.append((ortak / len(yeni), ortak / len(eski), etiket))
    return len(yeni), sorted(sonuc, reverse=True)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("islem", choices=["ekle", "karsilastir"])
    ap.add_argument("--db", required=True)
    ap.add_argument("--metin", required=True)
    ap.add_argument("--etiket")
    ap.add_argument("--dosya")
    a = ap.parse_args()
    metin = open(a.metin, encoding="utf-8", errors="ignore").read()
    db = oku_db(a.db)
    if a.islem == "ekle":
        kayit = {"kelime": len(re.findall(r"\w+", metin)), "h": sorted(set(parcalar(metin)))}
        if a.dosya and os.path.exists(a.dosya):
            kayit["md5"] = hashlib.md5(open(a.dosya, "rb").read()).hexdigest()
            kayit["bayt"] = os.path.getsize(a.dosya)
        db[a.etiket] = kayit
        yaz_db(a.db, db)
    else:
        n, sonuc = karsilastir(db, metin)
        for c1, c2, e in sonuc[:10]:
            print(f"yeninin %{c1*100:.0f}'i | eskinin %{c2*100:.0f}'i | {e}")


if __name__ == "__main__":
    main()
