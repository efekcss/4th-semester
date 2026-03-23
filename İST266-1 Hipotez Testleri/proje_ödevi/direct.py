import numpy as np
import pandas as pd
import matplotlib as mpl
"""
Ödev 1 dışında farklı ödev bölümlerinde normal 
dağılıma bağlı ancak farklı bir dağılım kullanırsak 
diye def ile fonksiyon olarak tanımlıyorum.
"""
def normal_dagilim(mu=50, std_sapma=100, n=10000):
    return np.random.normal(loc=0.0, scale=std_sapma, size=n)

kitle = normal_dagilim()
print(kitle)
"""
Bölüm 1
Kitle Parametrelerinin hesaplanmasi
"""
def ort(degerler, n):
    toplam = 0
    for i in degerler:
        toplam += i
    return (toplam/n)
kitle_ort = ort(kitle,10000)
print(kitle_ort)