#Program to find the minimum and maximum values by summing exactly four out of five elements in a list. Print the minimum and maximum values.
list = list(map(int, input("Enter five elements of a list: ").split()))

print(sum(list) - max(list), sum(list) - min(list))