###yardım
?var
help(var)
help(mean)

### atama operatoru
a <- 5
b<-10
x<-c(1,2,3,7,8,9)
y<-x+10;y

###calisma alanındaki kayitli nesneler
ls()

###grafik
plot(x)
plot(y)
par(mfrow=c(1,1))
par(mfrow=c(1,2))
plot(x)
plot(y)


###nesne olusturma
tamsayi<-2L
sayi<-2
ondalik<-2.5
karakter<- "modelleme"
mantiksal<- TRUE

###nesne turu sorgulama
typeof(tamsayi)
typeof(sayi)
typeof(ondalik)
typeof(karakter)
typeof(mantiksal)

#class
##########
mode(tamsayi)
mode(sayi)
mode(ondalik)




is.double(sayi)
is.numeric(sayi)
is.integer(sayi)



###paket yukleme###
install.packages("GGally")
install.packages("pracma")

library(GGally)
library(pracma)



###veri okutma
##1.yol
data<-read.csv(file.choose(),header=TRUE, sep=";")


##2.yol
library(haven)
Tanitim <- read_sav("C:/Users/Asus/Desktop/Tanitim.sav")
View(Tanitim)

##3.yol

#library(haven)
Tanitim2 <- read_sav("C:\\Users\\Asus\\Desktop\\Tanitim.sav")
View(Tanitim2)

head(Tanitim,4)
attach(Tanitim)

Tanitimdf<-data.frame(Tanitim)

Tanitim$cinsiyet<- factor(Tanitim$cinsiyet, 
                 levels=c(1,2), 
                 labels=c("kiz","erkek"))

Tanitim
mean(puan)

mean(Tanitim$puan)

rm(list=ls())
