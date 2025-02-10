import pandas as pd
import matplotlib.pyplot as plt
data = {
    'customer_name': ['Alice', 'Bob', 'Charlie', 'David', 'Emma', 'Frank', 'Grace', 'Henry', 'Isla', 'Jack'],
    'product_name': ['Laptop', 'Phone', 'Tablet', 'Laptop', 'Phone', 'Tablet', 'Laptop', 'Phone', 'Tablet', 'Laptop'],
    'quantity_sold':[2, 3, 5, 1, 4, 2, 3, 2, 1, 4],
    'price': [1000, 500, 300, 1000, 500, 300, 1000, 500, 300, 1000],
    'sale_date': pd.to_datetime(['2024-01-15', '2024-02-10', '2024-03-05', '2024-04-12', '2024-05-18',
                                 '2024-06-20', '2024-07-25', '2024-08-30', '2024-09-15', '2024-10-10'])
}
df = pd.DataFrame(data)

df['total_revenue'] = df['quantity_sold'] * df['price']

total_revenue = df['total_revenue'].sum()
print(f"Total Revenue for the year: ${total_revenue}")

average_revenue_per_sale = df['total_revenue'].mean()
print(f"Average Revenue per Sale: ${average_revenue_per_sale:.2f}")

best_selling_product = df.groupby('product_name')['quantity_sold'].sum().idxmax()
print(f"Best-Selling Product: {best_selling_product}")

highest_revenue_date = df.groupby('sale_date')['total_revenue'].sum().idxmax()
print(f"Date with Highest Total Revenue: {highest_revenue_date}")

sales_per_product = df.groupby('product_name')['quantity_sold'].sum()
sales_per_product.plot(kind='bar', color='green', edgecolor='black')
plt.xlabel("Product")
plt.ylabel("Total Quantity Sold")
plt.title("Total Sales per Product")
plt.xticks(rotation=45)
plt.show()

revenue_per_product = df.groupby('product_name')['total_revenue'].sum()
revenue_per_product.plot(kind='bar', color='yellow',label='Product',edgecolor='black')
plt.xlabel("Product")
plt.ylabel("Total Revenue")
plt.title("Total Revenue per Product")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
