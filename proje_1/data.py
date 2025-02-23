import random
import numpy  as np

random_numbers = np.random.randint(500, 5001, size=20)
print(random_numbers)

random_floats = np.random.uniform(1.0, 10.0, size=20)
print(random_floats)

rounded_floats = np.around(random_floats, decimals=2)
print(rounded_floats)

#print(type(random_numbers))
