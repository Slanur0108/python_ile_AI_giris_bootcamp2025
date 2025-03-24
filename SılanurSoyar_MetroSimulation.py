from collections import defaultdict, deque
import heapq
from typing import Dict, List, Tuple, Optional

# Istasyon (Durak) sınıfı tanımlanıyor
class Istasyon:
    def __init__(self, idx: str, ad: str, hat: str):
        self.idx = idx  # İstasyonun benzersiz kimliği
        self.ad = ad  # İstasyonun adı
        self.hat = hat  # İstasyonun ait olduğu metro hattı
        self.komsular: List[Tuple['Istasyon', int]] = []  # (Komşu istasyon, yolculuk süresi) bilgilerini saklayan liste

    def komsu_ekle(self, istasyon: 'Istasyon', sure: int):
        """İstasyona bir komşu istasyon ekler ve süreyi belirler."""
        self.komsular.append((istasyon, sure))

# Metro ağı sınıfı tanımlanıyor
class MetroAgi:
    def __init__(self):
        self.istasyonlar: Dict[str, Istasyon] = {}  # Tüm istasyonları saklayan sözlük
        self.hatlar: Dict[str, List[Istasyon]] = defaultdict(list)  # Hatlara göre istasyonları saklayan sözlük

    def istasyon_ekle(self, idx: str, ad: str, hat: str) -> None:
        """Yeni bir istasyon ekler."""
        if idx not in self.istasyonlar:  # Eğer istasyon zaten yoksa ekle
            istasyon = Istasyon(idx, ad, hat)
            self.istasyonlar[idx] = istasyon
            self.hatlar[hat].append(istasyon)  # İstasyonu ilgili hatta ekle

    def baglanti_ekle(self, istasyon1_id: str, istasyon2_id: str, sure: int) -> None:
        """İki istasyon arasında bağlantı ekler."""
        istasyon1 = self.istasyonlar[istasyon1_id]
        istasyon2 = self.istasyonlar[istasyon2_id]
        istasyon1.komsu_ekle(istasyon2, sure)
        istasyon2.komsu_ekle(istasyon1, sure)  # İki yönlü bağlantı ekleniyor
    
    def en_az_aktarma_bul(self, baslangic_id: str, hedef_id: str) -> Optional[List[Istasyon]]:
        """BFS algoritması kullanarak en az aktarmalı rotayı bulur."""
        if baslangic_id not in self.istasyonlar or hedef_id not in self.istasyonlar:
            return None  # Başlangıç veya hedef istasyon yoksa None döndür
        
        baslangic = self.istasyonlar[baslangic_id]
        hedef = self.istasyonlar[hedef_id]
        kuyruk = deque([(baslangic, [baslangic])])  # BFS kuyruğu, (istasyon, ziyaret edilen istasyonlar listesi)
        ziyaret_edildi = set()
        
        while kuyruk:
            mevcut, rota = kuyruk.popleft()  # Kuyruktan sıradaki istasyonu al
            
            if mevcut == hedef:
                return rota  # Hedef istasyona ulaşıldıysa rotayı döndür
            
            ziyaret_edildi.add(mevcut)  # İstasyonu ziyaret edildi olarak işaretle
            
            for komsu, _ in mevcut.komsular:
                if komsu not in ziyaret_edildi:
                    kuyruk.append((komsu, rota + [komsu]))  # Yeni rotayı kuyruğa ekle
        
        return None  # Rota bulunamazsa None döndür

    def en_hizli_rota_bul(self, baslangic_id: str, hedef_id: str) -> Optional[Tuple[List[Istasyon], int]]:
        """Dijkstra algoritması kullanarak en hızlı rotayı bulur."""
        if baslangic_id not in self.istasyonlar or hedef_id not in self.istasyonlar:
            return None  # Başlangıç veya hedef istasyon yoksa None döndür
        
        baslangic = self.istasyonlar[baslangic_id]
        hedef = self.istasyonlar[hedef_id]
        
        pq = [(0, baslangic, [baslangic])]  # Öncelik kuyruğu (toplam süre, mevcut istasyon, rota)
        ziyaret_edildi = {}
        
        while pq:
            sure, mevcut, rota = heapq.heappop(pq)  # En düşük süreli yolu al
            
            if mevcut == hedef:
                return rota, sure  # Hedefe ulaşıldıysa rotayı ve süreyi döndür
            
            if mevcut in ziyaret_edildi and ziyaret_edildi[mevcut] <= sure:
                continue  # Daha kısa bir yol varsa atla
            
            ziyaret_edildi[mevcut] = sure  # Şu anki istasyonu ziyaret edildi olarak işaretle
            
            for komsu, ek_sure in mevcut.komsular:
                heapq.heappush(pq, (sure + ek_sure, komsu, rota + [komsu]))  # Yeni rotayı kuyruğa ekle
        
        return None  # Rota bulunamazsa None döndür

