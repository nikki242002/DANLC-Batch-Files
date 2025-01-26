# Q1.How to find the mean of every NumPy array in the given list?
# Input: list = [ np.array([3, 2, 8, 9]), np.array([4, 12, 34, 25, 78]), np.array([23, 12, 67]) ]
import numpy as np
list_of_arrays = [np.array([3, 2, 8, 9]), np.array([4, 12, 34, 25, 78]), np.array([23, 12, 67])]
means = [np.mean(arr) for arr in list_of_arrays]
print(means)
