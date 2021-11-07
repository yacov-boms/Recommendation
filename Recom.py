# Recommendation program exercise for Il-Maq   7/11/2021
# Different products will appear in different product pages
# Method - Counting and ranking couples of products permutations to find associations

# Importing packages
import pandas as pd
from itertools import permutations
import matplotlib.pyplot as plt

# Reading files into pd and combining
order_items = pd.read_csv('C:/Users/Administrator/Downloads/order_items.csv')
orders = pd.read_csv('C:/Users/Administrator/Downloads/orders.csv')
combined = orders.join(order_items.set_index('order_id'), on='order_id')

orders.shape        # (15115, 3
order_items.shape   # (29099, 5)
combined.shape      # (29099, 7)

# Create function to find all couple permutations
def find_product_pairs(x):
  pairs = pd.DataFrame(list(permutations(x.values, 2)) ,columns=['product_a',
                                                                 'product_b'])
  return pairs

# Apply the function on products by each customer
product_combinations = combined.groupby('customer_unique_id')['product_id']. \
    apply(find_product_pairs).reset_index(drop=True)

# How often each item in product_a occurs with items in product_b
comb_counts_series = product_combinations.groupby(['product_a','product_b']).size()

# Make it a DataFrame
comb_counts = comb_counts_series.to_frame(name='size').reset_index()
print(comb_counts.head())

# Sort the counts descending
comb_counts_sorted = comb_counts.sort_values('size',ascending=False)

# Drop same product bought 
comb_counts_sorted = comb_counts_sorted[comb_counts_sorted.product_a != 
                                        comb_counts_sorted.product_b]

# Find the 5 products mostly bought by customers who buy product x
product_x = comb_counts_sorted[comb_counts_sorted['product_a'] == 
                          '389d119b48cf3043d311335e499d9c6b'].head()

# Produce a barchart
product_x.plot.bar(x="product_b")
plt.show()

