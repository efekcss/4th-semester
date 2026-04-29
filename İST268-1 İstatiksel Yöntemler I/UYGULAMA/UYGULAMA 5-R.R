##############UYGULAMA 5##############
############GENEL TEKRAR-R############

###Soru1
once <- c(120,124,130,118,140,128,140,135,126,130,126,127)  # C6nce verileri
sonra <- c(128,131,131,127,132,125,141,137,118,132,129,135)     # sonra verileri

fark<-once-sonra; fark


# Guven Araligi hesaplama, bagimli orneklem
t_result <- t.test(once, sonra, paired=TRUE, conf.level = 0.95, mu=)
t_result
print(t_result$conf.int)  # %95 guven araligi
t_result2 <- t.test(once, sonra, paired=TRUE, conf.level = 0.95, mu=, alternative = "greater")
t_result2


#Soru 2
kiz<- c(8.09,	8.08,	8.40,	7.58,	7.05,	10.15, 10.88,	8.11,	7.48,	7.90,	7.53,	6.13,	7.48)
erkek<-c(9.68, 9.97,	9.69,	11.85,	11.51,	12.79,	9.21,	9.19,	8.79)

# Orneklem istatistikleri
n1 <- length(kiz)  # Birinci grup orneklem buyuklukleri
n2 <- length(erkek)  # ikinci grup orneklem buyuklukleri

mean1 <- mean(kiz) # Birinci grup ortalamasi
mean2 <- mean(erkek) # ikinci grup ortalamasi

sd1 <- sd(kiz)     # Birinci grup standart sapmasi
sd2 <- sd(erkek)     # ikinci grup standart sapmasi

#varyans homojenligi
var.test(kiz, erkek)
#p=0.6797--> varyanslar homojen

#hipotez test
t_result <- t.test(kiz, erkek, var.equal = TRUE, alternative = "two.sided")
t_result
#t_result2 <- t.test(kiz, erkek, var.equal = TRUE, mu=,)
#t_result2

print(t_result$conf.int)  # %95 guven araligi
print(t_result$statistic)
print(t_result$p.value)  #hipotez testi p-value



#Soru3
n1<-15; n2<-15 #orneklem buyuklukleri
sd1<-645; sd2<-708  #st.sapma
var1<-sd1^2; var2<-sd2^2;var1;var2

# F istatistigi (Varyans orani)
F_stat <- var2 / var1 #buyuk/kucuk

# Serbestlik dereceleri
df1 <- n1 - 1
df2 <- n2 - 1

# p-degeri hesaplama (iki yanli test)
p_value <- 2 * min(pf(F_stat, df1, df2, lower.tail = FALSE),
                   pf(F_stat, df1, df2, lower.tail = TRUE))

F_stat
p_value
cat("F istatistigi:", F_stat, "\n")
cat("p-degeri:", p_value, "\n")



#Soru4
#hipotez test:
prop.test(c(120,210),c(550,620), correct = FALSE, alternative ="less")
#guven araligi:
prop.test(c(120,210),c(550,620), correct = FALSE, alternative ="two.sided")

