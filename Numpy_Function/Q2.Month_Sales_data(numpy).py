#Q2.Suppose you have a dataset containing monthly sales data for a company, and you want to split this data into quarterly reports for analysis and reporting purposes.
#Input: monthly_sales = np.array([120, 135, 148, 165, 180, 155, 168, 190, 205, 198, 210, 225])

import numpy as np

monthly_sales = np.array([120, 135, 148, 165, 180, 155, 168, 190, 205, 198, 210, 225])

quarterly_sales = np.split(monthly_sales, 4)

for i, quarter in enumerate(quarterly_sales, start=1):
    print(f"Quarter {i}(in thousand of Dollers): \n {quarter}")
