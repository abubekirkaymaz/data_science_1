import random
import numpy  as np
from openpyxl import Workbook


random_numbers = np.random.randint(500, 5001, size=20)
print(random_numbers)

random_floats = np.random.uniform(1.0, 10.0, size=20)
print(random_floats)

rounded_floats = np.around(random_floats, decimals=2)
print(rounded_floats)

print(type(random_numbers))

trash_data = Workbook()
worksheet = trash_data.active




"""
print(random.random())

#random.randint(a, b) >> Açıklama: a ile b arasında (dahil) rastgele bir tam sayı (integer) döndürür.
print(random.randint(1, 10))

#random.uniform(a, b) >> Açıklama: a ile b arasında rastgele bir kayan noktalı sayı (float) döndürür.
print(random.uniform(1, 5))

#random.choice(seq) >> Açıklama: Bir diziden (liste, tuple, string vb.) rastgele bir öğe seçer.
my_list = ["elma", "armut", "çilek"]
print(random.choice(my_list))

#random.shuffle(seq) >> Açıklama: Bir dizinin (liste) öğelerini rastgele karıştırır. Listenin kendisini değiştirir.
my_list = [1, 2, 3, 4, 5]
random.shuffle(my_list)
print(my_list)

#random.sample(population, k) >> Açıklama: Bir diziden (population) belirli sayıda (k) benzersiz öğe seçer.
my_list = [1, 2, 3, 4, 5]
print(random.sample(my_list, 3))

#random.seed(a=None) >> Açıklama: Rastgele sayı üretecinin başlangıç değerini (seed) ayarlar. Aynı seed değeri kullanıldığında, aynı rastgele sayılar üretilir. Bu, tekrarlanabilirlik sağlar.
#random.seed(42)  # Seed değerini ayarla
print(random.randint(1, 100))  # Her zaman aynı sonucu verir, örneğin: 82

#random.randrange(start, stop, step) >> Açıklama: Belirli bir aralıkta (start ile stop arasında) ve belirli bir adımla (step) rastgele bir tam sayı döndürür.
print(random.randrange(0, 10, 2))  # Örnek çıktı: 6 (0, 2, 4, 6, 8 arasından)

#random.choices(population, weights=None, k=1) >> Açıklama: Bir diziden (population) belirli sayıda (k) öğe seçer. weights parametresi ile her öğenin seçilme olasılığını ayarlayabilirsiniz.
my_list = ["elma", "armut", "çilek"]
print(random.choices(my_list, weights=[10, 1, 1], k=2))  # Örnek çıktı: ["elma", "elma"]

#random.gauss(mu, sigma) >> Açıklama: Normal dağılıma (Gauss dağılımı) uygun bir rastgele sayı döndürür. mu ortalama, sigma standart sapmadır.
print(random.gauss(0, 1))  # Örnek çıktı: 0.123456 (ortalama 0, standart sapma 1)

#random.getrandbits(k) >>Açıklama: k bit uzunluğunda rastgele bir tam sayı döndürür.
print(random.getrandbits(8))  # Örnek çıktı: 173 (0 ile 255 arasında bir sayı)

#random.triangular(low, high, mode) >> Açıklama: Üçgen dağılıma uygun bir rastgele sayı döndürür. low minimum, high maksimum, mode en olası değerdir.
print(random.triangular(0, 10, 5))  # Örnek çıktı: 4.567

#random.betavariate(alpha, beta) >> Açıklama: Beta dağılımına uygun bir rastgele sayı döndürür.
print(random.betavariate(0.5, 0.5))  # Örnek çıktı: 0.123456

#random.expovariate(lambd) >> Açıklama: Üstel dağılıma uygun bir rastgele sayı döndürür. lambd, dağılımın parametresidir.
print(random.expovariate(1.5))  # Örnek çıktı: 0.456789

#random.gammavariate(alpha, beta) >> Açıklama: Gamma dağılımına uygun bir rastgele sayı döndürür.
print(random.gammavariate(1.0, 2.0))  # Örnek çıktı: 1.234567
"""