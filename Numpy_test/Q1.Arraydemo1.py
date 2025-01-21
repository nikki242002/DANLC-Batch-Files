# Q1 Write a NumPy program to create an array of 10 zeros, 10 ones, and 10 fives.

import numpy as np
zeros_array = np.zeros(10)
print("Array of 10 zeros:", zeros_array)

ones_array = np.ones(10)
print("Array of 10 ones:", ones_array)

fives_array = np.full(10, 5)
print("Array of 10 fives:", fives_array)
