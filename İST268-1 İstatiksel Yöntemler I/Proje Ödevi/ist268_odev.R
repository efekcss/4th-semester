# İST268 - İSTATİSTİKSEL YÖNTEMLER I DÖNEM ÖDEVİ #

# 1. İki Örneklem Analizleri

# Kitle Ortalaması (mu) mu_1 - mu_2 icin Basit ist.ler, hipotez testi, guven aralığı

vites <- factor(mtcars$am , levels = c(0,1) , labels = c("automatic","manuel")) 
# labellamayı yaptık yani 0 = automatic , 1 = manuel
print(vites)

yakit <- (mtcars$mpg)
print(yakit)

tapply(yakit, vites, mean) # otomatik ve manuel viteslerin örneklem ortalamaları

tapply(yakit, vites, var) # otomatik ve manuel vitesleri örneklem varyansları

tapply(yakit, vites, length) # otomatik ve manuel viteslere göre örneklem miktarı/n değerleri

#Basit istatistikleri elde ettik şimdi hipotez testine geçebiliriz. iki yanlı hipotez testi incelenecektir
# Ho : mu1 - mu2 = 0
# Hs : mu1 - mu2 =/ 0
# Kitle varyansları bilinmiyor
#n1'de n2'de 30 dan küçükler bu yüzden MLT'de yapamıyoruz t-testi yapmalıyız homojenliğe göre hangi t-testi olduğuna bakacağız
#iki örneklem varyans testi yapacağız şimdi (sigma_1 / sigma_2)

