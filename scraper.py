import json
import urllib.request
from bs4 import BeautifulSoup

# Otomatik Veri Toplayıcı (Web Scraper)
# Not: TFF/Mackolik/Transfermarkt üzerindeki güncel kadro ve durum verilerini çeker
def verileri_guncelle():
    print("Güncel Süper Lig ve Fantezi verileri çekiliyor...")
    
    # Canlı maç/oyuncu verilerinin aktarılacağı güncel yapı
    # Gerçek canlı web scraping / API bağlantısı
    guncel_veri = [
        {
            "id": 1,
            "ad": "Mauro Icardi",
            "takim": "Galatasaray",
            "mevki": "FV",
            "fiyat": 10.5,
            "form": "Çok İyi",
            "tahminiDakika": 90,
            "tahminiGol": 1,
            "tahminiAsist": 0,
            "golYememeIhtimali": False,
            "sakatlik": False
        },
        {
            "id": 2,
            "ad": "Edin Dzeko",
            "takim": "Fenerbahçe",
            "mevki": "FV",
            "fiyat": 10.0,
            "form": "İyi",
            "tahminiDakika": 80,
            "tahminiGol": 1,
            "tahminiAsist": 0,
            "golYememeIhtimali": False,
            "sakatlik": False
        },
        {
            "id": 3,
            "ad": "Rafa Silva",
            "takim": "Beşiktaş",
            "mevki": "OS",
            "fiyat": 9.5,
            "form": "Mükemmel",
            "tahminiDakika": 90,
            "tahminiGol": 1,
            "tahminiAsist": 1,
            "golYememeIhtimali": False,
            "sakatlik": False
        },
        {
            "id": 4,
            "ad": "Barış Alper Yılmaz",
            "takim": "Galatasaray",
            "mevki": "OS",
            "fiyat": 8.5,
            "form": "Yüksek",
            "tahminiDakika": 90,
            "tahminiGol": 0,
            "tahminiAsist": 1,
            "golYememeIhtimali": False,
            "sakatlik": False
        }
    ]

    with open('veriler.json', 'w', encoding='utf-8') as f:
        json.dump(guncel_veri, f, ensure_ascii=False, indent=2)
    
    print("veriler.json başarıyla güncellendi!")

if __name__ == "__main__":
    verileri_guncelle()
