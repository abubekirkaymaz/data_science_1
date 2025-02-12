import numpy as np

# 50 kişilik rastgele veri seti oluşturuyoruz
np.random.seed(42)  # Aynı rastgele verileri tekrar almak için

# Yaş: 18 ile 70 arasında rastgele
age = np.random.randint(18, 71, 50)

# Boy: 150 cm ile 190 cm arasında rastgele
height = np.random.randint(150, 191, 50)

# Kilo: 40 kg ile 100 kg arasında rastgele
weight = np.random.randint(40, 101, 50)

# Gelir: 1000 USD ile 5000 USD arasında rastgele
income = np.random.randint(1000, 5001, 50)

# Eğitim durumu: 1 ile 4 arasında rastgele
education = np.random.randint(1, 5, 50)

# Verileri yazdır
# print("Yaş:", age)
# print("Boy (cm):", height)
# print("Kilo (kg):", weight)
# print("Gelir (USD):", income)
# print("Eğitim Durumu:", education)

data_lists = [age, height, weight, income, education]

data_arrays = [np.array(data) for data in data_lists]

for idx in range(len(data_arrays)):
    data_arrays[idx] = data_arrays[idx].reshape(50, 1)

all_arr = np.hstack(data_arrays)
#np.hstack() fonksiyonu aslında tuple alır. Ancak, listeyi bir tuple'a dönüştürmeden de çalışabilir çünkü np.hstack() fonksiyonu listeyi otomatik olarak bir tuple gibi kabul eder.


print(all_arr.size) #250 >> dizideki toplam veri sayısı
print(all_arr.shape) #(50, 5) 1d bir dizi
print(all_arr.dtype) #int32 >> integer tipinde veri
print(all_arr.ndim) #2 boyutlu dizi
print(all_arr)

#------------------------------------------------------------------#
# 1-Indexing-Slicing
#------------------------------------------------------------------#

# #3. sütunda ki ilk 10 veriyi 2 şer atlayarak almak
# print(all_arr[0:10:2, 2])

# #dizideki ilk dört satırın sütunlarını 2'şer atlayarak almak
# print(all_arr[0:4, 0:5:2])

# # İlk 20 satırın, 4. sütun hariç tüm verilerini alıyoruz
# result = np.delete(all_arr[0:20, :], 3, axis=1)  # 3. index olan 4. sütunu atıyoruz.axis=1 parametresi sütunları (yani yatay) silmeyi belirtir.
# print(result)

# # İlk 20 satırın, 4. ve 2. sütun hariç tüm verilerini alıyoruz
# result = np.delete(all_arr[0:20, :], [1, 3], axis=1)  # 2. ve 4. sütunları atıyoruz
# print(result)


# # İlk 20 satırdaki, 1. indeksten 3. indekse kadar olan sütunları siliyoruz
# result = np.delete(all_arr[0:20, :], range(1, 4), axis=1)  # 1, 2, 3. sütunları siliyoruz
# print(result)











#----------------------------------------------------------------------------------------------------------------------------------------
#1-The first step in data science is to transform it into arrays of numbers.
#2-Note that once an array is created in numpy, its size cannot be changed.
#3-Size tells us how big the array is, shape tells us the dimension.
#4-np.array bir fonksiyondur, yani bir şeyler yapar (listeyi Numpy dizisine dönüştürmek gibi).
#5-ndarray.size ise bir özelliktir, yani mevcut bir Numpy dizisi hakkinda bilgi verir (eleman sayisini döndürmek gibi).
#6-Another characteristic about numpy array is that it is homogeneous, meaning each element must be of the same data type.
#7-#Numpy supports several data types such as int (integer), float (numeric floating point), and bool (boolean values, True and False).
#8-iki dizeyi yataş birleştirmek istersek, satır sayıları aynı olmalı, (axis=1)
#9-iki dizeyi dikey birleştirmek istersek, sütun sayıları aynı olmalı, (axis=0)


