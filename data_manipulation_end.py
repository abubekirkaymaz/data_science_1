import numpy as np

#1-The first step in data science is to transform it into arrays of numbers.
#2-Note that once an array is created in numpy, its size cannot be changed.
#3-Size tells us how big the array is, shape tells us the dimension.
#4-np.array bir fonksiyondur, yani bir şeyler yapar (listeyi Numpy dizisine dönüştürmek gibi).
#5-ndarray.size ise bir özelliktir, yani mevcut bir Numpy dizisi hakkinda bilgi verir (eleman sayisini döndürmek gibi).
#6-Another characteristic about numpy array is that it is homogeneous, meaning each element must be of the same data type.
#7-#Numpy supports several data types such as int (integer), float (numeric floating point), and bool (boolean values, True and False).
#8-İki dizeyi yataş birleştirmek istersek, satır sayıları aynı olmalı, (axis=1)
#9-İki dizeyi dikey birleştirmek istersek, sütun sayıları aynı olmalı, (axis=0)


heights = [189, 170, 189, 163, 183, 171, 185, 168, 173, 183, 173, 173, 175, 178, 183, 193, 178, 173, 174, 183, 183, 180, 168, 180, 170, 178, 182, 180, 183, 178, 182, 188, 175, 179, 183, 193, 182, 183, 177, 185, 188, 188, 182, 185, 191]

ages = [57, 61, 57, 57, 58, 57, 61, 54, 68, 51, 49, 64, 50, 48, 65, 52, 56, 46, 54, 49, 51, 47, 55, 55, 54, 42, 51, 56, 55, 51, 54, 51, 60, 62, 43, 55, 56, 61, 52, 69, 64, 46, 54, 47, 70]

#------------------------------------------------------------------#
#Creat Array
#------------------------------------------------------------------#

# heights_arr = np.array(heights)
# ages_arr = np.array(ages)

# print(heights_arr.size)
# print(heights_arr.shape)
# print(ages_arr.dtype)
# print(heights_arr.ndim)

#------------------------------------------------------------------#
#Indexing
#------------------------------------------------------------------#

# #Axis 0 (↓): Yukaridan aşağiya gider, satirlar boyunca işler.
# #Axis 1 (→): Soldan sağa gider, sütunlar boyunca işler.

# heights_ages = heights + ages
# heights_ages_arr = np.array(heights_ages)

# new_arr = heights_ages_arr.reshape(2, -1)
# print(new_arr)

# print(new_arr[1,2]) #2. satir, 3. sütunda ki eleman>> tek eleman seçme>>x-y koordinati belirtme gibi
# print(new_arr[0,20]) #1. satir, 21. sütunda ki eleman

# print(new_arr[1,2]) #2. satir, 3. sütunda ki eleman>> tek eleman seçme>>x-y koordinati belirtme gibi
# print(new_arr[0,20]) #1. satir, 21. sütunda ki eleman


#------------------------------------------------------------------#
# Slicing
#------------------------------------------------------------------#

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
# # İki boyutlu dizilerde (2D), satir-sütun seçimi yapabilirsiniz.
# # Eğer satir-sütun ayrimi yapmak istiyorsaniz, 2D bir NumPy dizisi kullanmalisiniz.

# print(arr[:4])  # [10 20 30 40]
# #Başlangiç: Varsayilan olarak 0 (ilk elemandan başla).
# #Bitiş: 4 (İndeks 4'e kadar).
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
# heights_and_ages_arr[0, 3] = 165 #İlk satirin 3. indexinde ki 163 >>> 165 olarak değişti
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

# arr[:, 0] = [10, 20, 30, 40]  # İlk sütuna 1D bir liste atiyoruz

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
arr_1 = np.array([[1,2,3],
         [22,22,33]])
arr_2 = np.array([[10,20,30],
         [5,15,25],
         [44,55,66]])


# arr = np.vstack((arr_1, arr_2))
arr = np.concatenate((arr_1,arr_2), axis=0)
print(arr)





