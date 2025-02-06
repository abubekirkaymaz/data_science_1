import numpy as np

#1-The first step in data science is to transform it into arrays of numbers.
#2-Note that once an array is created in numpy, its size cannot be changed.
#3-Size tells us how big the array is, shape tells us the dimension.
#4-np.array bir fonksiyondur, yani bir şeyler yapar (listeyi Numpy dizisine dönüştürmek gibi).
#5-ndarray.size ise bir özelliktir, yani mevcut bir Numpy dizisi hakkinda bilgi verir (eleman sayisini döndürmek gibi).
#6-Another characteristic about numpy array is that it is homogeneous, meaning each element must be of the same data type.
#7-#Numpy supports several data types such as int (integer), float (numeric floating point), and bool (boolean values, True and False).

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

# print(new_arr[1,2]) #2. satır, 3. sütunda ki eleman>> tek eleman seçme>>x-y koordinatı belirtme gibi
# print(new_arr[0,20]) #1. satır, 21. sütunda ki eleman

# print(new_arr[1,2]) #2. satır, 3. sütunda ki eleman>> tek eleman seçme>>x-y koordinatı belirtme gibi
# print(new_arr[0,20]) #1. satır, 21. sütunda ki eleman


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
# #1. indeksli satırın tamammını (2. satır) seçer. 2 ve 3. indekste satır olmadığından onları atlar ve hata vermez.


# print(heights_and_ages_arr[0,:])
# #heights_and_ages_arr[0, :]
# # 0 → 0. satırı seçer.
# # : → Tüm sütunları seçer.
# # Açık ve standart bir NumPy dizisi dilimleme yöntemidir.

# # heights_and_ages_arr[0,]
# # Python'da sondaki virgül gereksizdir ve yokmuş gibi davranılır.
# # Yani heights_and_ages_arr[0] ile aynıdır.

# # heights_and_ages_arr[0]
# # NumPy'de tek bir indeksle erişildiğinde, varsayılan olarak tüm sütunlar seçilir.
# # Yani heights_and_ages_arr[0, :] ile aynıdır.


# arr = np.array([10, 20, 30, 40, 50, 60, 70])
# print("Array:", arr) #Array: [10 20 30 40 50 60 70]

# print(arr[1:4])  # [20 30 40]
# # Tek boyutlu dizilerde (1D), NumPy satır veya sütun ayrımı yapmaz, sadece indeks aralığını alır.
# # İki boyutlu dizilerde (2D), satır-sütun seçimi yapabilirsiniz.
# # Eğer satır-sütun ayrımı yapmak istiyorsanız, 2D bir NumPy dizisi kullanmalısınız.

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


