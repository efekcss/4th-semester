# İST268-01 İstatistiksel Yöntemler I Dönem Ödevi

### Dersin Sorumluları: 
Prof. Dr. Sevil BACANLI
Doç. Dr. Özge KARADAĞ ATAŞ
Arş. Gör. Dr. Ceren ÜNAL AKDENİZ

### Ödev Konusu: 
İki Örneklem Hipotez Testleri (Hipotez Testleri, Güven Aralığı, Bağımlı İki Örneklem İncelenmesi) ve Ki-Kare Çözümlemeleri (Uyum İyiliği Testi, Gruplar Arası Fark ve Bağımsızlık Kontrolü)

### Hazırlayanlar: 
Hasan Efe Kocasu
2240329066

**Giriş**
İST268 İstatistiksel Yöntemler I dersi dönem proje ödevi kapsamında 2 ve 2’den fazla değişken barındıran veri setleri iki başlık altında incelenecek, birinci kısımda: iki örneklem hipotez testleri, güven aralıkları ve verilerin basit istatistikleri incelenecektir. İkinci kısımda ise: Ki-kare çözümlemesinde verilen; uyum iyiliği testi, gruplar arası fark ve bağımsızlık kontrolüne ilişkin çözümlemeler yapılacaktır.

## Kullanılacak Veri Setleri:
Bu analiz için R’da default gelen “mtcars” veri seti üzerinde çalışılacaktır. Bağımlı 2 örneklem analizi içinse yine R’da default gelen “sleep” veri seti üzerinden analiz yapılacaktır. İki örneklem oran testi içinse yine R’da default gelen “Titanic” veri seti üzerinde analiz yapılacaktır.

   **“mtcars” Veri Seti:**
    “mtcars" veri seti 1972-1974 model 32 araba için 11 değişkenli bir veri barındırıyor. Bu veri seti Motor Trend US dergisinde 1974 yılında yayımlanmıştır. 
(Henderson HV, Velleman PF (1981). “Building Multiple Regression Models Interactively.” Biometrics, 37(2), 391–411.), (https://www.jstor.org/stable/2530428?origin=crossref&seq=5)
    “mtcars” veri seti içerisinde iki örneklem analizleri incelenirken arabalar “transmission” yani vites sistemlerine göre  iki gruba ayırarak incelenmiştir. (0 = automatic, 1 = manuel) Gruplar “mpg” değişkenine bakılarak incelenecekler, mpg değişkeni araçların mil başına tükettikleri galon miktarını içermektedir.

   **“Titanic” Veri Seti:**
“Titanic” veri seti Titanic gemisindeki her bir yolcunun sınıfı, cinsiyeti, yaşı ve hayatta kalma durumunu kaydeden bir veri seti sunmaktadır. Veri 4 kategori altında yapılandırılmıştır. 
Bu veri, aslen İngiliz Ticaret Bakanlığı tarafından toplanmış ve şu eserde yeniden basılmış verilere dayanmaktadır: 
(British Government (1990). Report on the Loss of the SS Titanic. Allan Sutton Publishing, Gloucester, UK. ISBN 978-0862997236.)
Bu veri seti üzerine R’da yapılan araştırmanın kaynağı ise: 
Dawson RJM (1995). “The “Unusual Episode” Data Revisited.” Journal of Statistics Education, 3(3). (https://www.tandfonline.com/doi/full/10.1080/10691898.1995.11910499)

   **“sleep” Veri Seti:**
“sleep” veri seti 2 grup öğrenci denek arasında yapılan 2 ilacın uyku sürelerine etkisi üzerine bilgi içermektedir. 3 değişken barındırmaktadır ve bunlar sırasıyla “d”, “group”, “ID”. “d” ilaç verildikten sonra öğrencilerde meydana gelen uyku sürelerindeki artış miktarıdır yani farkıdır (sonra – önce). “group” 2 gruba ayrılan öğrenci gruplarını temsil eder ve gruplar “1” ve “2” değerleri ile ayrıştırılmıştır. “ID” değişkeni ise verilerin, öğrencilerin sırasıyla numaralandırılarak eşlenmesi sağlanmıştır.

# 1. İki Örneklem Analizleri  
Bu başlık altında veri setleri üzerinde iki örneklem; hipotez testlerini, güven aralıklarını ve verilerin basit istatistikleri elde edilerek yorumlanacaktır.
### Kitle Ortalaması Analizi
Bu başlık altında kitle ortalaması (µ)’na dair hipotez testi, güven aralığı ve verilerin basit istatistikleri analiz edilecektir.  Bu analiz için daha önceden tanıtımı yapılan “mtcars” verisi kullanılacaktır.             


