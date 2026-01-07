#Program to demonstrate if-else in list comprehension
#For every even element in the list, square it; for every odd element, double it.

#Traditional approach
list = list(map(int, input("Enter the elements of a list: ").split()))
new_list = []
for i in list:
    if i % 2 == 0:
        new_list.append(i**2)
    else:
        new_list.append(i*2)
        
print("Original list:", list)
print("New list :", new_list)

#Using List Comprehension
new_list_comp = [i**2 if i % 2 == 0 else i*2 for i in list]
print("New list after using List Comprehension:", new_list_comp)