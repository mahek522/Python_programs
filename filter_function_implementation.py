
# Implementing filter() function using def function()

nums = list(map(int, input("Enter the elements of a list to be filtered: ").split()))

def is_even(num):
    return num % 2 == 0

even_list = list(filter(is_even, nums))

print("The even elements in the list are:", even_list)

