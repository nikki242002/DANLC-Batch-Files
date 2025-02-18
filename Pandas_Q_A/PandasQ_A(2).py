#WAP.2 Suppose you're working in a retail store you have some customer data.
# Please write a program to display the marital status wise customer count and also display the bar chart using python pandas and matplotlib.
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("D:\\NIK'S_FOLDER\Pandas_Lib\customer_data (1).csv")
print("Data Frame\n",df)
Marital_status_counts = df['Marital_status'].value_counts()

# Displaying the counts
print("Marital status-wise student count:")
print(Marital_status_counts)

plt.figure(figsize=(8,6))
Marital_status_counts.plot(kind='bar', color=['magenta','orange'], edgecolor='black')
plt.xlabel("Marital status")
plt.ylabel("Student Count")
plt.title("Marital Status-wise Student Count")
plt.xticks(rotation=0,fontsize=11)
plt.show()
