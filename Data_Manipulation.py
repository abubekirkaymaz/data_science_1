import numpy as np

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
