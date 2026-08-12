import json
import urllib.request
from bs4 import BeautifulSoup

def verileri_guncelle():
    print("Süper Lig kadroları Transfermarkt üzerinden çekiliyor...")

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }

    takimlar = [
        {"ad": "Fenerbahçe", "url": "https://www.transfermarkt.com.tr/fenerbahce-istanbul/kader/verein/36"},
        {"ad": "Galatasaray", "url": "https://www.transfermarkt.com.tr/galatasaray-istanbul/kader/verein/141"},
        {"ad": "Beşiktaş", "url": "https://www.transfermarkt.com.tr/besiktas-istanbul/kader/verein/418"},
        {"ad": "Trabzonspor", "url": "https://www.transfermarkt.com.tr/trabzonspor/kader/verein/449"},
        {"ad": "Başakşehir", "url": "https://www.transfermarkt.com.tr/istanbul-basaksehir-fk/kader/verein/2841"},
        {"ad": "Göztepe", "url": "https://www.transfermarkt.com.tr/goztepe/kader/verein/11252"},
        {"ad": "Samsunspor", "url": "https://www.transfermarkt.com.tr/samsunspor/kader/verein/152"},
        {"ad": "Eyüpspor", "url": "https://www.transfermarkt.com.tr/eyupspor/kader/verein/3257"}
    ]

    oyuncular = []
    oyuncu_id = 100

    for takim in takimlar:
        try:
            req = urllib.request.Request(takim["url"], headers=headers)
            html = urllib.request.urlopen(req).read().decode('utf-8')
            soup = BeautifulSoup(html, 'html.parser')

            oyuncu_kutulari = soup.find_all("td", class_="hauptlink")
            eklenenler = set()
            count = 0

            for kutu in oyuncu_kutulari:
                a_tag = kutu.find("a")
                if a_tag and a_tag.text:
                    isim = a_tag.text.strip()
                    if isim not in eklenenler and len(isim) > 2:
                        eklenenler.add(isim)
                        oyuncu_id += 1
                        count += 1
                        
                        oyuncular.append({
                            "id": oyuncu_id,
                            "ad": isim,
                            "takim": takim["ad"],
                            "mevki": "OS",
                            "fiyat": 8.0,
                            "form": "İyi",
                            "tahminiDakika": 90,
                            "tahminiGol": 0,
                            "tahminiAsist": 0,
                            "golYememeIhtimali": False,
                            "sakatlik": False
                        })
                        if count >= 8:
                            break
        except Exception as e:
            print(f"{takim['ad']} hatası: {e}")

    # EĞER TRANSFERMARKT BOTU ENGELLERSE SAYFA BOŞ KALMASIN DİYE YEDEK LİSTE:
    if len(oyuncular) == 0:
        print("Transfermarkt bağlantısı engellendi, yedek güncel liste yükleniyor...")
        oyuncular = [
            {"id": 1, "ad": "Youssef En-Nesyri", "takim": "Fenerbahçe", "mevki": "FV", "fiyat": 10.0, "form": "Yüksek", "tahminiDakika": 90, "tahminiGol": 1, "tahminiAsist": 0, "golYememeIhtimali": False, "sakatlik": False},
            {"id": 2, "ad": "Fred", "takim": "Fenerbahçe", "mevki": "OS", "fiyat": 8.0, "form": "Çok İyi", "tahminiDakika": 90, "tahminiGol": 0, "tahminiAsist": 1, "golYememeIhtimali": False, "sakatlik": False},
            {"id": 3, "ad": "Victor Osimhen", "takim": "Galatasaray", "mevki": "FV", "fiyat": 11.0, "form": "Mükemmel", "tahminiDakika": 90, "tahminiGol": 1, "tahminiAsist": 0, "golYememeIhtimali": False, "sakatlik": False},
            {"id": 4, "ad": "Barış Alper Yılmaz", "takim": "Galatasaray", "mevki": "OS", "fiyat": 9.0, "form": "Yüksek", "tahminiDakika": 90, "tahminiGol": 1, "tahminiAsist": 1, "golYememeIhtimali": False, "sakatlik": False},
            {"id": 5, "ad": "Ciro Immobile", "takim": "Beşiktaş", "mevki": "FV", "fiyat": 10.0, "form": "Mükemmel", "tahminiDakika": 90, "tahminiGol": 1, "tahminiAsist": 0, "golYememeIhtimali": False, "sakatlik": False},
            {"id": 6, "ad": "Rafa Silva", "takim": "Beşiktaş", "mevki": "OS", "fiyat": 9.5, "form": "Mükemmel", "tahminiDakika": 90, "tahminiGol": 1, "tahminiAsist": 1, "golYememeIhtimali": False, "sakatlik": False},
            {"id": 7, "ad": "Simon Banza", "takim": "Trabzonspor", "mevki": "FV", "fiyat": 8.5, "form": "Yüksek", "tahminiDakika": 90, "tahminiGol": 1, "tahminiAsist": 0, "golYememeIhtimali": False, "sakatlik": False}
        ]

    with open('veriler.json', 'w', encoding='utf-8') as f:
        json.dump(oyuncular, f, ensure_ascii=False, indent=2)

    print("Veriler başarıyla yazıldı.")

if __name__ == "__main__":
    verileri_guncelle()
