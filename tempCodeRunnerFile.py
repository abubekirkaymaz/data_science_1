import numpy as np

"""
heights = [189, 170, 189, 163, 183, 171, 185, 168, 173, 183, 173, 173, 175, 178, 183, 193, 178, 173, 174, 183, 183, 180, 168, 180, 170, 178, 182, 180, 183, 178, 182, 188, 175, 179, 183, 193, 182, 183, 177, 185, 188, 188, 182, 185, 191]

ages = [57, 61, 57, 57, 58, 57, 61, 54, 68, 51, 49, 64, 50, 48, 65, 52, 56, 46, 54, 49, 51, 47, 55, 55, 54, 42, 51, 56, 55, 51, 54, 51, 60, 62, 43, 55, 56, 61, 52, 69, 64, 46, 54, 47, 70]


heights_ages = heights + ages

#print(heights_ages)

heights_ages_arr = np.array(heights_ages)

#print(heights_ages_arr)

#print(type(heights_ages_arr))
#print(type(heights_ages))


#print(heights_ages_arr.shape)
#print(heights_ages_arr.shape)

reshape_arr = heights_ages_arr.reshape(5, -1)
print(reshape_arr)
#print(heights_ages_arr)

#print(heights_ages_arr.dtype)

#print(heights_ages_arr.shape)

#print(reshape_arr.shape)

#lst_1 = [20, 30, 60.5]

#lst_arr = np.array(lst_1)

#print(lst_arr)

#print(lst_arr.dtype)

#lst_2 = ['False', 'True', '10']

#lst_2_arr = np.array(lst_2)

#print(lst_2_arr.dtype)

#print(reshape_arr[0, 1])

#print(heights_ages_arr[0])

#item = slice(reshape_arr[:])
#print(item)


#print(reshape_arr[3,])
#print(reshape_arr[3,:])

#print(reshape_arr[0:3, :]) # tümünü seçmek istiyorsak ya boş birakilacak [0:3,], ya da boş : işareti koyulacak [0:3, :]
#print(reshape_arr[0:3,])

#print(reshape_arr[, 0:3]) #bu işlem hata verir, çünkü satir tarafi yani virgülün solu için bir belirtme yapilmasi gerekir.
#print(reshape_arr[:, 0:3]) #doğru kullanim bu şekilde. Virgülün solu boş birakilmaz.

#print(reshape_arr[0,0]) #doğru kullanim bu şekilde. Virgülün solu boş birakilmaz.

#x = reshape_arr[0,0]

#print(type(x)) #<class 'numpy.int64'>
#print(type(reshape_arr[:, 0:3])) #<class 'numpy.ndarray'>

print(reshape_arr[0:1, 0:3]) #satir dilimlemesi yapildiği için sonuç bir 2D dizi olur.
print(reshape_arr[0, 0:3])  #doğrudan satir seçildiği için, sonuç bir 1D dizi olur.
"""


"""
heights = [189, 170, 189, 163, 183, 171, 185, 168, 173, 183, 173, 173, 175, 178, 183, 193, 178, 173, 174, 183, 183, 180, 168, 180, 170, 178, 182, 180, 183, 178, 182, 188, 175, 179, 183, 193, 182, 183, 177, 185, 188, 188, 182, 185, 191]

ages = [57, 61, 57, 57, 58, 57, 61, 54, 68, 51, 49, 64, 50, 48, 65, 52, 56, 46, 54, 49, 51, 47, 55, 55, 54, 42, 51, 56, 55, 51, 54, 51, 60, 62, 43, 55, 56, 61, 52, 69, 64, 46, 54, 47, 70]


heights_ages = heights + ages
# print(heights_ages)

heights_ages_arr = np.array(heights_ages)

# print(type(heights_ages_arr))
# print(heights_ages_arr.size)
# print(heights_ages_arr.shape)

heights_ages_arr = heights_ages_arr.reshape(5, -1)
# print(heights_ages_arr.size)
# print(heights_ages_arr.shape)

# print(heights_ages_arr)

# heights_ages_arr[0:5, 0 ] = [1, 2, 3, 4, 5]

# print(heights_ages_arr)


# heights_ages_arr [2, 7:10] = [1, 2, 3] 
# print(heights_ages_arr)



# heights_ages_arr [0:2, 0:3] = [[10, 20, 30],[11,12,13]] #belirtilen dilime dilime uyacak bir listede ki verileri yerleştir.

# print(heights_ages_arr)


#heights_ages_arr [:, 7] = [1, 2, 3, 4, 5] # tüm satırların 7. indeksinde ki verileri atanan değerler ile değiştir




# print(heights_ages_arr[0,0]) #189 >>skaler değer
# print(heights_ages_arr[0:1,0:1]) #[[189]] >> bir NumPy dizisi

"""

