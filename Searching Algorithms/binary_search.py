def binary_search(arr, key):
    low, high, mid = 0, len(arr) - 1, 0
    if arr == sorted(arr):
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] < key:
                low = mid + 1
            elif arr[mid] > key:
                high = mid - 1
            else:
                return mid
    else:
        print("Array is not sorted. Binary search cannot be performed.")
        return -1
    return -1
def main():
    arr = list(map(int, input("Enter the elements of the sorted array separated by spaces: ").split()))
    key = int(input("Enter the element to search for: "))
    index = binary_search(arr, key)
    if index != -1:
        print(f"Element found at index: {index}")
    else:
        print("Element not found in the array.")
        
if __name__ == "__main__":
    main()