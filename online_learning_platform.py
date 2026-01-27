'''Set 4 (Online Learning Platform)
NumPy (Intermediate)
 An online platform tracks time spent (in minutes) by students on 6 courses over 14 days using a NumPy array.
Task:
1. Compute total time spent per course
2. Identify courses where average daily engagement exceeds a threshold
3. Rank courses based on engagement
'''
import numpy as np

# 14 days × 6 courses
time_spent = np.random.randint(20,106, size=(14,6))
print(time_spent)
total_time_per_course = np.sum(time_spent, axis=0)
print(total_time_per_course)
#Let's assume
threshold = 60
average_time_per_course = np.mean(time_spent, axis=0)
print(average_time_per_course)
high_engagement_courses = average_time_per_course > threshold
print(high_engagement_courses)
ranking = np.argsort(total_time_per_course)
print(ranking)
ranking_desc = np.argsort(total_time_per_course)[::-1]
print(ranking_desc)