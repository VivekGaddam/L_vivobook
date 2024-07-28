import pandas as pd
import matplotlib.pyplot as plt

# Read the Data
df = pd.read_csv("Data.csv")

# Data Cleaning
# Check for missing values
print(df.isnull().sum())

# Handle missing values
df.fillna(0, inplace=True)

df['total_sales'] = df['price'] * df['quantity']

total_sales_per_product = df.groupby('product_name')['total_sales'].sum().reset_index()
top_10_products = total_sales_per_product.sort_values(by='total_sales', ascending=False).head(10)


average_order_value = df.groupby('city')['total_sales'].mean().reset_index()

# Customer Activity
customer_orders = df.groupby('customer_id').size().reset_index(name='order_count')

# Visualization
# A. Top 10 Products
plt.figure(figsize=(10, 6))
plt.barh(top_10_products['product_name'], top_10_products['total_sales'])
plt.xlabel('Total Sales')
plt.ylabel('Product Name')
plt.title('Top 10 Selling Products')
plt.gca().invert_yaxis()  # Invert y-axis to display top selling product on top
plt.show() # B. Customer Activity
plt.figure(figsize=(10, 6))
customer_activity = customer_orders['order_count'].value_counts().sort_index()
plt.bar(customer_activity.index, customer_activity.values)
plt.xlabel('Number of Orders')
plt.ylabel('Number of Customers')
plt.title('Customer Order Frequency')
plt.show()
