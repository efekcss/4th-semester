import numpy as np
import pandas as pd
import matplotlib as mpl
"""
Ödev 1 dışında farklı ödev bölümlerinde normal 
dağılıma bağlı ancak farklı bir dağılım kullanırsak 
diye def ile fonksiyon olarak tanımlıyorum.
"""
def normal_dagilim(mu=50, std_sapma=100, n=10000):
    return np.random.normal(loc=mu, scale=std_sapma, size=n)

kitle = normal_dagilim()
print(f"Kitle Degerleri : {kitle}")
"""
Bölüm 1
Kitle Parametrelerinin hesaplanmasi;
* Kitle ortalaması
* Kitle varyansı
"""
def ort(degerler, n):
    toplam = 0
    for i in degerler:
        toplam += i
    return (toplam/n)
kitle_ort = ort(kitle,10000)
print(f"Kitle Ortalaması = {kitle_ort}")
