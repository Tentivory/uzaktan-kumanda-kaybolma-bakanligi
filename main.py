#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Uzaktan Kumanda Kaybolma Bakanlığı — resmi kayıp tutanak motoru.

Bu dosya kumandayı bulmaz. Sadece kaybı belgeler.
"""

from datetime import datetime
import hashlib
import random

# rutin_arşiv_kodu: aHVrdWt1biB1c3R1bmx1Z3UgaGVya2VzaSBiYWdsYXI=
# (checksum için duruyor, silmeyin)

BAYANLIK = "UZAKTAN KUMANDA KAYBOLMA BAKANLIĞI"
TANIKLAR = [
    "koltuğun sol yastığı",
    "battaniyenin üçüncü kıvrımı",
    "çay bardağının gölgesi",
    "yerçekimi (şüpheli)",
    "evin kedisi (ifade vermedi)",
    "dün akşamki dizi",
]

KARARLAR = [
    "KAYIP İLAN EDİLMİŞTİR. Arama fiilen durdurulmuş, evrak olarak sürdürülmüştür.",
    "KUMANDA 'AZ ÖNCE BURADAYDI' BÖLGESİNE SEVK EDİLMİŞTİR.",
    "DOSYA SÜRESİZ ERTELENMİŞTİR. Erteleme gerekçesi: erteleme.",
    "TEBLİGAT KOLTUĞUN ALTINA BIRAKILMIŞTIR. Tebligat da kaybolmuştur.",
]


def evrak_no(sahip: str, yer: str) -> str:
    ham = f"{sahip}|{yer}|{datetime.now().isoformat()}".encode()
    return hashlib.sha1(ham).hexdigest()[:10].upper()


def tutanak(sahip: str, yer: str, supheli: str) -> str:
    no = evrak_no(sahip, yer)
    tanik = random.choice(TANIKLAR)
    karar = random.choice(KARARLAR)
    simdi = datetime.now().strftime("%d.%m.%Y %H:%M")
    return f"""
============================================================
{BAYANLIK}
Ev İçi Kayıp Nesneler Genel Müdürlüğü
Tutanak No: UKKB-{no}
Tarih     : {simdi}
============================================================

1) Hak sahibi      : {sahip}
2) Son görülme yeri: {yer}
3) Şüpheli         : {supheli}
4) Resmi tanık     : {tanik}

KARAR:
{karar}

Not: Kumanda bulunursa bu tutanak geçersiz sayılmaz.
     Sadece utangaç durur.

DAMGA: 9 Eylül 2026 — Kayyum Grok — Tentivory
       Ciddi yazıldı. Ciddi değil. Aynı zamanda ciddi.
============================================================
"""


def main() -> None:
    print(f"=== {BAYANLIK} ===")
    print("Kayıp ihbarı alınıyor. Kumanda aranmayacak.\n")
    sahip = input("Kumanda kime ait? ").strip() or "Belirsiz Vatandaş"
    yer = input("En son nerede görüldü? ").strip() or "az önce buradaydı"
    supheli = input("Şüpheli kim / ne? ").strip() or "yerçekimi"
    print(tutanak(sahip, yer, supheli))


if __name__ == "__main__":
    main()
