'''Set 2 (Employee Performance System)
NumPy (Intermediate)
 An HR system stores employee performance ratings (scale 1–5) for 100 employees over 4 quarters in a NumPy array.
Task:
1. Normalize the ratings using min-max normalization
2. Calculate the average rating per employee
3. Identify employees whose average rating is above the company mean
'''


import numpy as np

# Create sample ratings (random integers from 1 to 5)
ratings = np.random.randint(1, 6, size=(100, 4))
#print(ratings)
# Formula for Min-Max Normalisation: normalized_value = (value - min) / (max - min)
min_rating = ratings.min()
max_rating = ratings.max()
#print(max_rating)
#print(min_rating)
normalized_ratings = (ratings - min_rating) / (max_rating - min_rating)
#print(normalized_ratings)
avg_rating_per_employee = ratings.mean(axis=1)
print(avg_rating_per_employee)
print(avg_rating_per_employee.shape)
company_mean = avg_rating_per_employee.mean()
#print(company_mean)
above_average_employees = np.where(avg_rating_per_employee > company_mean)
#print(above_average_employees)
above_average_employees = above_average_employees[0]
#print(above_average_employees)
print("Company Mean Rating:", company_mean)
print("Employees with above-average performance:", above_average_employees)
print("Number of such employees:", len(above_average_employees))