    # LAB1.Analyze the relationship between the size of houses (measured in square footage) and their selling prices in a particular neighborhood. You have collected
    #  data on various houses in that neighborhood.Create a scatter plot using the
    #  below data and share your conclusion/analysis.
    #  Input:
    #  square_footage = np.array([1200, 1400, 1600, 1800, 2000, 2200, 2400, 2600, 2800,
    #  3000])
    #  selling_prices = np.array([250, 290, 315, 380, 410, 450, 500, 525, 570, 610]

import numpy as np
import matplotlib.pyplot as plt

square_footage = np.array([1200, 1400, 1600, 1800, 2000, 2200, 2400, 2600, 2800, 3000])
selling_prices = np.array([250, 290, 315, 380, 410, 450, 500, 525, 570, 610])

plt.figure(figsize=(8,6))
plt.scatter(square_footage, selling_prices, color='Green', label='House Data')

# m, b = np.polyfit(square_footage, selling_prices, 1)
# plt.plot(square_footage, m * square_footage + b, color='red', linestyle='--', label='Trend Line')

plt.xlabel("Square Footage(sq. ft.)")
plt.ylabel("Selling Price ($000s)")
plt.title("Relationship B/W Housing Size Vs Square footage")
plt.legend()
plt.grid(True)
plt.show()
