# Recommendation program exercise for Il-Maq   7/11/2021
# Different products will appear for different customers
# Method - Counting and ranking product purchases for each customer and offering the most common

# Importing packages
import pandas as pd
import matplotlib.pyplot as plt

# Reading files into pd and combining
order_items = pd.read_csv('C:/Users/Administrator/Downloads/order_items.csv')
orders = pd.read_csv('C:/Users/Administrator/Downloads/orders.csv')
combined = orders.join(order_items.set_index('order_id'), on='order_id')

orders.shape        # (15115, 3
order_items.shape   # (29099, 5)
combined.shape      # (29099, 7)

# Count products purchased by customer
customer_products = combined.groupby('customer_unique_id')['product_id']. \
                                      value_counts().reset_index(name='Counts')

# Find the 5 products most bought by customer x
customer_x = customer_products[customer_products.customer_unique_id == 
                               'dc813062e0fc23409cd255f7f53c7074'].head()

# Produce a barchart
customer_x.plot.bar(x='product_id')
plt.show()
