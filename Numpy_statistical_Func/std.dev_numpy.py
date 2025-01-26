#Q3.Compute the standard deviation of the NumPy array Input: arr = [20, 2, 7, 1, 34].

import numpy as np
arr = np.array([20, 2, 7, 1, 34])
std_dev = np.std(arr)
print("Array:",arr)
std_float32 = np.std(arr, dtype=np.float32)
std_float64 = np.std(arr, dtype=np.float64)
print("Standard Deviation of arr:", std_dev)
print(f"More precision with (float32):\n {std_float32}")
print(f"More accuracy with (float64):\n {std_float64}")
