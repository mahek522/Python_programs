nums = eval(input("Enter the list of integers: "))
target = int(input("Enter the target value: "))
res_list=[]
for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        if nums[i]+nums[j]==target:
            res_list.extend([i,j])
            
print("The pairs in the list whose sum is equal to target value are:", res_list)