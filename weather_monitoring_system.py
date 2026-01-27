'''Set 3 (Weather Monitoring System)
NumPy (Intermediate)
 A weather station stores hourly temperature readings for 7 days in a NumPy array of shape (7, 24).
Task:
1. Find the daily maximum and minimum temperature
2. Identify the day with the largest temperature variation
3. Replace outliers beyond ±2 standard deviations with the mean temperature
'''

import numpy as np

# Sample temperature data (7 days × 24 hours)
temps = np.random.randint(15, 40, size=(7, 24))
print(temps)
daily_max = np.max(temps, axis=1)
daily_min = np.min(temps, axis=1)
print("Daily Maximum Temperatures:", daily_max)
print("Daily Minimum Temperatures:", daily_min)
# Temperature Variation = (max temperature – min temperature) for a day
daily_variation = daily_max - daily_min
day_with_max_variation = np.argmax(daily_variation)
print("Daily Temperature Variation:", daily_variation)
print("Day with highest variation (0-based index):", day_with_max_variation)

# An outlier is any temperature that is < (mean - 2 × std) OR > (mean + 2 × std)
mean_temp = np.mean(temps)
std_temp = np.std(temps)

lower_limit = mean_temp - 2 * std_temp
upper_limit = mean_temp + 2 * std_temp

# Replace outliers
temps_cleaned = np.where(
    (temps < lower_limit) | (temps > upper_limit),
    mean_temp,
    temps
)
print("Mean Temperature:", mean_temp)
print("Standard Deviation:", std_temp)
print("Cleaned Temperature Data:\n", temps_cleaned)