"""
heights = [189, 170, 189, 163, 183, 171, 185, 168, 173, 183, 173, 173, 175, 178, 183, 193, 178, 173, 174, 183, 183, 180, 168, 180, 170, 178, 182, 180, 183, 178, 182, 188, 175, 179, 183, 193, 182, 183, 177, 185, 188, 188, 182, 185, 191]

ages = [57, 61, 57, 57, 58, 57, 61, 54, 68, 51, 49, 64, 50, 48, 65, 52, 56, 46, 54, 49, 51, 47, 55, 55, 54, 42, 51, 56, 55, 51, 54, 51, 60, 62, 43, 55, 56, 61, 52, 69, 64, 46, 54, 47, 70]

heights_arr = np.array(heights)
ages_arr = np.array(ages)

# print(type(heights_arr), ", " , type(ages_arr))
# print(heights_arr.size, ", " , ages_arr.size)
# print(heights_arr.shape, ", " , ages_arr.shape)

heights_arr_1 = heights_arr.reshape(5, -1)

ages_arr_1 = ages_arr.reshape(5, -1)

print("......................................................................")
print(heights_arr_1)
print("......................................................................")
print(ages_arr_1)
print("......................................................................")

height_age_arr_1 = np.vstack((heights_arr_1, ages_arr_1))
print(height_age_arr_1)

"""
"""
heights = [189, 170, 189, 163, 183, 171, 185, 168, 173, 183, 173, 173, 175, 178, 183, 193, 178, 173, 174, 183, 183, 180, 168, 180, 170, 178, 182, 180, 183, 178, 182, 188, 175, 179, 183, 193, 182, 183, 177, 185, 188, 188, 182, 185, 191]

ages = [57, 61, 57, 57, 58, 57, 61, 54, 68, 51, 49, 64, 50, 48, 65, 52, 56, 46, 54, 49, 51, 47, 55, 55, 54, 42, 51, 56, 55, 51, 54, 51, 60, 62, 43]

heights_arr  = np.array(heights)
ages_arr = np.array(ages)

# print(heights_arr)
# print(ages_arr)

# print(heights_arr.size)
# print(ages_arr.size)



# print(heights_arr.shape)
# print(ages_arr.shape)

# ages_arr_15 = ages_arr.reshape(-1, 5)
# heights_arr_15 = heights_arr.reshape(-1, 5)

# print(ages_arr_15)
# print(heights_arr_15)

# heights_ages_arr = np.vstack((heights_arr_15, ages_arr_15)) #vstack için sütun sayıları eşit olacak
# print(heights_ages_arr)
 

# ages_arr_51 = ages_arr.reshape(5, -1)
# heights_arr_51 = heights_arr.reshape(5, -1)

# #heights_ages_arr__ = np.hstack((heights_arr_51, ages_arr_51)) 



# heights_ages_arr__ = np.concatenate((ages_arr_51, heights_arr_51), axis=1)

# print(heights_ages_arr__)



ages_arr_51 = ages_arr.reshape(-1, 5)
heights_arr_51 = heights_arr.reshape(-1, 5)

heights_ages_arr__ = np.concatenate((ages_arr_51, heights_arr_51), axis=0)

print(heights_ages_arr__)

#vstack ve axis = 0 dikey, alt alta birleştirme, Sütun sayıları aynı olmalı
#hstack ve axis = 1 yatay, yan yana birleştirme. Satır sayıları aynı olmalı
"""


#Indexing
# Slicing
#2D Numpy Array'de Slicing
#Assigning Single Values
#Assigning an Array to an Array

