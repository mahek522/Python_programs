#Missing number in a list
def find_missing_number(nums):
    n = len(nums) + 1
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum
def main():
    nums = [1, 2, 4, 5, 6]  #Example list with a missing number
    missing_number = find_missing_number(nums) 
    print(f"The missing number is: {missing_number}")
    
if __name__=="__main__":
    main()