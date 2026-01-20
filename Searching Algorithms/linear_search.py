def linear_search(arr, key):
    for i in range(0,len(arr)):
        if arr[i] == key:
            return i
    return -1
def main():
    arr = list(map(int, input("Enter the elements of the array separated by spaces: ").split()))
    key = int(input("Enter the element to search for: "))
    index = linear_search(arr, key)
    if index != -1:
        print(f"Element found at index: {index}")
    else:
        print("Element not found in the array.")
if __name__ == "__main__":
    main()