#-----------------------------------------------------------------------------------------------------------------------------------#
#Mathematical Operations on Arrays
"""
# heights_arr = np.array([189, 170, 189, 163, 183, 171, 185, 168, 173, 183, 173, 173, 175, 178, 183, 193, 178, 173, 174, 183, 183, 180, 168, 180, 170, 178, 182, 180, 183, 178, 182, 188, 175, 179, 183, 193, 182, 183, 177, 185, 188, 188, 182, 185, 191])
# ages_arr = np.array([57, 61, 57, 57, 58, 57, 61, 54, 68, 51, 49, 64, 50, 48, 65, 52, 56, 46, 54, 49, 51, 47, 55, 55, 54, 42, 51, 56, 55, 51, 54, 51, 60, 62, 43, 55, 56, 61, 52, 69, 64, 46, 54, 47, 70]).reshape((-1,1))

# heights_arr = heights_arr.reshape((45,1))

# print("---------------------------")
# print(heights_arr)
# print("---------------------------")
# print(ages_arr)
# print("---------------------------")


#vstack ve axis = 0 dikey, alt alta birleştirme, Sütun sayıları aynı olmalı
#hstack ve axis = 1 yatay, yan yana birleştirme. Satır sayıları aynı olmalı

# heights_ages_arr = np.hstack((heights_arr, ages_arr))
# heights_ages_arr = np.concatenate((heights_arr, ages_arr), axis=1)

# print(heights_ages_arr)
# print("---------------------------")
# print(heights_ages_arr[0])


# print(heights_ages_arr[:, 0] * 0.0328084)

# lst_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# lst_2 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]

# lst_1_arr = np.array(lst_1)
# lst_2_arr = np.array(lst_2)

# print(lst_1_arr.shape)
# print(lst_2_arr.shape)

# lst_2_arr = lst_2_arr.reshape(3, 4)
#print(lst_2_arr)

# lst_1_arr = lst_1_arr.reshape(3, 4)
#print(lst_1_arr)

#lst_arr = np.vstack((lst_1_arr, lst_2_arr))
# lst_arr = np.concatenate((lst_1_arr, lst_2_arr), axis=0)
#print(lst_arr.shape) # (6,4)

# print(lst_arr[0:2, 0:2].sum()) #dizi diliminin tüm elemanlarının toplamını verir ==> 14 (1+2+5+6)
# print(lst_arr.sum()) #tüm elemanların toplamını verir ==> 858

# print (lst_arr.sum(axis=0)) #sütunların tek tek toplamalrını verir.==> [165 198 231 264]
# print (lst_arr.sum(axis=1)) #satırların tek tek toplamlarını verir ==> [ 10  26  42 100 260 420]

# print ((lst_arr.sum(axis=0)).shape) #1d boyutlu bir vektör çıktı verir ==> (4,)
# print(lst_arr.sum(axis=0, keepdims=True).shape) # 2d boyultlu bir matris çıktı verir. ==> (1,4)

# print(lst_arr.min()) #1
# print(lst_arr.max()) #120
# print(lst_arr.mean()) #35.75 ==> print((lst_arr.sum())/lst_arr.size)

# print(lst_arr[0:2, : ].min()) #dizide ki bir dilim üzerinde işlem yapabilir
# print(lst_arr[0:2, : ].max()) #dizide ki bir dilim üzerinde işlem yapabilir
# print(lst_arr[0:2, : ].mean()) #dizide ki bir dilim üzerinde işlem yapabilir

# print(lst_arr)
# print(".............................")
# print(lst_arr[4].min()) #dizinin 5. satırının min değerini verir
# print(lst_arr[1, 2].max()) #mantıksız. çünkü zaten tek bir elemanı seçip onun max değerini alıyorum.

#print(lst_arr[0,:] + 1) #matematiksel işlem sonucunda esas dizeden farklı bir dize döner [  1   2   3   4] ==> [2 3 4 5] 
# print((lst_arr[0:2, 1:4] * 2).shape)
"""

#-----------------------------------------------------------------------------------------------------------------------------------#
#Comparisons
"""
lst_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
lst_2 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]

lst_1_arr = np.array(lst_1)
lst_2_arr = np.array(lst_2)
lst_arr = np.hstack((lst_1_arr, lst_2_arr))

lst_arr_46 = lst_arr.reshape(4,-1)
print(lst_arr_46)

print(lst_arr_46[0:2, 3:6] > 5) #seçilen dilimi kontrol eder ve dilim ve seçilen boyut formatında true, false verilerini gösterir.
print((lst_arr_46[0:2, 3:6] > 5).sum()) # true = 1, false=0 olarak alır ve toplamlarını verir. Toplam dört adet true mevcut.
"""

#-----------------------------------------------------------------------------------------------------------------------------------#
#Mask & Subsetting

