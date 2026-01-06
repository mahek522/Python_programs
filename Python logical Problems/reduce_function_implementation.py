# Implementing reduce() function using def function()
from functools import reduce
list = list(map(int, input("Enter the elements of a list to be reduced: ").split()))
def sum_two_numbers(x, y):
    return x + y
result = reduce(sum_two_numbers, list)
print("The sum of all elements in the list is: ", result)
#Implementing reduce() function using lambda function
result_lambda = reduce(lambda x, y: x + y, list)
print("The sum of all elements in the list using Lambda is: ", result_lambda)

