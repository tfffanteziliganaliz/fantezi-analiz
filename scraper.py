import json
import urllib.request
from bs4 import BeautifulSoup

def transfermarkt_canli_cek():
    print("Transfermarkt üzerinden takım kadroları çekiliyor...")

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }

    # Fotoğraftaki takım listesi ve Transfermarkt bağlantıları
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
                            "fiyat": 7.5,
                            "form": "İyi",
                            "tahminiDakika": 90,
                            "tahminiGol": 0,
                            "tahminiAsist": 0,
                            "golYememeIhtimali": False,
                            "sakatlik": False
                        })
                        
                        # Her takımdan ilk 10 ana oyuncuyu otomatik çeker
                        if count >= 10:
                            break

            print(f"✅ {takim['ad']}: {count} oyuncu otomatik çekildi.")

        except Exception as e:
            print(f"⚠️ {takim['ad']} çekilirken hata oluştu: {e}")

    with open('veriler.json', 'w', encoding='utf-8') as f:
        json.dump(oyuncular, f, ensure_ascii=False, indent=2)

    print(f"\n🚀 Toplam {len(oyuncular)} oyuncu otomatik veritabanına aktarıldı.")

if __name__ == "__main__":
    transfermarkt_canli_cek()
