import numpy as np


#2D Numpy Array'de Slicing
"""
arr_2d = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
])
print("2D Array:\n", arr_2d)

print(arr_2d[1:, 2:])
# [[ 7  8]
#  [11 12]]
#Satirlar (axis 0): 1: (1. satirdan başla, sonuna kadar al).
#Sütunlar (axis 1): 2: (2. sütundan başla, sonuna kadar al).

print(arr_2d[:, ::2])
# [[ 1  3]
#  [ 5  7]
#  [ 9 11]]
#Satirlar (axis 0): : (tüm satirlari al).
#Sütunlar (axis 1): ::2 (Her 2. sütunu al).
"""


#Assigning Single Values
"""
import numpy as np

heights = [189, 170, 189, 163, 183, 171, 185, 168, 173, 183, 173, 173, 175, 178, 183, 193, 178, 173, 174, 183, 183, 180, 168, 180, 170, 178, 182, 180, 183, 178, 182, 188, 175, 179, 183, 193, 182, 183, 177, 185, 188, 188, 182, 185, 191]

heights_arr = np.array(heights)
heights_arr[3] = 165 #3. indexdeki veri olan 163 >> 165 olarak değiştirildi
print(heights_arr) 

"""
"""
import numpy as np

heights = [189, 170, 189, 163, 183, 171, 185, 168, 173, 183, 173, 173, 175, 178, 183, 193, 178, 173, 174, 183, 183, 180, 168, 180, 170, 178, 182, 180, 183, 178, 182, 188, 175, 179, 183, 193, 182, 183, 177, 185, 188, 188, 182, 185, 191]

ages = [57, 61, 57, 57, 58, 57, 61, 54, 68, 51, 49, 64, 50, 48, 65, 52, 56, 46, 54, 49, 51, 47, 55, 55, 54, 42, 51, 56, 55, 51, 54, 51, 60, 62, 43, 55, 56, 61, 52, 69, 64, 46, 54, 47, 70]

heights_and_ages = heights + ages 
heights_and_ages_arr = np.array(heights_and_ages)
heights_and_ages_arr = heights_and_ages_arr.reshape((2,45))
#print(heights_and_ages_arr)
#heights_and_ages_arr[0, 3] = 165 #İlk satirin 3. indexinde ki 163 >>> 165 olarak değişti
#print(heights_and_ages_arr)

#heights_and_ages_arr[0,:] = 180 # ilk satirin tüm verileri (:) 180 olarak değişti
#print(heights_and_ages_arr)

heights_and_ages_arr[:2, :5] = 0 #ilk iki satirin ilk beş verisi 0 ile değiştirildi
print(heights_and_ages_arr)
"""

#Assigning an Array to an Array
"""
#In addition, a 1darray or a 2darry can be assigned to a subset of another 2darray, as long as their shapes match.

import numpy as np

heights = [189, 170, 189, 163, 183, 171, 185, 168, 173, 183, 173, 173, 175, 178, 183, 193, 178, 173, 174, 183, 183, 180, 168, 180, 170, 178, 182, 180, 183, 178, 182, 188, 175, 179, 183, 193, 182, 183, 177, 185, 188, 188, 182, 185, 191]

ages = [57, 61, 57, 57, 58, 57, 61, 54, 68, 51, 49, 64, 50, 48, 65, 52, 56, 46, 54, 49, 51, 47, 55, 55, 54, 42, 51, 56, 55, 51, 54, 51, 60, 62, 43, 55, 56, 61, 52, 69, 64, 46, 54, 47, 70]

heights_and_ages = heights + ages
heights_and_ages_arr = np.array(heights_and_ages)
heights_and_ages_arr = heights_and_ages_arr.reshape((2,45))
print(heights_and_ages_arr)
heights_and_ages_arr[:, 0:5] = [0, 11, 22, 33, 44]  #tüm satirlarin ilk beş verisine yeni değerler atandi
print(heights_and_ages_arr)

"""
"""
import numpy as np

heights = [189, 170, 189, 163, 183, 171, 185, 168, 173, 183, 173, 173, 175, 178, 183, 193, 178, 173, 174, 183, 183, 180, 168, 180, 170, 178, 182, 180, 183, 178, 182, 188, 175, 179, 183, 193, 182, 183, 177, 185, 188, 188, 182, 185, 191]

ages = [57, 61, 57, 57, 58, 57, 61, 54, 68, 51, 49, 64, 50, 48, 65, 52, 56, 46, 54, 49, 51, 47, 55, 55, 54, 42, 51, 56, 55, 51, 54, 51, 60, 62, 43, 55, 56, 61, 52, 69, 64, 46, 54, 47, 70]

heights_and_ages = heights + ages
heights_and_ages_arr = np.array(heights_and_ages)
heights_and_ages_arr = heights_and_ages_arr.reshape((2,45))

#new_record = np.array([[180, 183, 190], [54, 50, 69]])
#heights_and_ages_arr[:, 42:] = new_record

heights_and_ages_arr[:, 42:] = [[180, 183, 190], [54, 50, 69]] #tüm satirlarin son üç indisine farkli veriler atandi
print(heights_and_ages_arr)

print(heights_and_ages_arr.size)
"""


