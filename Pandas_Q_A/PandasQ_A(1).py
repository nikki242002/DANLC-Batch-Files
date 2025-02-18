#WAP.1Suppose you're working in a school you have some student data.Please write a program to display the Major subject wise students count
# and also display the pie chart using python pandas and matplotlib.
import pandas as pd
import matplotlib.pyplot as plt

df = df = pd.read_csv("C:\\Users\\NITIN SHARMA\Downloads\student_data.csv")
print("Data Frame\n",df)
major_counts = df['Major'].value_counts()
print("Major-wise student count:")
print(major_counts)
plt.figure(figsize=(8, 6))
plt.pie(major_counts, labels=major_counts.index, autopct='%1.1f%%', startangle=90,colors=['orange','blue','purple','red','green'])
plt.title("City-wise Student Distribution")
plt.axis('equal')
plt.show()