#------------------------------------------------------------------#
# 2-Indexing-Slicing
#------------------------------------------------------------------#

#Axis 0 (↓): Yukaridan aşağiya gider, satirlar boyunca işler.
#Axis 1 (→): Soldan sağa gider, sütunlar boyunca işler.

# heights_ages = heights + ages
# heights_ages_arr = np.array(heights_ages)

# new_arr = heights_ages_arr.reshape(2, -1)
# print(new_arr)

# print(new_arr[1,2]) #2. satir, 3. sütunda ki eleman>> tek eleman seçme>>x-y koordinati belirtme gibi
# print(new_arr[0,20]) #1. satir, 21. sütunda ki eleman

# print(new_arr[1,2]) #2. satir, 3. sütunda ki eleman>> tek eleman seçme>>x-y koordinati belirtme gibi
# print(new_arr[0,20]) #1. satir, 21. sütunda ki eleman

# print(new_arr[1, :]) # tümünü seçmek istiyorsak ya boş birakilacak [0:3,], ya da boş ":"" işareti koyulacak [0:3, :]
# #print(new_arr[, 1:3]) #bu işlem hata verir, çünkü satir tarafi yani virgülün solu için bir belirtme yapilmasi gerekir.
# print(new_arr[:, 1:3]) #doğru kullanim bu şekilde. Virgülün solu boş birakilmaz.
# print(new_arr[1,5]) #doğru kullanim bu şekilde. Virgülün solu boş birakilmaz.

# print(type(new_arr)) #<class 'numpy.ndarray'>

# print(new_arr[0:1, 0:3]) #satir dilimlemesi yapildiği için sonuç bir 2D dizi olur.
# print(new_arr[0, 0:3])  #doğrudan satir seçildiği için, sonuç bir 1D dizi olur.


# #We use ":" to select all the elements from the index up to but not including the ending index. This is called slicing.
# #NumPy'de sütun indeksi belirtilmediğinde, tüm sütunlar seçilir.

# #Numpy Slicing Sözdizimi:
# #start: Dilimleme işleminin başlangiç indeksini belirtir (varsayilan: 0).
# #stop: Dilimlemenin nerede duracağini belirtir (bu indeks dahil edilmez) (varsayilan: boyutun sonu).
# #step: Dilimleme işleminin adim boyutunu belirtir (varsayilan: 1).
# #Sözdizimi: array[start:stop:step]

# heights = [189, 170, 189, 163, 183, 171, 185, 168, 173, 183, 173, 173, 175, 178, 183, 193, 178, 173, 174, 183, 183, 180, 168, 180, 170, 178, 182, 180, 183, 178, 182, 188, 175, 179, 183, 193, 182, 183, 177, 185, 188, 188, 182, 185, 191]

# ages = [57, 61, 57, 57, 58, 57, 61, 54, 68, 51, 49, 64, 50, 48, 65, 52, 56, 46, 54, 49, 51, 47, 55, 55, 54, 42, 51, 56, 55, 51, 54, 51, 60, 62, 43, 55, 56, 61, 52, 69, 64, 46, 54, 47, 70]

# heights_and_ages = heights + ages
# heights_and_ages_arr = np.array(heights_and_ages)
# heights_and_ages_arr = heights_and_ages_arr.reshape((2,45))
# print(heights_and_ages_arr)

# print(heights_and_ages_arr[0, 0:3]) #ilk satirin ilk 3 kaydi. 0:3 >> birinci değer (0) dahil, ikinci değer (3) dahil değil.
# print(heights_and_ages_arr[0, :3])  # ,:3 de başlangiç değeri 0 ise ihmal edilebilir.>>When the starting index is 0, we can omit it
# print(heights_and_ages_arr[0, 9:])  # ,9: de index 9 (10. değer) dan (dahil) satirin sonuna kadar alir
# print(heights_and_ages_arr[:, 3])   # 4. sütunun tamamini alir

