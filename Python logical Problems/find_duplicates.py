#Find All Duplicates in a List
#Return elements that appear more than once.
def find_duplicates(input_list):
    seen = set()
    duplicates = set()
    
    for item in input_list:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)
    
    return list(duplicates)
#Example usage
input_list = [1, 2, 3, 4, 5, 3, 2, 6, 7, 8, 1]
duplicates = find_duplicates(input_list)
print("Duplicates:", duplicates)  #Output: Duplicates: [1, 2, 3]