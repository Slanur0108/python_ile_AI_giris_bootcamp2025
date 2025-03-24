# python_ile_AI_giris_bootcamp2025

1. Proje Başlığı ve Kısa Açıklama: Bu proje, bir metro ağını grafik veri yapısını kullanarak modellemekte ve iki farklı algoritma ile en uygun rotaları belirlemektedir:
BFS (Breadth-First Search): En az aktarma ile rota bulma.
A Algoritması:* En hızlı rotayı bulma.

4. Kullanılan Teknolojiler ve Kütüphaneler

Projede kullanılan temel Python kütüphaneleri:
heapq: Öncelik kuyruğu yapısını kullanarak A* algoritmasını uygular.
collections.deque: BFS algoritması için kuyruk veri yapısını sağlar.

3. Algoritmaların Çalışma Mantığı

BFS Algoritması (en_az_aktarma_bul)
  Amaç: En az aktarma yapılan rotayı bulur.
  
  Çalışma Mantığı: 
  Başlangıç istasyonu kuyruğa eklenir,
  her istasyon için komşular ziyaret edilir, hedef istasyon bulunduğunda rota oluşturulur.

A* Algoritması (en_hizli_rota_bul)
  Amaç: En kısa sürede ulaşılan rotayı bulur.
  
  Çalışma Mantığı:
  Öncelik kuyruğu kullanarak istasyonlar en kısa sürede keşfedilir,
  toplam seyahat süresi hesaplanır, hedef istasyona ulaşıldığında en hızlı rota oluşturulur.

4. Örnek Kullanım ve Test Sonuçları

        if __name__ == "__main__":
        metro = MetroAgi()
        # İstasyonlar ekleme
        # Kırmızı Hat
        metro.istasyon_ekle("K1", "Kızılay", "Kırmızı Hat")
        metro.istasyon_ekle("K2", "Ulus", "Kırmızı Hat")
        metro.istasyon_ekle("K3", "Demetevler", "Kırmızı Hat")
        metro.istasyon_ekle("K4", "OSB", "Kırmızı Hat")
        
        # Mavi Hat
        metro.istasyon_ekle("M1", "AŞTİ", "Mavi Hat")
        metro.istasyon_ekle("M2", "Kızılay", "Mavi Hat")  # Aktarma noktası
        metro.istasyon_ekle("M3", "Sıhhiye", "Mavi Hat")
        metro.istasyon_ekle("M4", "Gar", "Mavi Hat")
        
        # Turuncu Hat
        metro.istasyon_ekle("T1", "Batıkent", "Turuncu Hat")
        metro.istasyon_ekle("T2", "Demetevler", "Turuncu Hat")  # Aktarma noktası
        metro.istasyon_ekle("T3", "Gar", "Turuncu Hat")  # Aktarma noktası
        metro.istasyon_ekle("T4", "Keçiören", "Turuncu Hat")
        
        # Bağlantılar ekleme
        metro.baglanti_ekle("K1", "K2", 4)
        metro.baglanti_ekle("K2", "K3", 6)
        metro.baglanti_ekle("K3", "K4", 8)
        metro.baglanti_ekle("M1", "M2", 5)
        metro.baglanti_ekle("M2", "M3", 3)
        metro.baglanti_ekle("M3", "M4", 4)
        metro.baglanti_ekle("T1", "T2", 7)
        metro.baglanti_ekle("T2", "T3", 9)
        metro.baglanti_ekle("T3", "T4", 5)
        metro.baglanti_ekle("K1", "M2", 2)
        metro.baglanti_ekle("K3", "T2", 3)
        metro.baglanti_ekle("M4", "T3", 2)
        
        # Test senaryoları
        print("\n=== Test Senaryoları ===")
        
        # Senaryo 1: AŞTİ'den OSB'ye
        print("\n1. AŞTİ'den OSB'ye:")
        rota = metro.en_az_aktarma_bul("M1", "K4")
        if rota:
            print("En az aktarmalı rota:", " -> ".join(i.ad for i in rota))
        
        sonuc = metro.en_hizli_rota_bul("M1", "K4")
        if sonuc:
            rota, sure = sonuc
            print(f"En hızlı rota ({sure} dakika):", " -> ".join(i.ad for i in rota))
        
        # Senaryo 2: Batıkent'ten Keçiören'e
        print("\n2. Batıkent'ten Keçiören'e:")
        rota = metro.en_az_aktarma_bul("T1", "T4")
        if rota:
            print("En az aktarmalı rota:", " -> ".join(i.ad for i in rota))
        
        sonuc = metro.en_hizli_rota_bul("T1", "T4")
        if sonuc:
            rota, sure = sonuc
            print(f"En hızlı rota ({sure} dakika):", " -> ".join(i.ad for i in rota))
        
        # Senaryo 3: Keçiören'den AŞTİ'ye
        print("\n3. Keçiören'den AŞTİ'ye:")
        rota = metro.en_az_aktarma_bul("T4", "M1")
        if rota:
            print("En az aktarmalı rota:", " -> ".join(i.ad for i in rota))
        
        sonuc = metro.en_hizli_rota_bul("T4", "M1")
        if sonuc:
            rota, sure = sonuc
            print(f"En hızlı rota ({sure} dakika):", " -> ".join(i.ad for i in rota))


5. Projeyi Geliştirme Fikirleri

Farklı algoritmaların eklenmesi (Dijkstra gibi).
Kullanıcıdan girdi alarak interaktif rota hesaplama
Gerçek zamanlı trafik verisi ile entegrasyon.