# print(heights_and_ages_arr[1:4]) 
# #1. indeksli satirin tamammini (2. satir) seçer. 2 ve 3. indekste satir olmadiğindan onlari atlar ve hata vermez.


# print(heights_and_ages_arr[0,:])
# #heights_and_ages_arr[0, :]
# # 0 → 0. satiri seçer.
# # : → Tüm sütunlari seçer.
# # Açik ve standart bir NumPy dizisi dilimleme yöntemidir.

# # heights_and_ages_arr[0,]
# # Python'da sondaki virgül gereksizdir ve yokmuş gibi davranilir.
# # Yani heights_and_ages_arr[0] ile aynidir.

# # heights_and_ages_arr[0]
# # NumPy'de tek bir indeksle erişildiğinde, varsayilan olarak tüm sütunlar seçilir.
# # Yani heights_and_ages_arr[0, :] ile aynidir.


# arr = np.array([10, 20, 30, 40, 50, 60, 70])
# print("Array:", arr) #Array: [10 20 30 40 50 60 70]

# print(arr[1:4])  # [20 30 40]
# # Tek boyutlu dizilerde (1D), NumPy satir veya sütun ayrimi yapmaz, sadece indeks araliğini alir.
# # iki boyutlu dizilerde (2D), satir-sütun seçimi yapabilirsiniz.
# # Eğer satir-sütun ayrimi yapmak istiyorsaniz, 2D bir NumPy dizisi kullanmalisiniz.

# print(arr[:4])  # [10 20 30 40]
# #Başlangiç: Varsayilan olarak 0 (ilk elemandan başla).
# #Bitiş: 4 (indeks 4'e kadar).
# #Adim: Varsayilan olarak 1.

# print(arr[::2])  # [10 30 50 70]
# #Başlangiç: Varsayilan olarak 0.
# #Bitiş: Varsayilan olarak dizinin sonuna kadar.
# #Adim: 2 (Her 2. elemani al).

# print(arr[-3:])  # [50 60 70]
# #Başlangiç: Sondan 3. elemandan (50) başla.
# #Bitiş: Varsayilan olarak dizinin sonuna kadar.
# #Adim: Varsayilan olarak 1.

# print(arr[::-1]) #[70 60 50 40 30 20 10]
# #Başlangiç: Varsayilan olarak dizinin sonundan başla.
# #Bitiş: Varsayilan olarak dizinin başina kadar git.
# #Adim: -1 (Diziyi ters çevir).

# print(arr[-1:4:-1]) #[70 60]
# #Başlangiç: Dizinin sonundan başla.
# #Bitiş: Dördüncü indekse kadar git
# #Adim: -1 Dizenin sonundan dördüncü indekse doğru git.


# arr_2d = np.array([
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12]
# ])

# print("2D Array:\n", arr_2d)

# print(arr_2d[1:, 2:])
# # [[ 7  8]
# #  [11 12]]
# #Satirlar (axis 0): 1: (1. satirdan başla, sonuna kadar al).
# #Sütunlar (axis 1): 2: (2. sütundan başla, sonuna kadar al).

# print(arr_2d[:, ::2])
# # [[ 1  3]
# #  [ 5  7]
# #  [ 9 11]]
# #Satirlar (axis 0): : (tüm satirlari al).
# #Sütunlar (axis 1): ::2 (Her 2. sütunu al).

# print("--------------------------")
# print(arr_2d[::2, 1]) #her 2 satirdan birinin ikinci sütununu al


#------------------------------------------------------------------#
#Assigning Single Values
#------------------------------------------------------------------#

# heights_and_ages = heights + ages 
# heights_and_ages_arr = np.array(heights_and_ages)
# heights_and_ages_arr = heights_and_ages_arr.reshape((2,45))

# print(heights_and_ages_arr)
# heights_and_ages_arr[0, 3] = 165 #ilk satirin 3. indexinde ki 163 >>> 165 olarak değişti
# print(heights_and_ages_arr)

