import json
import urllib.request
from bs4 import BeautifulSoup

def transfermarkt_canli_cek():
    print("Transfermarkt üzerinden canlı Süper Lig verileri çekiliyor...")

    # Transfermarkt bot engellerini aşmak için tarayıcı kimliği
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }

    # Süper Lig takımlarının Transfermarkt linkleri
    takim_url_listesi = [
        {"ad": "Galatasaray", "url": "https://www.transfermarkt.com.tr/galatasaray-istanbul/kader/verein/141"},
        {"ad": "Fenerbahçe", "url": "https://www.transfermarkt.com.tr/fenerbahce-istanbul/kader/verein/36"},
        {"ad": "Beşiktaş", "url": "https://www.transfermarkt.com.tr/besiktas-istanbul/kader/verein/418"},
        {"ad": "Trabzonspor", "url": "https://www.transfermarkt.com.tr/trabzonspor/kader/verein/449"},
        {"ad": "Başakşehir", "url": "https://www.transfermarkt.com.tr/istanbul-basaksehir-fk/kader/verein/2841"},
        {"ad": "Eyüpspor", "url": "https://www.transfermarkt.com.tr/eyupspor/kader/verein/3257"},
        {"ad": "Sivasspor", "url": "https://www.transfermarkt.com.tr/sivasspor/kader/verein/2400"},
        {"ad": "Kasımpaşa", "url": "https://www.transfermarkt.com.tr/kasimpasa/kader/verein/10484"},
        {"ad": "Alanyaspor", "url": "https://www.transfermarkt.com.tr/alanyaspor/kader/verein/11282"},
        {"ad": "Antalyaspor", "url": "https://www.transfermarkt.com.tr/antalyaspor/kader/verein/1982"},
        {"ad": "Göztepe", "url": "https://www.transfermarkt.com.tr/goztepe/kader/verein/11252"},
        {"ad": "Samsunspor", "url": "https://www.transfermarkt.com.tr/samsunspor/kader/verein/152"},
        {"ad": "Rizespor", "url": "https://www.transfermarkt.com.tr/caykur-rizespor/kader/verein/132"},
        {"ad": "Gaziantep FK", "url": "https://www.transfermarkt.com.tr/gaziantep-fk/kader/verein/28164"},
        {"ad": "Konyaspor", "url": "https://www.transfermarkt.com.tr/konyaspor/kader/verein/2293"},
        {"ad": "Kayserispor", "url": "https://www.transfermarkt.com.tr/kayserispor/kader/verein/3205"},
        {"ad": "Hatayspor", "url": "https://www.transfermarkt.com.tr/hatayspor/kader/verein/7858"},
        {"ad": "Bodrum FK", "url": "https://www.transfermarkt.com.tr/bodrum-fk/kader/verein/32688"}
    ]

    oyuncular = []
    oyuncu_id = 100

    for takim in takim_url_listesi:
        try:
            req = urllib.request.Request(takim["url"], headers=headers)
            html = urllib.request.urlopen(req).read().decode('utf-8')
            soup = BeautifulSoup(html, 'html.parser')

            # Transfermarkt kadro tablosundaki oyuncu isimleri
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
                            "mevki": "OS", # Varsayılan fantezi mevkisi
                            "fiyat": 7.5,
                            "form": "İyi",
                            "tahminiDakika": 90,
                            "tahminiGol": 0,
                            "tahminiAsist": 0,
                            "golYememeIhtimali": False,
                            "sakatlik": False
                        })
                        
                        if count >= 8: # Her takımdan en popüler 8 ana oyuncuyu al
                            break

            print(f"✅ {takim['ad']}: {count} canlı oyuncu verisi çekildi.")

        except Exception as e:
            print(f"⚠️ {takim['ad']} verisi çekilirken hata: {e}")

    # JSON dosyasına yazma
    with open('veriler.json', 'w', encoding='utf-8') as f:
        json.dump(oyuncular, f, ensure_ascii=False, indent=2)

    print(f"\n🚀 Toplam {len(oyuncular)} oyuncu Transfermarkt'tan canlı çekilip veriler.json dosyasına kaydedildi.")

if __name__ == "__main__":
    transfermarkt_canli_cek()
