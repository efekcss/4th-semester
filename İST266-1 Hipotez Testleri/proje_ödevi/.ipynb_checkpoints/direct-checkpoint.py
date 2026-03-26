import numpy as np
import pandas as pd #Daha sonra kullanım için
import matplotlib as mpl # Daha sonra kullanma için
import os

"""
Ödev 1
"""
if not os.path.exists('odev1_kitle.npy'):
    degerler = np.random.normal(loc=50, scale=10, size=10000)
    np.save('odev1_kitle.npy', degerler)

kitle = np.load('odev1_kitle.npy')

print(kitle)

"""
Bölüm 1 - Kitle Parametrelerinin Hesaplanması
 - Kitle oratalaması 
 - Kitle varyansı 
hesabı
"""
# Kitle ortalaması
toplam = 0
for i in kitle:
    toplam += i
kitle_ort = toplam/len(kitle)
print(f"Kitle Ortalaması = {kitle_ort}")

# Kitle varyansı

toplam = 0
for i in kitle:
    denklem = (i - kitle_ort)**2
    toplam += denklem
kitle_var = toplam/len(kitle)
print(f"Kitle Varyansı = {kitle_var}")

"""
Bölğm 2 - Farklı Örneklem Büyüklükleri ile Nokta Tahmini
Oluşturduğumuz kitleden n=10, n=30, n=100, n=500 büyüklüklerinde
örneklemler oluşturalım

Soru : X'in dağılımının parametrelerine ait nokta tahmini için neleri kullanırsınız? Elde ettiğiniz tahminleri kitle parametreleri ile karşılaştırınız.
"""