# heights_and_ages_arr[0,:] = 180 # ilk satirin tüm verileri (:) 180 olarak değişti
# print(heights_and_ages_arr)

# heights_and_ages_arr[:2, :5] = 0 #ilk iki satirin ilk beş verisi 0 ile değiştirildi
# print(heights_and_ages_arr)



#------------------------------------------------------------------#
#Assigning Values
#------------------------------------------------------------------#

#In addition, a 1darray or a 2darry can be assigned to a subset of another 2darray, as long as their shapes match.

# heights_and_ages = heights + ages
# heights_and_ages_arr = np.array(heights_and_ages)
# heights_and_ages_arr = heights_and_ages_arr.reshape((2,45))
# print(heights_and_ages_arr)
# heights_and_ages_arr[:, 0:5] = [0, 11, 22, 33, 44]  #tüm satirlarin ilk beş verisine yeni değerler atandi
# print(heights_and_ages_arr)

#NumPy, broadcasting sayesinde [0, 11, 22, 33, 44] listesini otomatik olarak (2,5) şekline getiriyor ve her satira ayni değerleri kopyaliyor. Bu yüzden tek boyutlu bir dizi, çok boyutlu bir bölgeye atanabiliyor.


# Eğer farkli bir atama yapmak istersen, örneğin her sütunun farkli değerler almasini istersen, şu şekilde (2,5) biçiminde bir dizi sağlaman gerekir:
# heights_and_ages_arr[:, 0:5] = np.array([[0, 1, 2, 3, 4], 
#                                          [10, 11, 12, 13, 14]])
# print(heights_and_ages_arr)


# #-------------------------------------------------------------------------
# arr = np.zeros((4, 3))  # 4 satir, 3 sütunluk bir matris (sifirlarla dolu)
# print("Başlangiç dizisi:\n", arr)

# arr[:, 0] = [10, 20, 30, 40]  # ilk sütuna 1D bir liste atiyoruz

# print("Güncellenmiş dizi:\n", arr)
# #NumPy, (4,) şeklindeki 1D listeyi (4,1) olarak yorumladi ve otomatik olarak genişletti.
# #-------------------------------------------------------------------------

# arr[:, :] = [10, 20, 30]  # (3,) şeklindeki liste, (4,3) matrisine genişletilir
# print("Tüm sütunlar güncellendi:\n", arr)
# #Eğer tüm sütunlari ayni 1D diziyle doldurmak istersek, NumPy bunu da broadcasting ile genişletebilir:
# #-------------------------------------------------------------------------

"""
Özet
Satir bazinda broadcasting
(1D → (n, m)) şeklinde bir genişleme, satirlarda tekrar ederek çalişir.
Örnek: arr[:, 0:5] = [1, 2, 3, 4, 5] → (2,5) şekline genişler.

Sütun bazinda broadcasting
(n,) → (n, 1) şeklinde bir genişleme olur ve sütunlara uygulanabilir.
Örnek: arr[:, 0] = [10, 20, 30, 40] → (4,1) olarak genişletilir.

Tüm matris için broadcasting
(m,) → (n, m) şeklinde genişler.
Örnek: arr[:, :] = [10, 20, 30] → (4,3) olur.

NumPy Broadcasting Kurallari
NumPy, atama yapilan verinin boyutunu hedef diziye uygun hale getirmek için şu kurallari kullanir:

1️⃣ Boyut Eşitleme

Eğer atama yapilan subset (hedef alan) ile atama yapilacak veri ayni boyuta sahipse, doğrudan atanir.
Örneğin:

arr = np.zeros((3, 3))
arr[:, :] = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
Burada (3,3) dizi, (3,3) matrisle birebir uyuştuğu için doğrudan kopyalanir.
2️⃣ Tek Boyutlu (1D) Veri Atamasi (Satir veya Sütun Yayildiğinda)

Eğer atanan dizi (m,) şeklinde ise:
(m,) → (1, m) veya (m, 1) yapilarak uygun bir yöne yayilir.
Eğer satir bazli bir atama yapiliyorsa, (1, m) olur.
Eğer sütun bazli bir atama yapiliyorsa, (m, 1) olur.
3️⃣ Boyutu 1 Olan Eksik Eksenler (1D → 2D Dönüşüm ve Yayilma)

Özel olarak, (n, 1) veya (1, m) gibi boyutu 1 olan eksenler NumPy tarafindan tekrar ettirilebilir.
Bu yüzden [:, 0] = (n,) olan bir vektör sütun olarak,
arr[0, :] = (m,) olan bir vektör satir olarak yayilir.
"""

