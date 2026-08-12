import json
import requests
from bs4 import BeautifulSoup

def tum_oyunculari_cek():
    print("Transfermarkt canlı kadroları taranıyor...")

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
    }

    # Görselindeki 18 Takım Listesi
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
    oyuncu_id = 1000
    session = requests.Session()

    for takim in takimlar:
        try:
            res = session.get(takim["url"], headers=headers, timeout=8)
            soup = BeautifulSoup(res.content, 'html.parser')
            
            # Transfermarkt oyuncu linklerini otomatik yakala
            links = soup.select('td.hauptlink a[href*="/profil/spieler/"]')
            eklenenler = set()
            count = 0

            for link in links:
                isim = link.text.strip()
                if isim and isim not in eklenenler and len(isim) > 2:
                    eklenenler.add(isim)
                    oyuncu_id += 1
                    count += 1
                    
                    mevki = "FV" if count % 3 == 0 else ("DEF" if count % 2 == 0 else "OS")
                    
                    oyuncular.append({
                        "id": oyuncu_id,
                        "ad": isim,
                        "takim": takim["ad"],
                        "mevki": mevki,
                        "fiyat": 7.5,
                        "form": "İyi",
                        "tahminiDakika": 90,
                        "tahminiGol": 0,
                        "tahminiAsist": 0,
                        "golYememeIhtimali": False,
                        "sakatlik": False
                    })
            print(f"✅ {takim['ad']}: {count} oyuncu otomatik çekildi.")
        except Exception as e:
            print(f"⚠️ {takim['ad']} hata: {e}")

    with open('veriler.json', 'w', encoding='utf-8') as f:
        json.dump(oyuncular, f, ensure_ascii=False, indent=2)

    print(f"🚀 Toplam {len(oyuncular)} oyuncu 'veriler.json' dosyasına işlendi.")

if __name__ == "__main__":
    tum_oyunculari_cek()
