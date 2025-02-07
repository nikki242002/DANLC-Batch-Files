#LAB2.Create a pie chart to visualize the distribution of your monthly income by
 # source. You have collected data on the various sources of your income, such as
 # salary, freelance work, investments, and rental income. Share your
 # conclusion/analysis.
 # Input:
 # income_sources = ['Salary', 'Freelance', 'Investments', 'Rental', 'Other']
 # monthly_income = [5000, 1500, 1000, 600, 400]

import matplotlib.pyplot as plt

income_sources = ['Salary', 'Freelance', 'Investments', 'Rental', 'Other']
monthly_income = [5000, 1500, 1000, 600, 400]

plt.figure(figsize=(7, 7))
plt.pie(monthly_income, labels=income_sources, autopct='%1.1f%%', startangle=140, colors=['lightpink', 'skyblue', 'lightgreen','orange','purple'])

plt.title("Monthly Income Distribution")
plt.show()