# heights_and_ages = heights + ages
# heights_and_ages_arr = np.array(heights_and_ages)
# heights_and_ages_arr = heights_and_ages_arr.reshape((6,-1))

# print(heights_and_ages_arr)
# heights_and_ages_arr[0:4, 2:5] = np.array([0, 0, 0, 0]).reshape(4,1)
# print(heights_and_ages_arr)

# heights_and_ages_arr[0:4, 2:5] = np.array([0, 0, 0]).reshape(1,3)


#------------------------------------------------------------------#
#Combining Two Arrays
#------------------------------------------------------------------#
#To combine more than two arrays horizontally, simply add the additional arrays into the tuple.

# # Örnek sütun vektörleri
# heights = np.array([[150], [160], [170]])
# ages = np.array([[25], [30], [35]])
# weights = np.array([[60], [70], [80]])

# # Yatay birleştirme
# combined = np.hstack((heights, ages, weights))
# #You can use np.hstack to concatenate arrays ONLY if they have the same number of rows.
# print(combined)

#More generally, we can use the function numpy.concatenate. If we want to concatenate, link together, two arrays along rows, then pass 'axis = 1' to achieve the same result as using numpy.hstack; and pass 'axis = 0' if you want to combine arrays vertically.

# heights = [189, 170, 189, 163, 183, 171, 185, 168, 173, 183, 173, 173, 175, 178, 183, 193, 178, 173, 174, 183, 183, 180, 168, 180, 170, 178, 182, 180, 183, 178, 182, 188, 175, 179, 183, 193, 182, 183, 177, 185, 188, 188, 182, 185, 191]
# ages = [57, 61, 57, 57, 58, 57, 61, 54, 68, 51, 49, 64, 50, 48, 65, 52, 56, 46, 54, 49, 51, 47, 55, 55, 54, 42, 51, 56, 55, 51, 54, 51, 60, 62, 43, 55, 56, 61, 52, 69, 64, 46, 54, 47, 70]

# heights_arr = np.array(heights)
# ages_arr = np.array(ages)

# heights_arr = heights_arr.reshape((45,1))
# ages_arr = ages_arr.reshape((45,1))

# # height_age_arr = np.hstack((heights_arr, ages_arr))
# height_age_arr = np.concatenate((heights_arr, ages_arr), axis=1) 
# print(height_age_arr.shape) #(45, 2)
# print(height_age_arr[:3,:])

# # Dikey birleştirme: birleştirilen dizilerin sütun sayıları eşit olmalı
# arr_1 = np.array([[1,2,3],
#          [22,22,33]])
# arr_2 = np.array([[10,20,30],
#          [5,15,25],
#          [44,55,66]])


# # arr = np.vstack((arr_1, arr_2))
# arr = np.concatenate((arr_1,arr_2), axis=0)
# print(arr)


#------------------------------------------------------------------#
#Mathematical Operations on Arrays
#------------------------------------------------------------------#

# heights_arr = np.array(heights)
# ages_arr = np.array(ages)

# heights_arr = heights_arr.reshape((45,1))
# ages_arr = ages_arr.reshape((45,1))
# height_age_arr = np.hstack((heights_arr, ages_arr))

