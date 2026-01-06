# Read inputs
print("Enter initial balance:")
balance = int(input())
print("Enter number of transactions:")
n = int(input())
print("Enter transaction amounts:")
for _ in range(n):
    amount = int(input())

    if amount % 100 == 0 and balance >= amount:
        balance -= amount
        print("SUCCESS")
    else:
        print("FAILED")

# Print final balance
print(balance)