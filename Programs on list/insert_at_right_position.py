#Program to insert an element at the right position in a sorted list
sorted_list = list(map(int, input("Enter the elements of a sorted list: ").split()))
element = int(input("Enter the element to be inserted: "))
print("Original sorted list:", sorted_list)

for i in range(len(sorted_list)):
    if element < sorted_list[i]:
        sorted_list.insert(i, element)
        break
    
print("List after inserting the element at the right position:", sorted_list)