# print(height_age_arr[:,0]*0.0328084)

# #Now we have all heights in feet. Note that this operation won’t change the original array, it returns a new 1darray where 0.0328084 has been multiplied to each element in the first column of 'heights_age_arr'.

# #Numpy Array Mathematical Methods
# print(height_age_arr.sum()) 
# print(height_age_arr.sum(axis=0))  #[8100 2475] >> sütunlar toplamlari
# print(height_age_arr.sum(axis=1)) #satirlar toplamlari

# #Other operations, such as .min(), .max(), .mean(), work in a similar way to .sum().

#------------------------------------------------------------------#
#Comparisons
#------------------------------------------------------------------#

# heights_arr = np.array(heights)
# ages_arr = np.array(ages)

# heights_arr = heights_arr.reshape((45,1))
# ages_arr = ages_arr.reshape((45,1))
# height_age_arr = np.hstack((heights_arr, ages_arr))

# print(height_age_arr[:, 1] < 55)
# print(height_age_arr[:, 1] == 51)
# print((height_age_arr[:, 1] == 51).sum()) #True is treated as 1 and False as 0 in the sum.

#------------------------------------------------------------------#
#Mask & Subsetting
#------------------------------------------------------------------#
# heights_arr = np.array(heights)
# ages_arr = np.array(ages)

# heights_arr = heights_arr.reshape((45,1))
# ages_arr = ages_arr.reshape((45,1))
# height_age_arr = np.hstack((heights_arr, ages_arr))

# mask = height_age_arr[:, 0] >= 182

# print(mask)
# print(mask.sum())

# tall_presidents = height_age_arr[mask, ]

# print(tall_presidents.shape)

#Extra:new_arr = heights_ages_arr.reshape(2, -1).T

# mask = height_age_arr[:, 0] >= 180 # ilk sütunda 180 den büyük ve eşit olan değerler için bir mask değişkeni tanimladik

# print(mask.shape)

# print(height_age_arr[mask,]) #esas dizimizde bu mask değişkeninin tuttuğu değerleri tüm satirlara uyguladiğimizda koşulu sağlayan değerler listelenir.

# arr = np.array([
#     [10,  20,  30,  40,  50],   # 0. satir
#     [60,  70,  80,  90, 100]    # 1. satir
# ])

# mask = arr[1, :] > 80
# # print(mask) #[False False False  True  True]

# filtered_arr = arr[:, mask]
# # print(filtered_arr)

# mask = (height_age_arr[:, 0]>=182) & (height_age_arr[:,1]<=50)
# print(height_age_arr[mask,])