#Combining Two Arrays
"""
import numpy as np

ages = [57, 61, 57, 57, 58, 57, 61, 54, 68, 51, 49, 64, 50, 48, 65, 52, 56, 46, 54, 49, 51, 47, 55, 55, 54, 42, 51, 56, 55, 51, 54, 51, 60, 62, 43, 55, 56, 61, 52, 69, 64, 46, 54, 47, 70]

ages_arr = np.array(ages)

print(ages_arr.shape) # (45,)
print(ages_arr[:3,]) #[57 61 57]
"""
"""
import numpy as np

heights = [189, 170, 189, 163, 183, 171, 185, 168, 173, 183, 173, 173, 175, 178, 183, 193, 178, 173, 174, 183, 183, 180, 168, 180, 170, 178, 182, 180, 183, 178, 182, 188, 175, 179, 183, 193, 182, 183, 177, 185, 188, 188, 182, 185, 191]
ages = [57, 61, 57, 57, 58, 57, 61, 54, 68, 51, 49, 64, 50, 48, 65, 52, 56, 46, 54, 49, 51, 47, 55, 55, 54, 42, 51, 56, 55, 51, 54, 51, 60, 62, 43, 55, 56, 61, 52, 69, 64, 46, 54, 47, 70]

heights_arr = np.array(heights)
ages_arr = np.array(ages)

heights_arr = heights_arr.reshape((45,1)) #45 satir ve 1 sütundan oluşan bir sütun vektörüne dönüşür
ages_arr = ages_arr.reshape((45,1)) #45 satir ve 1 sütundan oluşan bir sütun vektörüne dönüşür

#height_age_arr = np.hstack((heights_arr, ages_arr)) # İki sütun vektörünü yan yana birleştirme
height_age_arr = np.vstack((heights_arr, ages_arr)) #iki sütun vektörünü uç uca ekler ve (90,1) şeklini alir

print(height_age_arr.shape)
print(height_age_arr[:,:]) #tüm sütunlardaki ilk 5 satiri verir

"""


#To combine more than two arrays horizontally, simply add the additional arrays into the tuple.
"""
import numpy as np

# Örnek sütun vektörleri
heights = np.array([[150], [160], [170]])
ages = np.array([[25], [30], [35]])
weights = np.array([[60], [70], [80]])

# Yatay birleştirme
combined = np.hstack((heights, ages, weights))
#You can use np.hstack to concatenate arrays ONLY if they have the same number of rows.

print(combined)
"""

"""
#Concatenate
#More generally, we can use the function numpy.concatenate. If we want to concatenate, link together, two arrays along rows, then pass 'axis = 1' to achieve the same result as using numpy.hstack; and pass 'axis = 0' if you want to combine arrays vertically.

import numpy as np

heights = [189, 170, 189, 163, 183, 171, 185, 168, 173, 183, 173, 173, 175, 178, 183, 193, 178, 173, 174, 183, 183, 180, 168, 180, 170, 178, 182, 180, 183, 178, 182, 188, 175, 179, 183, 193, 182, 183, 177, 185, 188, 188, 182, 185, 191]
ages = [57, 61, 57, 57, 58, 57, 61, 54, 68, 51, 49, 64, 50, 48, 65, 52, 56, 46, 54, 49, 51, 47, 55, 55, 54, 42, 51, 56, 55, 51, 54, 51, 60, 62, 43, 55, 56, 61, 52, 69, 64, 46, 54, 47, 70]

heights_arr = np.array(heights)
ages_arr = np.array(ages)

heights_arr = heights_arr.reshape((45,1))
ages_arr = ages_arr.reshape((45,1))

# height_age_arr = np.hstack((heights_arr, ages_arr))
height_age_arr = np.concatenate((heights_arr, ages_arr), axis=1) 

print(height_age_arr.shape) #(45, 2)
print(height_age_arr[:3,:])

"""



#Mathematical Operations on Arrays
"""
import numpy as np

heights_arr = np.array([189, 170, 189, 163, 183, 171, 185, 168, 173, 183, 173, 173, 175, 178, 183, 193, 178, 173, 174, 183, 183, 180, 168, 180, 170, 178, 182, 180, 183, 178, 182, 188, 175, 179, 183, 193, 182, 183, 177, 185, 188, 188, 182, 185, 191])
ages_arr = np.array([57, 61, 57, 57, 58, 57, 61, 54, 68, 51, 49, 64, 50, 48, 65, 52, 56, 46, 54, 49, 51, 47, 55, 55, 54, 42, 51, 56, 55, 51, 54, 51, 60, 62, 43, 55, 56, 61, 52, 69, 64, 46, 54, 47, 70]).reshape((-1,1))

heights_arr = heights_arr.reshape((45,1))
height_age_arr = np.hstack((heights_arr, ages_arr))

print(height_age_arr[:,0]*0.0328084)

#Now we have all heights in feet. Note that this operation won’t change the original array, it returns a new 1darray where 0.0328084 has been multiplied to each element in the first column of 'heights_age_arr'.

#Numpy Array Method
print(height_age_arr.sum()) 
print(height_age_arr.sum(axis=0))  #[8100 2475] >> sütunlar toplamlari
print(height_age_arr.sum(axis=1)) #satirlar toplamlari

#Other operations, such as .min(), .max(), .mean(), work in a similar way to .sum().
"""

