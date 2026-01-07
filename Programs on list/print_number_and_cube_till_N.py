#Program to print the number and its cube till N
N = int(input("Enter a number N: "))
res = []

#Traditional approach
for i in range(1, N + 1):
    res.append((i, i**3))
print("The numbers and their cubes till N are:", res)

#Using List Comprehension
res_comp = [(i, i**3) for i in range(1, N + 1)]
print("The numbers and their cubes till N using List Comprehension are:", res_comp)