#MASK EXERCiSES
"""
#1-Bir NumPy array’i oluştur ve sadece pozitif olan elemanlari seçerek yeni bir array oluştur.
arr = np.array([-3, 7, -1, 4, -9, 10, 0, -2])  
print(arr)
print("---------------------------------------------------")
mask = arr > 0
print(arr[mask])

#2-Aşağidaki array’den 10 ile 30 arasindaki (10 ve 30 dahil) sayilari seç ve yeni bir array oluştur.
arr = np.array([5, 12, 25, 30, 7, 40, 15, 28, 35])  

mask = (arr >= 10) & (arr <= 30)
print(arr[mask])

#3-Aşağidaki array’de tek sayilari -1 ile değiştir.
arr = np.array([4, 9, 12, 15, 22, 33, 42])

mask = arr % 2 != 0  
arr[mask] = -1  
print(arr)

#4-Aşağidaki array içinden sadece 2 veya 5 ile tam bölünebilen sayilari içeren yeni bir array oluştur.
arr = np.array([10, 17, 22, 25, 30, 37, 40, 45])  

mask = (arr % 2 == 0) & (arr % 5 == 0)
print(arr[mask])

#5-Aşağidaki NumPy array'inde NaN (Not a Number) değerlerini maskele ve sadece geçerli sayilari içeren bir array oluştur.
arr = np.array([3.4, np.nan, 5.6, np.nan, 7.8, 10.2])
mask = ~np.isnan(arr)  # NaN olmayanlari seçmek için tersleme (~) kullanilir
new_arr = arr[mask]
print(new_arr)

#6-Aşağidaki dizide, 10'dan küçük olan elemanlari seçin:
arr = np.array([2, 8, 12, 5, 20, 7, 15])
mask = arr < 10
print(arr[mask])

#7-Aşağidaki dizideki negatif sayilari sifirla değiştirin:
arr = np.array([1, -5, 3, -2, 7, -1, 4])
mask = arr < 0
arr[mask] = 0
print(arr)

#8-Aşağidaki dizideki sadece çift sayilari seçin:
arr = np.array([11, 24, 9, 16, 31, 8, 17])
mask = arr % 2 == 0

print(arr[mask])

#9-Aşağidaki dizideki 5'e bölünebilen sayilari seçin:
arr = np.array([13, 25, 30, 7, 45, 12, 20])
mask = arr % 5 == 0
print(arr[mask])

#10-Aşağidaki dizide, NaN olmayan elemanlari sirasiyla 3'e bölün:
arr = np.array([12, np.nan, 15, np.nan, 24, 18])
mask = ~np.isnan(arr)

new_arr_1 = arr[mask] / 3
print(new_arr_1)

#11-NaN değerler ayni indekslerinde kalacak ve diğerleri ise 3 bölümleri olacak  
arr = np.array([12, np.nan, 15, np.nan, 24, 18])
mask = ~np.isnan(arr)  # NaN olmayan elemanlari seçer

#12-NaN olmayan elemanlari 3'e böler, NaN'ler olduğu gibi kalir
arr_result = arr.copy()  # Orijinal diziyi bozmamak için bir kopya oluşturuyoruz
arr_result[mask] = arr_result[mask] / 3
print(arr_result)  # Yeni diziyi yazdirir

#13-Soru: Bir NumPy dizisi oluşturun ve bu dizideki tek sayilari sifirla değiştirin.
arr = np.array([12, 7, 14, 19, 20, 25, 30])
mask = arr % 2 != 0
arr[mask] = 0
print(arr)

#14-Soru:Bir NumPy dizisinde, 5'e bölünebilen sayilari 2 ile çarpin ve sonucu yazdirin.
arr = np.array([3, 10, 15, 18, 25, 30, 35])
mask = arr % 5 == 0
arr[mask] = arr[mask] * 2
print(arr)

#15-Soru: Bir NumPy dizisinde, tüm pozitif sayilari 3 ile bölecek şekilde yeni bir diziyi oluşturun. NaN değerlerini olduğu gibi birakin.
arr = np.array([10, -3, 15, np.nan, 25, -2])

mask = ~np.isnan(arr)   #~ (tilde)
arr[mask] = arr[mask] / 3
print(arr)

#16-sadece pozitif sayilari 3 ile bölmek
arr = np.array([10, -3, 15, np.nan, 25, -2])
mask = (~np.isnan(arr))  & (arr > 0)
arr[mask] = arr[mask] / 3
print(arr)


#17-Soru: Bir NumPy dizisinde, 10'dan küçük olan sayilari 10 ile toplayin ve sonucu yazdirin.
arr = np.array([5, 15, 3, 22, 8, 1])

mask = arr < 10
arr[mask] = arr[mask] + 10

print(arr)

#18-Soru: Bir NumPy dizisinde, 3'e bölünebilen sayilari 10 ile değiştirin ve sonucu yazdirin.
arr = np.array([9, 14, 30, 7, 18, 21, 5])

mask = arr % 3 == 0
arr[mask] = 10
print(arr)

#19-Aşağidaki NumPy dizisini kullanarak, hem 3'e hem de 5'e bölünebilen elemanlari 3 ile çarpin ve dizinin tamamini yazdirin.
arr = np.array([15, 30, 12, 45, 18, 25, 50, 7, 10, 35])
mask = (arr % 3 == 0) & (arr % 5 == 0)
arr[mask] = arr[mask] * 3
print(arr) 


#20-Bir NumPy dizisini ele alalim. Bu dizide 3'e bölünebilen ve 7'ye bölünebilen sayilara 5 ekleyin. Dizinin geri kalanini olduğu gibi birakin. Sonucu yazdirin.
arr = np.array([14, 21, 28, 9, 5, 33, 49, 63, 8, 12])
mask = (arr % 3 == 0) & (arr % 7 == 0)
arr[mask] = arr[mask] + 5
print(arr)
 
#21-Aşağidaki NumPy dizisini kullanarak, dizinin en küçük ve en büyük değerleri dişindaki tüm değerleri 0 ile değiştirin. Sonucu yazdirin 
arr = np.array([5, 12, 19, 2, 31, 8, 22, 4, 17])
# En küçük ve en büyük değerleri buluyoruz
min_val = np.min(arr)
max_val = np.max(arr)
# Maske oluşturuyoruz: En küçük ve en büyük değerler dişindaki tüm değerler seçilecek
mask = (arr != min_val) & (arr != max_val)
# En küçük ve en büyük dişindaki değerleri 0 yapiyoruz
arr[mask] = 0
print(arr)


#22-Aşağidaki NumPy dizisinde negatif sayilari pozitif yapin ve 0 olan elemanlari olduğu gibi birakin. Sonucu yazdirin. 
arr = np.array([4, -5, 10, 0, -12, 15, -3, 0, -9])
mask = arr < 0 
arr[mask] = -arr[mask]
print(arr)


#23-Aşağidaki 2 boyutlu dizide, yalnizca çift sayilari seçip yazdiran bir maske uygulayin.
arr = np.array([[4, 7, 12], [3, 8, 6], [9, 10, 2]])

mask = arr % 2 == 0

print("--------------------")
print(arr[mask])

#23-Aşağidaki 2 boyutlu dizide, ilk iki sütunda ki değerlerden negatif olanlari 333 değeri ile değiştir.
arr = np.array([[2, -3, 5], [-8, 12, 7], [0, -1, 4]])
mask = arr[:, 0:2] < 0
arr[:, 0:2][mask] = 333
print(arr)

#Aşağidaki 2 boyutlu dizide, yalnizca pozitif sayilari seçip yazdiran bir maske uygulayin.
arr = np.array([[2, -3, 5], [-8, 12, 7], [0, -1, 4]])
# Maskeyi pozitif sayilari seçecek şekilde tanimliyoruz
mask = arr >= 0
# Maskeyi kullanarak sadece pozitif sayilari içeren yeni bir dizi oluşturuyoruz
positive_arr = np.where(mask, arr, np.nan)
print(positive_arr)

#Aşağidaki 2 boyutlu dizide, negatif olmayan sayilari (sifir dahil) seçip yazdiran bir maske oluşturun.
arr = np.array([[-5, 2, 10], [-3, 0, -1], [4, 7, -8]])
mask = arr >= 0
new_arr = np.where(mask, arr, -111)
print(new_arr)
"""

#----------------------------------------------------------------------------------------------------------------------------
# #PRACTICE EXERCISE-Data Science - Average of Rows
# import numpy as np

# # Kullanicidan giriş almak
# n, p = map(int, input().split())  # ilk satir: satir ve sütun sayisi
# matrix = []  # Boş liste

# for _ in range(n):
#     row = list(map(float, input().split()))  # Satir verilerini al
#     matrix.append(row)

# # NumPy array'e dönüştür
# matrix_np = np.array(matrix)

# # Satir ortalamalarini hesapla
# row_means = np.mean(matrix_np, axis=1)

# # Sonuçlari yuvarla
# row_means_rounded = np.round(row_means, 2)

# # Çiktiyi yazdir
# print(row_means_rounded)
