import numpy as np

"""
#1-the first step in data science is to transform it into arrays of numbers.

heights = [189, 170, 189, 163, 183, 171, 185, 168, 173, 183, 173, 173, 175, 178, 183, 193, 178, 173, 174, 183, 183, 180, 168, 180, 170, 178, 182, 180, 183, 178, 182, 188, 175, 179, 183, 193, 182, 183, 177, 185, 188, 188, 182, 185, 191]

ages = [57, 61, 57, 57, 58, 57, 61, 54, 68, 51, 49, 64, 50, 48, 65, 52, 56, 46, 54, 49, 51, 47, 55, 55, 54, 42, 51, 56, 55, 51, 54, 51, 60, 62, 43, 55, 56, 61, 52, 69, 64, 46, 54, 47, 70]

heights_ages = heights + ages #>> iki listeyi tek liste haline getirir.

heights_ages_arr = np.array(heights_ages) #np array tipine çevirir
#Note that once an array is created in numpy, its size cannot be changed.
#Size tells us how big the array is, shape tells us the dimension.
#The output is a tuple, recall that the built-in data type tuple is immutable whereas a list is mutable

#print(heights_ages_arr)

#print(heights_ages_arr.dtype) #int64 >> 64 bitsize integer

#print(heights_ages_arr.size) #90 >> dizenin 90 adet elemanı var

#print(heights_ages_arr.shape) #(90,)
#np.array bir fonksiyondur, yani bir şeyler yapar (listeyi Numpy dizisine dönüştürmek gibi).
#ndarray.size ise bir özelliktir, yani mevcut bir Numpy dizisi hakkında bilgi verir (eleman sayısını döndürmek gibi).


#print(heights_ages_arr.reshape(-1,9).shape) #(10, 9)

#print(heights_ages_arr.reshape(-1,9).size) #90 >> reshape yapılsa da eleman sayısı değişmez: 90

#2-Another characteristic about numpy array is that it is homogeneous, meaning each element must be of the same data type.

lst_1 = [10, 30, 50]
lst_arr = np.array(lst_1)

print(lst_arr)
print(lst_arr.size)
print(lst_arr.shape)
print(lst_arr.dtype) #int64
  
lst_2 = [10.50 , 30, 50] #dize de bir adet float veri varsa np dizenin tümünü float yapar
lst_arr_2 = np.array(lst_2)
print(lst_arr_2)
print(lst_arr_2.dtype) #float64

#Numpy supports several data types such as int (integer), float (numeric floating point), and bool (boolean values, True and False). 

"""
"""
#Indexing

heights = [189, 170, 189, 163, 183, 171, 185, 168, 173, 183, 173, 173, 175, 178, 183, 193, 178, 173, 174, 183, 183, 180, 168, 180, 170, 178, 182, 180, 183, 178, 182, 188, 175, 179, 183, 193, 182, 183, 177, 185, 188, 188, 182, 185, 191]

ages = [57, 61, 57, 57, 58, 57, 61, 54, 68, 51, 49, 64, 50, 48, 65, 52, 56, 46, 54, 49, 51, 47, 55, 55, 54, 42, 51, 56, 55, 51, 54, 51, 60, 62, 43, 55, 56, 61, 52, 69, 64, 46, 54, 47, 70]

heights_ages = heights + ages
heights_ages_arr = np.array(heights_ages)

print(heights_ages_arr.shape)

new_arr = heights_ages_arr.reshape(2, -1)

print(new_arr)

print(new_arr[0,0]) # first row, first column

#Axis 0 (↓): Yukarıdan aşağıya gider, satırlar boyunca işler.
#Axis 1 (→): Soldan sağa gider, sütunlar boyunca işler.

"""
"""
# Slicing
# What if we want to inspect the first three elements from the first row in a 2darray? 
# We use ":" to select all the elements from the index up to but not including the ending index. This is called slicing.

heights = [189, 170, 189, 163, 183, 171, 185, 168, 173, 183, 173, 173, 175, 178, 183, 193, 178, 173, 174, 183, 183, 180, 168, 180, 170, 178, 182, 180, 183, 178, 182, 188, 175, 179, 183, 193, 182, 183, 177, 185, 188, 188, 182, 185, 191]

ages = [57, 61, 57, 57, 58, 57, 61, 54, 68, 51, 49, 64, 50, 48, 65, 52, 56, 46, 54, 49, 51, 47, 55, 55, 54, 42, 51, 56, 55, 51, 54, 51, 60, 62, 43, 55, 56, 61, 52, 69, 64, 46, 54, 47, 70]

heights_and_ages = heights + ages
heights_and_ages_arr = np.array(heights_and_ages)
heights_and_ages_arr = heights_and_ages_arr.reshape((2,45))
print(heights_and_ages_arr[0, 0:3]) #ilk satırın ilk 3 kaydı. 0:3 >> birinci değer (0) dahil, ikinci değer (3) dahil değil.
print(heights_and_ages_arr[0, :3]) # ,:3 de başlangıç değeri 0 ise ihmal edilebilir.>>When the starting index is 0, we can omit it
print(heights_and_ages_arr[0, 9:]) # ,9: de index 9 (10. değer) dan (dahil) satırın sonuna kadar alır

print(heights_and_ages_arr)
print(heights_and_ages_arr[:, 3]) # 4. sütunun tamamını alır(index 3)

##Numpy Slicing Sözdizimi:
#start: Dilimleme işleminin başlangıç indeksini belirtir (varsayılan: 0).
#stop: Dilimlemenin nerede duracağını belirtir (bu indeks dahil edilmez) (varsayılan: boyutun sonu).
#step: Dilimleme işleminin adım boyutunu belirtir (varsayılan: 1).
#Sözdizimi: array[start:stop:step]

arr = np.array([10, 20, 30, 40, 50, 60, 70])
print("Array:", arr) #Array: [10 20 30 40 50 60 70]

print(arr[1:4])  # [20 30 40]
#Başlangıç (start): 1 (İndeks 1'den başla, yani 20'den).
#Bitiş (stop): 4 (İndeks 4'e kadar, yani 50'ye kadar; 50 dahil değil).
#Adım (step): Varsayılan olarak 1.

print(arr[:4])  # [10 20 30 40]
#Başlangıç: Varsayılan olarak 0 (ilk elemandan başla).
#Bitiş: 4 (İndeks 4'e kadar).
#Adım: Varsayılan olarak 1.

print(arr[::2])  # [10 30 50 70]
#Başlangıç: Varsayılan olarak 0.
#Bitiş: Varsayılan olarak dizinin sonuna kadar.
#Adım: 2 (Her 2. elemanı al).

print(arr[-3:])  # [50 60 70]
#Başlangıç: Sondan 3. elemandan (50) başla.
#Bitiş: Varsayılan olarak dizinin sonuna kadar.
#Adım: Varsayılan olarak 1.

print(arr[::-1])
#Başlangıç: Varsayılan olarak dizinin sonundan başla.
#Bitiş: Varsayılan olarak dizinin başına kadar git.
#Adım: -1 (Diziyi ters çevir).

print(arr[-1:4:-1]) #[70 60]
#Başlangıç: Dizinin sonundan başla.
#Bitiş: Dördüncü indekse kadar git
#Adım: -1 Dizenin sonundan dördüncü indekse doğru git.
"""

#2D Numpy Array'de Slicing
arr_2d = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
])
print("2D Array:\n", arr_2d)

print(arr_2d[1:, 2:])
# [[ 7  8]
#  [11 12]]
#Satırlar (axis 0): 1: (1. satırdan başla, sonuna kadar al).
#Sütunlar (axis 1): 2: (2. sütundan başla, sonuna kadar al).

print(arr_2d[:, ::2])
# [[ 1  3]
#  [ 5  7]
#  [ 9 11]]
#Satırlar (axis 0): : (tüm satırları al).
#Sütunlar (axis 1): ::2 (Her 2. sütunu al).