"""
heights = [189, 170, 189, 163, 183, 171, 185, 168, 173, 183, 173, 173, 175, 178, 183, 193, 178, 173, 174, 183, 183, 180, 168, 180, 170, 178, 182, 180, 183, 178, 182, 188, 175, 179, 183, 193, 182, 183, 177, 185, 188, 188, 182, 185, 191]

ages = [57, 61, 57, 57, 58, 57, 61, 54, 68, 51, 49, 64, 50, 48, 65, 52, 56, 46, 54, 49, 51, 47, 55, 55, 54, 42, 51, 56, 55, 51, 54, 51, 60, 62, 43, 55, 56, 61, 52, 69, 64, 46, 54, 47, 70]

heights_ages = heights + ages
heights_ages_arr = np.array(heights_ages)

# print(heights_ages_arr.shape)

# print(heights_ages_arr)

new_arr = heights_ages_arr.reshape(2, -1).T

# print(new_arr)

mask = new_arr[:, 0] >= 180 # ilk sütunda 180 den büyük ve eşit olan değerler için bir mask değişkeni tanımladık

# print(mask.shape)

# print(new_arr[mask,]) #esas dizimizde bu mask değişkeninin tuttuğu değerleri tüm satırlara uyguladığımızda koşulu sağlayan değerler listelenir.

arr = np.array([
    [10,  20,  30,  40,  50],   # 0. satır
    [60,  70,  80,  90, 100]    # 1. satır
])

mask = arr[1, :] > 80
# print(mask) #[False False False  True  True]

filtered_arr = arr[:, mask]
# print(filtered_arr)

lst_1 = []
for i in range(20, 40, 2):
  lst_1.append(i)

# print(lst_1)

lst_2 =[]
for i in range(6, 34, 3):
  lst_2.append(i)

# print(lst_2)

lst_3 = []
for i in range(20, 30):
  lst_3.append(i)

# print(lst_3)

lst1 = np.array(lst_1).reshape(-1,1)
lst2 = np.array(lst_2).reshape(-1,1)
lst3 = np.array(lst_3).reshape(-1,1)

lst = np.hstack((lst1, lst2, lst3))

print(lst)

mask = lst[:, 1] % 2 == 0

print(lst[mask])
"""

#-----------------------------------------------------------------------------------------------------------------------------------#
#Multiple Criteria
"""
heights_arr = np.array([189, 170, 189, 163, 183, 171, 185, 168, 173, 183, 173, 173, 175, 178, 183, 193, 178, 173, 174, 183, 183, 180, 168, 180, 170, 178, 182, 180, 183, 178, 182, 188, 175, 179, 183, 193, 182, 183, 177, 185, 188, 188, 182, 185, 191])
ages_arr = np.array([57, 61, 57, 57, 58, 57, 61, 54, 68, 51, 49, 64, 50, 48, 65, 52, 56, 46, 54, 49, 51, 47, 55, 55, 54, 42, 51, 56, 55, 51, 54, 51, 60, 62, 43, 55, 56, 61, 52, 69, 64, 46, 54, 47, 70]).reshape((-1,1))

heights_arr = heights_arr.reshape((45,1))
height_age_arr = np.hstack((heights_arr, ages_arr))

mask = (height_age_arr[:, 0]>=182) & (height_age_arr[:,1]<=50)

print(height_age_arr)
print("---------------------------------------------------")
print(height_age_arr[mask,])
"""
#Bir NumPy array’i oluştur ve sadece pozitif olan elemanları seçerek yeni bir array oluştur.
arr = np.array([-3, 7, -1, 4, -9, 10, 0, -2])  
print(arr)
print("---------------------------------------------------")
mask = arr > 0
print(arr[mask])

#Aşağıdaki array’den 10 ile 30 arasındaki (10 ve 30 dahil) sayıları seç ve yeni bir array oluştur.
arr = np.array([5, 12, 25, 30, 7, 40, 15, 28, 35])  

mask = (arr >= 10) & (arr <= 30)
print(arr[mask])

#Aşağıdaki array’de tek sayıları -1 ile değiştir.
arr = np.array([4, 9, 12, 15, 22, 33, 42])

mask = arr % 2 != 0  
arr[mask] = -1  
print(arr)

#Aşağıdaki array içinden sadece 2 veya 5 ile tam bölünebilen sayıları içeren yeni bir array oluştur.
arr = np.array([10, 17, 22, 25, 30, 37, 40, 45])  

mask = (arr % 2 == 0) & (arr % 5 == 0)
print(arr[mask])

#Aşağıdaki NumPy array'inde NaN (Not a Number) değerlerini maskele ve sadece geçerli sayıları içeren bir array oluştur.
arr = np.array([3.4, np.nan, 5.6, np.nan, 7.8, 10.2])

mask = ~np.isnan(arr)  # NaN olmayanları seçmek için tersleme (~) kullanılır

new_arr = arr[mask]
print(new_arr)

#Aşağıdaki dizide, 10'dan küçük olan elemanları seçin:
arr = np.array([2, 8, 12, 5, 20, 7, 15])

mask = arr < 10
print(arr[mask])


# Burada pozitif sayıları içeren yeni bir array oluştur.

#-----------------------------------------------------------------------------------------------------------------------------------#
#Concatenate & Combine
#-----------------------------------------------------------------------------------------------------------------------------------#
