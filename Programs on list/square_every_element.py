#Program to square every element ina list and place it in a new list

#Traditional approach
list = list(map(int, input("Enter the elements of a list: ").split()))
new_list = []
for i in list:
    new_list.append(i**2)
print("Original list:", list)
print("New list with squared elements:", new_list)

#using List Comprehension
squared_list = [i**2 for i in list]
print("New list with squared elements using List Comprehension:", squared_list)
