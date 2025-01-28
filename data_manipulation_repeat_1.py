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



#Indexing
# Slicing
#2D Numpy Array'de Slicing
#Assigning Single Values
#Assigning an Array to an Array
#Mathematical Operations on Arrays
#Comparisons
#Mask & Subsetting
#Multiple Criteria
#Concatenate & Combine
