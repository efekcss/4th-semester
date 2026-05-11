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
