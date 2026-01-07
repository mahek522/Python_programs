#Find the sum of all elements in a list without using built-in functions.
list = list(map(int, input("Enter the elements of a list: ").split()))
total_sum = 0
for i in list:
    total_sum += i
print("The sum of all elements in the list is:", total_sum)