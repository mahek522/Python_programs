#Implementing Lambda function to calculate the power of 2
power_of_2 = int(input("Enter the power of 2: \n"))
result = (lambda num, power: num**power)(2, power_of_2)
print(f"2 raised to the power {power_of_2} is: {result}")