#Comparisons
"""
import numpy as np

heights_arr = np.array([189, 170, 189, 163, 183, 171, 185, 168, 173, 183, 173, 173, 175, 178, 183, 193, 178, 173, 174, 183, 183, 180, 168, 180, 170, 178, 182, 180, 183, 178, 182, 188, 175, 179, 183, 193, 182, 183, 177, 185, 188, 188, 182, 185, 191])
ages_arr = np.array([57, 61, 57, 57, 58, 57, 61, 54, 68, 51, 49, 64, 50, 48, 65, 52, 56, 46, 54, 49, 51, 47, 55, 55, 54, 42, 51, 56, 55, 51, 54, 51, 60, 62, 43, 55, 56, 61, 52, 69, 64, 46, 54, 47, 70]).reshape((-1,1))

heights_arr = heights_arr.reshape((45,1))
height_age_arr = np.hstack((heights_arr, ages_arr))

print(height_age_arr[:, 1] < 55)
print(height_age_arr[:, 1] == 51)
print((height_age_arr[:, 1] == 51).sum()) #True is treated as 1 and False as 0 in the sum.
"""


#Mask & Subsetting
"""
import numpy as np

heights_arr = np.array([189, 170, 189, 163, 183, 171, 185, 168, 173, 183, 173, 173, 175, 178, 183, 193, 178, 173, 174, 183, 183, 180, 168, 180, 170, 178, 182, 180, 183, 178, 182, 188, 175, 179, 183, 193, 182, 183, 177, 185, 188, 188, 182, 185, 191])
heights_arr = heights_arr.reshape((45,1))

#ages_arr = np.array([57, 61, 57, 57, 58, 57, 61, 54, 68, 51, 49, 64, 50, 48, 65, 52, 56, 46, 54, 49, 51, 47, 55, 55, 54, 42, 51, 56, 55, 51, 54, 51, 60, 62, 43, 55, 56, 61, 52, 69, 64, 46, 54, 47, 70]).reshape((-1,1))
ages_arr = np.array([57, 61, 57, 57, 58, 57, 61, 54, 68, 51, 49, 64, 50, 48, 65, 52, 56, 46, 54, 49, 51, 47, 55, 55, 54, 42, 51, 56, 55, 51, 54, 51, 60, 62, 43, 55, 56, 61, 52, 69, 64, 46, 54, 47, 70])
ages_arr = ages_arr.reshape((45,1))


height_age_arr = np.hstack((heights_arr, ages_arr))

mask = height_age_arr[:, 0] >= 182

print(mask)
print(mask.sum())

tall_presidents = height_age_arr[mask, ]
tall_presidents.shape

print(tall_presidents.shape)
"""

#Multiple Criteria
"""
import numpy as np

heights_arr = np.array([189, 170, 189, 163, 183, 171, 185, 168, 173, 183, 173, 173, 175, 178, 183, 193, 178, 173, 174, 183, 183, 180, 168, 180, 170, 178, 182, 180, 183, 178, 182, 188, 175, 179, 183, 193, 182, 183, 177, 185, 188, 188, 182, 185, 191])
ages_arr = np.array([57, 61, 57, 57, 58, 57, 61, 54, 68, 51, 49, 64, 50, 48, 65, 52, 56, 46, 54, 49, 51, 47, 55, 55, 54, 42, 51, 56, 55, 51, 54, 51, 60, 62, 43, 55, 56, 61, 52, 69, 64, 46, 54, 47, 70]).reshape((-1,1))

heights_arr = heights_arr.reshape((45,1))
height_age_arr = np.hstack((heights_arr, ages_arr))

mask = (height_age_arr[:, 0]>=182) & (height_age_arr[:,1]<=50)

print(height_age_arr[mask,])
"""

#PRACTICE EXERCISE-Data Science - Average of Rows
import numpy as np

# Kullanicidan giriş almak
n, p = map(int, input().split())  # İlk satir: satir ve sütun sayisi
matrix = []  # Boş liste

for _ in range(n):
    row = list(map(float, input().split()))  # Satir verilerini al
    matrix.append(row)

# NumPy array'e dönüştür
matrix_np = np.array(matrix)

# Satir ortalamalarini hesapla
row_means = np.mean(matrix_np, axis=1)

# Sonuçlari yuvarla
row_means_rounded = np.round(row_means, 2)

# Çiktiyi yazdir
print(row_means_rounded)
