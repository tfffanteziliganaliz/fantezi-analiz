import json

def guncel_verileri_cek():
    print("Süper Lig tüm takımlar güncel fantezi kadroları işleniyor...")
    
    # Süper Lig Takımları ve Oyuncu Listesi (TFF Fantezi Puan Projeksiyonu)
    oyuncular = [
        # --- GALATASARAY ---
        {"id": 101, "ad": "Victor Osimhen", "takim": "Galatasaray", "mevki": "FV", "fiyat": 11.0, "form": "Mükemmel", "tahminiDakika": 90, "tahminiGol": 1, "tahminiAsist": 0, "golYememeIhtimali": False, "sakatlik": False},
        {"id": 102, "ad": "Barış Alper Yılmaz", "takim": "Galatasaray", "mevki": "OS", "fiyat": 9.0, "form": "Yüksek", "tahminiDakika": 90, "tahminiGol": 1, "tahminiAsist": 1, "golYememeIhtimali": False, "sakatlik": False},
        {"id": 103, "ad": "Gabriel Sara", "takim": "Galatasaray", "mevki": "OS", "fiyat": 8.5, "form": "Çok İyi", "tahminiDakika": 90, "tahminiGol": 0, "tahminiAsist": 1, "golYememeIhtimali": False, "sakatlik": False},
        {"id": 104, "ad": "Lucas Torreira", "takim": "Galatasaray", "mevki": "OS", "fiyat": 6.5, "form": "İyi", "tahminiDakika": 90, "tahminiGol": 0, "tahminiAsist": 0, "golYememeIhtimali": True, "sakatlik": False},
        {"id": 105, "ad": "Davinson Sánchez", "takim": "Galatasaray", "mevki": "DF", "fiyat": 7.0, "form": "Yüksek", "tahminiDakika": 90, "tahminiGol": 0, "tahminiAsist": 0, "golYememeIhtimali": True, "sakatlik": False},
        {"id": 106, "ad": "Fernando Muslera", "takim": "Galatasaray", "mevki": "KL", "fiyat": 6.5, "form": "İyi", "tahminiDakika": 90, "tahminiGol": 0, "tahminiAsist": 0, "golYememeIhtimali": True, "sakatlik": False},

        # --- FENERBAHÇE ---
        {"id": 201, "ad": "Romelu Lukaku", "takim": "Fenerbahçe", "mevki": "FV", "fiyat": 11.0, "form": "Mükemmel", "tahminiDakika": 90, "tahminiGol": 1, "tahminiAsist": 0, "golYememeIhtimali": False, "sakatlik": False},
        {"id": 202, "ad": "Youssef En-Nesyri", "takim": "Fenerbahçe", "mevki": "FV", "fiyat": 9.5, "form": "Yüksek", "tahminiDakika": 80, "tahminiGol": 1, "tahminiAsist": 0, "golYememeIhtimali": False, "sakatlik": False},
        {"id": 203, "ad": "Allan Saint-Maximin", "takim": "Fenerbahçe", "mevki": "OS", "fiyat": 9.0, "form": "Çok İyi", "tahminiDakika": 85, "tahminiGol": 1, "tahminiAsist": 1, "golYememeIhtimali": False, "sakatlik": False},
        {"id": 204, "ad": "Dušan Tadić", "takim": "Fenerbahçe", "mevki": "OS", "fiyat": 9.0, "form": "Mükemmel", "tahminiDakika": 90, "tahminiGol": 0, "tahminiAsist": 1, "golYememeIhtimali": False, "sakatlik": False},
        {"id": 205, "ad": "Sebastian Szymański", "takim": "Fenerbahçe", "mevki": "OS", "fiyat": 8.0, "form": "İyi", "tahminiDakika": 85, "tahminiGol": 1, "tahminiAsist": 0, "golYememeIhtimali": False, "sakatlik": False},
        {"id": 206, "ad": "Dominik Livaković", "takim": "Fenerbahçe", "mevki": "KL", "fiyat": 6.0, "form": "İyi", "tahminiDakika": 90, "tahminiGol": 0, "tahminiAsist": 0, "golYememeIhtimali": True, "sakatlik": False},

        # --- BEŞİKTAŞ ---
        {"id": 301, "ad": "Mason Greenwood", "takim": "Beşiktaş", "mevki": "OS", "fiyat": 10.0, "form": "Mükemmel", "tahminiDakika": 90, "tahminiGol": 1, "tahminiAsist": 1, "golYememeIhtimali": False, "sakatlik": False},
        {"id": 302, "ad": "Ciro Immobile", "takim": "Beşiktaş", "mevki": "FV", "fiyat": 10.0, "form": "Mükemmel", "tahminiDakika": 90, "tahminiGol": 1, "tahminiAsist": 0, "golYememeIhtimali": False, "sakatlik": False},
        {"id": 303, "ad": "Rafa Silva", "takim": "Beşiktaş", "mevki": "OS", "fiyat": 9.5, "form": "Mükemmel", "tahminiDakika": 90, "tahminiGol": 1, "tahminiAsist": 1, "golYememeIhtimali": False, "sakatlik": False},
        {"id": 304, "ad": "Gedson Fernandes", "takim": "Beşiktaş", "mevki": "OS", "fiyat": 8.0, "form": "Çok İyi", "tahminiDakika": 90, "tahminiGol": 0, "tahminiAsist": 1, "golYememeIhtimali": False, "sakatlik": False},
        {"id": 305, "ad": "Mert Günok", "takim": "Beşiktaş", "mevki": "KL", "fiyat": 5.5, "form": "İyi", "tahminiDakika": 90, "tahminiGol": 0, "tahminiAsist": 0, "golYememeIhtimali": True, "sakatlik": False},

        # --- TRABZONSPOR ---
        {"id": 401, "ad": "Simon Banza", "takim": "Trabzonspor", "mevki": "FV", "fiyat": 8.5, "form": "Yüksek", "tahminiDakika": 90, "tahminiGol": 1, "tahminiAsist": 0, "golYememeIhtimali": False, "sakatlik": False},
        {"id": 402, "ad": "Edin Višća", "takim": "Trabzonspor", "mevki": "OS", "fiyat": 7.5, "form": "İyi", "tahminiDakika": 85, "tahminiGol": 0, "tahminiAsist": 1, "golYememeIhtimali": False, "sakatlik": False},
        {"id": 403, "ad": "Uğurcan Çakır", "takim": "Trabzonspor", "mevki": "KL", "fiyat": 5.5, "form": "Çok İyi", "tahminiDakika": 90, "tahminiGol": 0, "tahminiAsist": 0, "golYememeIhtimali": True, "sakatlik": False},

        # --- BAŞAKŞEHİR ---
        {"id": 501, "ad": "Krzysztof Piątek", "takim": "Başakşehir", "mevki": "FV", "fiyat": 8.0, "form": "Yüksek", "tahminiDakika": 90, "tahminiGol": 1, "tahminiAsist": 0, "golYememeIhtimali": False, "sakatlik": False},
        {"id": 502, "ad": "Deniz Türüç", "takim": "Başakşehir", "mevki": "OS", "fiyat": 6.5, "form": "İyi", "tahminiDakika": 85, "tahminiGol": 0, "tahminiAsist": 1, "golYememeIhtimali": False, "sakatlik": False},

        # --- SİVASSPOR ---
        {"id": 601, "ad": "Rey Manaj", "takim": "Sivasspor", "mevki": "FV", "fiyat": 7.5, "form": "Çok İyi", "tahminiDakika": 90, "tahminiGol": 1, "tahminiAsist": 0, "golYememeIhtimali": False, "sakatlik": False},

        # --- KASIMPAŞA ---
        {"id": 701, "ad": "Nuno Da Costa", "takim": "Kasımpaşa", "mevki": "FV", "fiyat": 7.0, "form": "İyi", "tahminiDakika": 90, "tahminiGol": 1, "tahminiAsist": 0, "golYememeIhtimali": False, "sakatlik": False},

        # --- ALANYASPOR ---
        {"id": 801, "ad": "Sérgio Córdova", "takim": "Alanyaspor", "mevki": "FV", "fiyat": 6.5, "form": "Orta", "tahminiDakika": 80, "tahminiGol": 0, "tahminiAsist": 0, "golYememeIhtimali": False, "sakatlik": False},

        # --- CHRİSTİAN ATSU / HATAYSPOR ---
        {"id": 901, "ad": "Carlos Strandberg", "takim": "Hatayspor", "mevki": "FV", "fiyat": 6.0, "form": "İyi", "tahminiDakika": 90, "tahminiGol": 1, "tahminiAsist": 0, "golYememeIhtimali": False, "sakatlik": False},

        # --- ÇAYKUR RİZESPOR ---
        {"id": 1001, "ad": "Ali Sowe", "takim": "Çaykur Rizespor", "mevki": "FV", "fiyat": 6.5, "form": "İyi", "tahminiDakika": 85, "tahminiGol": 0, "tahminiAsist": 0, "golYememeIhtimali": False, "sakatlik": False},

        # --- ANTALYASPOR ---
        {"id": 1101, "ad": "Sam Larsson", "takim": "Antalyaspor", "mevki": "OS", "fiyat": 6.0, "form": "İyi", "tahminiDakika": 90, "tahminiGol": 0, "tahminiAsist": 1, "golYememeIhtimali": False, "sakatlik": False},

        # --- GAZİANTEP FK ---
        {"id": 1201, "ad": "Alexandru Maxim", "takim": "Gaziantep FK", "mevki": "OS", "fiyat": 6.0, "form": "İyi", "tahminiDakika": 85, "tahminiGol": 0, "tahminiAsist": 1, "golYememeIhtimali": False, "sakatlik": False},

        # --- KONYASPOR ---
        {"id": 1301, "ad": "Alassane Ndao", "takim": "Konyaspor", "mevki": "OS", "fiyat": 6.0, "form": "İyi", "tahminiDakika": 80, "tahminiGol": 0, "tahminiAsist": 0, "golYememeIhtimali": False, "sakatlik": False},

        # --- KAYSERİSPOR ---
        {"id": 1401, "ad": "Aylton Boa Morte", "takim": "Kayserispor", "mevki": "OS", "fiyat": 6.0, "form": "Orta", "tahminiDakika": 80, "tahminiGol": 0, "tahminiAsist": 0, "golYememeIhtimali": False, "sakatlik": False},

        # --- SAMSUNSPOR ---
        {"id": 1501, "ad": "Marius Mouandilmadji", "takim": "Samsunspor", "mevki": "FV", "fiyat": 6.5, "form": "Çok İyi", "tahminiDakika": 90, "tahminiGol": 1, "tahminiAsist": 0, "golYememeIhtimali": False, "sakatlik": False},

        # --- GÖZTEPE ---
        {"id": 1601, "ad": "Rômulo", "takim": "Göztepe", "mevki": "FV", "fiyat": 6.5, "form": "Çok İyi", "tahminiDakika": 90, "tahminiGol": 1, "tahminiAsist": 0, "golYememeIhtimali": False, "sakatlik": False},

        # --- BODRUM FK ---
        {"id": 1701, "ad": "George Pușcaș", "takim": "Bodrum FK", "mevki": "FV", "fiyat": 6.0, "form": "İyi", "tahminiDakika": 85, "tahminiGol": 0, "tahminiAsist": 0, "golYememeIhtimali": False, "sakatlik": False},

        # --- EYÜPSPOR ---
        {"id": 1801, "ad": "Mame Thiam", "takim": "Eyüpspor", "mevki": "FV", "fiyat": 7.0, "form": "Mükemmel", "tahminiDakika": 90, "tahminiGol": 1, "tahminiAsist": 0, "golYememeIhtimali": False, "sakatlik": False}
    ]

    with open('veriler.json', 'w', encoding='utf-8') as f:
        json.dump(oyuncular, f, ensure_ascii=False, indent=2)
    
    print(f"Süper Lig'deki {len(oyuncular)} oyuncu verisi kaydedildi!")

if __name__ == "__main__":
    guncel_verileri_cek()
