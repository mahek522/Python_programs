#Taking input from user
N = int(input("Enter the power value of 2: "))

#Checking for invalid power
if N < 0 or N >= 31:
    print("Please enter N such that 0 <= N < 31")
else:
    power = 1
    for i in range(N + 1):
        print(f"2^{i} = {power}")
        power *= 2