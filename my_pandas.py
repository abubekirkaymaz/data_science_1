import pandas as pd
import numpy as np


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

