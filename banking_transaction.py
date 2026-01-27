'''Set 5 (Banking Transactions)
NumPy (Intermediate)
 A bank stores transaction amounts for 50 accounts across 20 days in a NumPy array.
Task:
1. Separate debit and credit transactions
2. Compute daily net balance changes
3. Identify accounts with continuous negative balance trends
'''
import numpy as np

transactions = np.random.randint(-5000, 5000, size=(20, 50))
print(transactions)
credits = transactions[transactions > 0]
debits = transactions[transactions < 0]
print(credits)
print(debits)
daily_net_change = np.sum(transactions, axis=1)
print(daily_net_change)
negative_trend_accounts = np.where(np.all(transactions < 0, axis=0))
print(negative_trend_accounts)