import pandas as pd
import numpy as np

#**********Pandas**************#
# #1-The Series is one building block in pandas. Pandas Series is a one-dimensional labeled array that can hold data of any type (integer, string, float, python objects, etc.), similar to a column in an excel spreadsheet. The axis labels are collectively called index.If we are given a bag of letters a, b, and c, and count how many of each we have, we find that there are 1 a, 2 b’s, and 3 c’s. We could create a Series by supplying a list of counts and their corresponding labels:
#print(pd.Series([1, 2, 3], index=['a', 'b', 'c'])) # with index

# #2-Alternatively, the values can be a numpy array:
# print(pd.Series(np.array([1, 2, 3]), index=['a', 'b', 'c'])) # from a 1darray

# #3-we could use a dictionary to specify the index with keys:
# print(pd.Series({'a': 1, 'b': 2, 'c':3})) # from a dict

# #4-If we don’t specify the index, by default, the index would be the integer positions starting from 0.
# print(pd.Series([1, 2, 3]))

# #5-In a Series, we can access the value by its index directly:
# series = pd.Series({'a': 1, 'b': 2, 'c':3})
# print(series['a'])

#**********Pandas DataFrames**************#

# #1-Think of DataFrame as a collection of the Series. Here, sales consists of two Series, one named under "red_wine", the other "white_wine", thus, we can access each series by calling its name:

# wine_dict = {
#     'red_wine': [3, 6, 5],
#     'white_wine':[5, 0, 10]
# }
# sales = pd.DataFrame(wine_dict, index=["adam", "bob", "charles"])
# print(sales)
# print(sales['white_wine'])

# #2- The DataFrame presidents_df is read from a CSV file as follows. Note that index is set to be the names of presidents.
# presidents_df = pd.read_csv('https://sololearn.com/uploads/files/president_heights_party.csv', index_col='name')
# print(presidents_df.shape) #(45, 4)


# #3-There are 45 rows and 4 columns in this DataFrame. To get the number of rows we can access the first element in the tuple.
# presidents_df = pd.read_csv('https://sololearn.com/uploads/files/president_heights_party.csv', index_col='name')                       
# print(presidents_df.shape[0])

# #4-Size also works on DataFrame to return an integer representing the number of elements in this object.
# presidents_df = pd.read_csv('https://sololearn.com/uploads/files/president_heights_party.csv', index_col='name')
# print(presidents_df.size)

# #5-Instead of looking at the entire dataset, we can just take a peep. To see the first few lines in a DataFrame, use .head(); if we don’t specify n (the number of lines), by default, it displays the first five rows. Here we want to see the top 3 rows.
# presidents_df = pd.read_csv('https://sololearn.com/uploads/files/president_heights_party.csv', index_col='name')
# print(presidents_df.head(n=3))

# #6-Similarly, if we want to see the last few rows, we can use .tail(), the default is also five rows.
# presidents_df = pd.read_csv('https://sololearn.com/uploads/files/president_heights_party.csv', index_col='name')
# print(presidents_df.tail())

# #7-Use .info() to get an overview of the DataFrame. Its output includes index, column names, count of non-null values, dtypes, and memory usage.
# #"party" sütunu metinsel parti isimleri içerdiği için Pandas bunu object olarak saklar.

# presidents_df = pd.read_csv('https://sololearn.com/uploads/files/president_heights_party.csv', index_col='name')
# presidents_df.info()                                  
