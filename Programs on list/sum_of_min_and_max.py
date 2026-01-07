#Find the sum of minimum and maximum number of a list without using built-in functions.
list = list(map(int, input("Enter the elements of a list: ").split()))
min_num = list[0]
max_num = list[0]
for i in range(1,len(list)):
    if list[i]<min_num:
        min_num = list[i]
    if list[i]>max_num:
        max_num = list[i]
        
print("The sum of minimum and maximum number in the list is:", min_num + max_num)