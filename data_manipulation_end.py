import numpy as np

#1-the first step in data science is to transform it into arrays of numbers.
#2-Note that once an array is created in numpy, its size cannot be changed.
#3-Size tells us how big the array is, shape tells us the dimension.
#4-np.array bir fonksiyondur, yani bir şeyler yapar (listeyi Numpy dizisine dönüştürmek gibi).
#5-ndarray.size ise bir özelliktir, yani mevcut bir Numpy dizisi hakkinda bilgi verir (eleman sayisini döndürmek gibi).
#6-Another characteristic about numpy array is that it is homogeneous, meaning each element must be of the same data type.


heights = [189, 170, 189, 163, 183, 171, 185, 168, 173, 183, 173, 173, 175, 178, 183, 193, 178, 173, 174, 183, 183, 180, 168, 180, 170, 178, 182, 180, 183, 178, 182, 188, 175, 179, 183, 193, 182, 183, 177, 185, 188, 188, 182, 185, 191]

ages = [57, 61, 57, 57, 58, 57, 61, 54, 68, 51, 49, 64, 50, 48, 65, 52, 56, 46, 54, 49, 51, 47, 55, 55, 54, 42, 51, 56, 55, 51, 54, 51, 60, 62, 43, 55, 56, 61, 52, 69, 64, 46, 54, 47, 70]


heights_arr = np.array(heights)
ages_arr = np.array(ages)
print(heights_arr.size, "----", ages_arr.size, "----", heights_arr.shape, "----", ages_arr.shape)

