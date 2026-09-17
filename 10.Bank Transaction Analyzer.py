transactions = [5000, -1200, -500, 3000, -800, 10000, -15000]
balance = 0
total_deposits = 0
total_withdrawals = 0
deposit_count = 0
withdrawal_count = 0
largest_deposit = 0
largest_withdrawal = 0
for transaction in transactions:
    if transaction == 0:
        continue
    if transaction > 0:
        balance += transaction
        total_deposits += transaction
        deposit_count += 1

        if transaction > largest_deposit:
            largest_deposit = transaction

    else:
        withdrawal = abs(transaction)

        if withdrawal > balance:
            print("Insufficient balance")
            continue

        balance -= withdrawal
        total_withdrawals += withdrawal
        withdrawal_count += 1

        if withdrawal > largest_withdrawal:
            largest_withdrawal = withdrawal

    if balance < 0:
        break

print("Total deposits:", total_deposits)
print("Total withdrawals:", total_withdrawals)
print("Number of deposits:", deposit_count)
print("Number of withdrawals:", withdrawal_count)
print("Final balance:", balance)
print("Largest deposit:", largest_deposit)
print("Largest withdrawal:", largest_withdrawal)