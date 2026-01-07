#Find the length of a list without using built-in functions.
list = list(map(int, input("Enter the elements of a list: ").split()))
length = 0
for i in list:
    length += 1
print("The length of the list is:", length)