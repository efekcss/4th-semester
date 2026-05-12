# İST268 - İSTATİSTİKSEL YÖNTEMLER I DÖNEM ÖDEVİ #

# 1. İki Örneklem Analizleri

# Kitle Ortalaması (mu) mu_1 - mu_2 icin Basit ist.ler, hipotez testi, guven aralığı

vites <- factor(mtcars$am , levels = c(0,1) , labels = c("automatic","manuel")) 
yakit <- mtcars$mpg

tapply(yakit, vites, mean)

tapply(yakit, vites, var)

tapply(yakit, vites, length)

#Basit istatistikleri elde ettik şimdi hipotez testine geçebiliriz. iki yanlı hipotez testi incelenecektir
# Ho : mu1 - mu2 = 0
# Hs : mu1 - mu2 =/ 0
# Kitle varyansları bilinmiyor
#n1'de n2'de 30 dan küçükler bu yüzden MLT'de yapamıyoruz t-testi yapmalıyız homojenliğe göre hangi t-testi olduğuna bakacağız
#iki örneklem varyans testi yapacağız şimdi (sigma_1 / sigma_2)

# 1.2.Varyansların Homojenliği Testi (F-Test)
var.test(yakit ~ vites, data = mtcars)

# Sp^2 li t-testi kullanacağız (varyanslar homojenmiş)
t.test(mpg ~ am, data = mtcars, var.equal = TRUE, conf.level = 0.95)

# 1.3. İki kitle oranı analiiz
# Sadece Yetişkinlerin hayatta kalma tablosunu getirir
Titanic[, , "Adult", ]

prop.test(x = c(316,338), n = c(425,1667))

# 1.4 Bağımlı örneklem analizi

tapply(sleep$extra, sleep$group, mean)
tapply(sleep$extra, sleep$group, var)
tapply(sleep$extra, sleep$group, length)

# 1. ve 2. ilacı alanların verilerini (ilk 10 ve son 10 satırı) ayırıyoruz
ilac1 <- sleep$extra[sleep$group == 1]
ilac2 <- sleep$extra[sleep$group == 2]


t.test(ilac1, ilac2, paired = TRUE)

### 2. Kİ-KARE ÇÖZÜMLEMESİ 

## 2.1 Uyum iyiliği testi

# ortalma ve standart sapma hesaplanması
ort_mpg <- mean(mtcars$mpg)
ss_mpg <- sd(mtcars$mpg)

# veriyi sınıflra ayırma/Gözlenen Frekanslar
frekans_tablosu <- hist(mtcars$mpg, plot = TRUE)

# sonuçlar
ort_mpg
ss_mpg
frekans_tablosu$breaks  # Sınıfların başlangıç ve bitiş sınırları
frekans_tablosu$counts  # Her sınıfa düşen araç sayısı (Gözlenen Frekanslar= f_i)

# Her sınıfın teorik normal dağılım olasılığını (P_i) hesaplama
# (Üst sınır olasılığı - Alt sınır olasılığı)
p_i <- pnorm(frekans_tablosu$breaks[-1], mean = ort_mpg, sd = ss_mpg) - pnorm(frekans_tablosu$breaks[-length(frekans_tablosu$breaks)], mean = ort_mpg, sd = ss_mpg)

# Beklenen Frekansları (e_i = N * P_i) hesaplama
e_i <- 32 * p_i
e_i

f_i_yeni <- c(6, 12, 8, 6)
# 1.sınıfı, 2. sınıfı, 3'ü aynen al, 4. ve 5. sınıfı topla
e_i_yeni <- c(4.87,9.44,9.55,6.43)
round(e_i_yeni,2)

# Formül: Toplam( (f_i - e_i)^2 / e_i )
ki_kare_hesap <- sum((f_i_yeni - e_i_yeni)^2 / e_i_yeni)
ki_kare_hesap

tablo_degeri <- qchisq(0.95, df = 1)
tablo_degeri


# 2.2 Gruplar Arası Fark 
# 1. Çapraz Tablonun Oluşturulması (Satır: Gruplar, Sütun: Cevap Değişkeni)
tablo_fark <- table(mtcars$cyl, mtcars$am)
print("Gözlenen Frekanslar (f_ij):")
tablo_fark

# 2. Gruplar Arası Fark Kontrolü (Ki-Kare Testi)
test_sonucu <- chisq.test(tablo_fark)
test_sonucu

# 3. Beklenen Frekansların Kontrolü (e_ij >= 5 kuralı için)
print("Beklenen Frekanslar (e_ij):")
test_sonucu$expected

# satırların birleştirilmesi
yeni_tablo_fark <- rbind(tablo_fark[1,] + tablo_fark[2,], tablo_fark[3,])
rownames(yeni_tablo_fark) <- c("4_ve_6_Silindir", "8_Silindir")
yeni_tablo_fark

# ki-kare testi
yeni_test <- chisq.test(yeni_tablo_fark)
yeni_test

#yeni beklenen frekanslar
print("Yeni Beklenen Frekanslar:")
yeni_test$expected


# 2.3 İlişki/Bağımsızlık Kontrolü
# Çapraz Tablonun Oluşturulması (Satır: Motor Şekli, Sütun: Vites Türü)
tablo_iliski <- table(mtcars$vs, mtcars$am)
print("Gözlenen Frekanslar Tablosu:")
tablo_iliski

# bağımsızlık Testi Ki-Kare Testi
test_iliski <- chisq.test(tablo_iliski)
test_iliski

# Phi Hesaplanması
# Formül: karekök( Ki-Kare / n )
ki_kare_degeri <- test_iliski$statistic
n <- sum(tablo_iliski)
phi_katsayisi <- sqrt(ki_kare_degeri / n)
phi_katsayisi
