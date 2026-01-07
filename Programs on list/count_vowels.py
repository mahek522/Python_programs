#Program to count the number of vowels in a string
string = input("Enter a string: ")
vowels = "aeiouAEIOU"

#Traditional approach
res = []
for i in string:
    if i in vowels:
        res.append(i)
print("Number of vowels in the given string:", len(res))

#Using List Comprehension
print("Number of vowels in the given string using List Comprehension:", len([i for i in string if i in vowels]))