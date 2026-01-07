#Program to find pairs from two lists

list1 = list(map(int, input("Enter the elements of the first list: ").split()))
list2 = list(map(int, input("Enter the elements of the second list: ").split()))


#Traditional approach
pairs = []
for i in list1:
    for j in list2:
        if i != j:
            pairs.append((i, j))
            
print("The pairs from the two lists are:", pairs)

#Using List Comprehension
pairs_comp = [(i, j) for i in list1 for j in list2 if i != j]
print("The pairs from the two lists using List Comprehension are:", pairs_comp)