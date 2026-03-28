import numpy as np

rng = np.random.default_rng(seed=26)
kitle = rng.normal(loc=50, scale=10, size=10000)
print(kitle)

n10_means = []
n30_means = []
n100_means = []
n500_means = []
# Seed kullanmıyorum (rng.choice) çünkü kaydetmeme gerek yok sadece ortalmaları gereklı
for i in range(1000):
    sample10 = rng.choice(kitle,size=10)
    n10_means.append(sample10)
    
    sample30 = rng.choice(kitle,size=30)
    n30_means.append(sample30)
    
    sample100 = rng.choice(kitle,size=100)
    n100_means.append(sample100)

    sample500 = rng.choice(kitle,size=500)
    n500_means.append(sample500)
print(n10_means)

