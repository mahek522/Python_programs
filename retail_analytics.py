'''Set 1 (Retail Analytics)
NumPy (Intermediate)
 A retail company records daily sales of 5 products across 30 days in a 2D NumPy array of shape (30, 5).
 Due to a system error, negative values appear in the dataset.
Task:
1. Replace negative values with 0
2. Compute the average weekly sales per product (assume 7 days = 1 week)
3. Identify the product with the highest average weekly sales
'''

import numpy as np

sales = np.random.randint(-20, 100, size=(30, 5))

sales[sales < 0] = 0
weekly_data = sales[:28]
weekly_data = weekly_data.reshape(4, 7, 5)

weekly_sales = weekly_data.sum(axis=1)
print(weekly_sales)
avg_weekly_sales = weekly_sales.mean(axis=0)
print(avg_weekly_sales)
highest_product = np.argmax(avg_weekly_sales)
print("Average weekly sales per product:")
print(avg_weekly_sales)
print("Product with highest average weekly sales:", highest_product)

