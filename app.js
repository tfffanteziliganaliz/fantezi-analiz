let tumOyuncular = [];

// TFF Fantezi Lig Puanlama Motoru
function puanHesapla(oyuncu) {
    let puan = 0;

    // Süre Puanı
    if (oyuncu.tahminiDakika >= 60) puan += 2;
    else if (oyuncu.tahminiDakika > 0) puan += 1;

    // Gol Puanları (Mevkiye Göre)
    if (oyuncu.mevki === 'KL') puan += oyuncu.tahminiGol * 10;
    if (oyuncu.mevki === 'DF') puan += oyuncu.tahminiGol * 6;
    if (oyuncu.mevki === 'OS') puan += oyuncu.tahminiGol * 5;
    if (oyuncu.mevki === 'FV') puan += oyuncu.tahminiGol * 4;

    // Asist Puanı
    puan += oyuncu.tahminiAsist * 3;

    // Clean Sheet (Gol Yememe)
    if (oyuncu.golYememeIhtimali && oyuncu.tahminiDakika >= 60) {
        if (oyuncu.mevki === 'KL' || oyuncu.mevki === 'DF') puan += 4;
        if (oyuncu.mevki === 'OS') puan += 1;
    }

    return puan;
}

// Verileri Yükle
async function verileriYukle() {
    const res = await fetch('veriler.json');
    tumOyuncular = await res.json();
    ekraniGuncelle(tumOyuncular);
}

function ekraniGuncelle(liste) {
    const oyuncuKapsayici = document.getElementById('oyuncu-listesi');
    const kaptanKapsayici = document.getElementById('kaptan-listesi');
    
    oyuncuKapsayici.innerHTML = '';
    kaptanKapsayici.innerHTML = '';

    // Puan hesaplayıp sıralayalım
    const IslenmisData = liste.map(o => ({...o, tahminiPuan: puanHesapla(o)}))
                              .sort((a,b) => b.tahminiPuan - a.tahminiPuan);

    // Kaptan Adayları (En yüksek puanlı ilk 2 kişi)
    IslenmisData.slice(0,2).forEach(o => {
        kaptanKapsayici.innerHTML += `
            <div class="bg-slate-800 border border-amber-500/30 p-3 rounded-2xl relative overflow-hidden">
                <div class="text-xs text-amber-400 font-bold mb-1">${o.takim}</div>
                <div class="font-bold text-sm text-white">${o.ad}</div>
                <div class="text-xs text-slate-400 mb-2">Mevki: ${o.mevki} | ₺${o.fiyat}M</div>
                <div class="text-right text-emerald-400 font-black text-lg">x2 ile ${o.tahminiPuan * 2} Puan</div>
            </div>
        `;
    });

    // Tüm Oyuncular
    IslenmisData.forEach(o => {
        oyuncuKapsayici.innerHTML += `
            <div class="bg-slate-800 p-4 rounded-2xl flex justify-between items-center border border-slate-700/50">
                <div>
                    <div class="flex items-center gap-2">
                        <span class="font-bold text-white text-base">${o.ad}</span>
                        <span class="text-xs bg-slate-700 px-2 py-0.5 rounded text-slate-300">${o.mevki}</span>
                    </div>
                    <div class="text-xs text-slate-400 mt-1">
                        ${o.takim} • ₺${o.fiyat}M • Form: <span class="text-emerald-400">${o.form}</span>
                    </div>
                </div>
                <div class="text-right">
                    <div class="text-xs text-slate-400">Beklenen</div>
                    <div class="text-xl font-black text-emerald-400">${o.tahminiPuan} <span class="text-xs">Puan</span></div>
                </div>
            </div>
        `;
    });
}

function filtrele(mevki) {
    if (mevki === 'Hepsi') ekraniGuncelle(tumOyuncular);
    else ekraniGuncelle(tumOyuncular.filter(o => o.mevki === mevki));
}

verileriYukle();
