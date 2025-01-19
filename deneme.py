import numpy as np
#1-the first step in data science is to transform it into arrays of numbers.



heights = [189, 170, 189, 163, 183, 171, 185, 168, 173, 183, 173, 173, 175, 178, 183, 193, 178, 173, 174, 183, 183, 180, 168, 180, 170, 178, 182, 180, 183, 178, 182, 188, 175, 179, 183, 193, 182, 183, 177, 185, 188, 188, 182, 185, 191]

ages = [57, 61, 57, 57, 58, 57, 61, 54, 68, 51, 49, 64, 50, 48, 65, 52, 56, 46, 54, 49, 51, 47, 55, 55, 54, 42, 51, 56, 55, 51, 54, 51, 60, 62, 43, 55, 56, 61, 52, 69, 64, 46, 54, 47, 70]

heights_ages = heights + ages #>> iki listeyi tek liste haline getirir.

heights_ages_arr = np.array(heights_ages) #np array tipine çevirir

#print(heights_ages_arr)

#print(heights_ages_arr.dtype) #int64 >> 64 bitsize integer

#print(heights_ages_arr.size) #90 >> dizenin 90 adet elemanı var

#print(heights_ages_arr.shape) #(90,)

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