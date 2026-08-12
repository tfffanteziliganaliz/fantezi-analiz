import json
import cloudscraper
from bs4 import BeautifulSoup

def tum_oyunculari_otomatik_cek():
    print("Transfermarkt canlı taranıyor (Cloudflare Bypass)...")

    # Cloudflare engelini aşan tarayıcı simülasyonu
    scraper = cloudscraper.create_scraper(
        browser={
            'browser': 'chrome',
            'platform': 'windows',
            'desktop': True
        }
    )

    takimlar = [
        {"ad": "Fenerbahçe", "url": "https://www.transfermarkt.com.tr/fenerbahce-istanbul/kader/verein/36"},
        {"ad": "Galatasaray", "url": "https://www.transfermarkt.com.tr/galatasaray-istanbul/kader/verein/141"},
        {"ad": "Beşiktaş", "url": "https://www.transfermarkt.com.tr/besiktas-istanbul/kader/verein/418"},
        {"ad": "Trabzonspor", "url": "https://www.transfermarkt.com.tr/trabzonspor/kader/verein/449"},
        {"ad": "Başakşehir", "url": "https://www.transfermarkt.com.tr/istanbul-basaksehir-fk/kader/verein/2841"},
        {"ad": "Göztepe", "url": "https://www.transfermarkt.com.tr/goztepe/kader/verein/11252"},
        {"ad": "Samsunspor", "url": "https://www.transfermarkt.com.tr/samsunspor/kader/verein/152"},
        {"ad": "Çorum FK", "url": "https://www.transfermarkt.com.tr/corum-fk/kader/verein/30680"},
        {"ad": "Ç. Rizespor", "url": "https://www.transfermarkt.com.tr/caykur-rizespor/kader/verein/132"},
        {"ad": "Alanyaspor", "url": "https://www.transfermarkt.com.tr/alanyaspor/kader/verein/11282"},
        {"ad": "Kasımpaşa", "url": "https://www.transfermarkt.com.tr/kasimpasa/kader/verein/10484"},
        {"ad": "Konyaspor", "url": "https://www.transfermarkt.com.tr/konyaspor/kader/verein/2293"},
        {"ad": "Amed SK", "url": "https://www.transfermarkt.com.tr/amed-sk/kader/verein/28168"},
        {"ad": "Gaziantep FK", "url": "https://www.transfermarkt.com.tr/gaziantep-fk/kader/verein/28164"},
        {"ad": "Kocaelispor", "url": "https://www.transfermarkt.com.tr/kocaelispor/kader/verein/3207"},
        {"ad": "Erzurumspor FK", "url": "https://www.transfermarkt.com.tr/erzurumspor-fk/kader/verein/42491"},
        {"ad": "Gençlerbirliği", "url": "https://www.transfermarkt.com.tr/genclerbirligi-ankara/kader/verein/820"},
        {"ad": "Eyüpspor", "url": "https://www.transfermarkt.com.tr/eyupspor/kader/verein/3257"}
    ]

    oyuncular = []
    global_id = 1000

    for takim in takimlar:
        try:
            res = scraper.get(takim["url"], timeout=12)
            if res.status_code == 200:
                soup = BeautifulSoup(res.text, 'html.parser')
                links = soup.select('td.hauptlink a[href*="/profil/spieler/"]')
                eklenenler = set()
                count = 0

                for link in links:
                    isim = link.text.strip()
                    if isim and isim not in eklenenler and len(isim) > 2:
                        eklenenler.add(isim)
                        global_id += 1
                        count += 1

                        # Mevki dağılımı (KL, DEF, OS, FV)
                        mevki = "KL" if count == 1 else ("DEF" if count <= 4 else ("OS" if count <= 8 else "FV"))

                        oyuncular.append({
                            "id": global_id,
                            "ad": isim,
                            "takim": takim["ad"],
                            "mevki": mevki,
                            "fiyat": 7.5,
                            "form": "İyi",
                            "tahminiDakika": 90,
                            "tahminiGol": 1 if mevki == "FV" else 0,
                            "tahminiAsist": 1 if mevki in ["OS", "FV"] else 0,
                            "golYememeIhtimali": True if mevki in ["KL", "DEF"] else False,
                            "sakatlik": False
                        })

                print(f"✅ {takim['ad']}: {count} oyuncu çekildi.")
            else:
                print(f"⚠️ {takim['ad']} erişim engeli (HTTP {res.status_code})")

        except Exception as e:
            print(f"❌ {takim['ad']} hatası: {e}")

    # EĞER SUNUCU ENGELLENİRSE SİTE BOŞ KALMASIN DİYE EMNİYET SİSTEMİ
    if len(oyuncular) == 0:
        print("⚠️ Canlı bağlantı kısıtlandı, emniyet sistemi devreye giriyor...")
        for takim in takimlar:
            for i in range(1, 11):
                global_id += 1
                mevki = "KL" if i == 1 else ("DEF" if i <= 4 else ("OS" if i <= 8 else "FV"))
                oyuncular.append({
                    "id": global_id,
                    "ad": f"{takim['ad']} Oyuncu {i}",
                    "takim": takim["ad"],
                    "mevki": mevki,
                    "fiyat": 7.0,
                    "form": "İyi",
                    "tahminiDakika": 90,
                    "tahminiGol": 0,
                    "tahminiAsist": 0,
                    "golYememeIhtimali": False,
                    "sakatlik": False
                })

    with open('veriler.json', 'w', encoding='utf-8') as f:
        json.dump(oyuncular, f, ensure_ascii=False, indent=2)

    print(f"\n🚀 Toplam {len(oyuncular)} oyuncu 'veriler.json'a kaydedildi.")

if __name__ == "__main__":
    tum_oyunculari_otomatik_cek()
