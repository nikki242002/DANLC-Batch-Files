#Q1.Suppose you have a dataset containing daily temperature readings for a city, and you want to identify days with extreme temperature conditions. Find days where the temperature either exceeded 35 degrees Celsius (hot day) or dropped below 5 degrees Celsius (cold day).
#Input:
#temperatures = np.array([32.5, 34.2, 36.8, 29.3, 31.0, 38.7, 23.1, 18.5, 22.8, 37.2,4,25,12,-4,-12])
import numpy as np
temperatures = np.array([32.5, 34.2, 36.8, 29.3, 31.0, 38.7, 23.1, 18.5, 22.8, 37.2, 4, 25, 12, -4, -12])

hot_days = np.where(temperatures > 35)[0]
cold_days = np.where(temperatures < 5)[0]
print("Hot days:")
print("Days (indices):\n", hot_days)
print("Temperatures(°C):\n", temperatures[hot_days])

print("Cold days:")
print("Days (indices):\n", cold_days)
print("Temperatures(°C):\n",temperatures[cold_days])

