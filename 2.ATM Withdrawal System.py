balance = float(input("Enter current account balance: ₹"))
while True:
    print("\n ATM Menu")
    print("1. Withdraw Money")
    print("2. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        amount = int(input("Enter withdrawal amount: ₹"))
        if amount % 500 != 0:
            print("Invalid amount! Withdrawal must be a multiple of ₹500.")
        elif amount > balance:
            print("Insufficient balance!")
        elif balance - amount < 1000:
            print("Invalid withdrawal! Minimum balance of ₹1,000 must be maintained.")
        else:
            balance -= amount
            print("Withdrawal successful!")
            print("Withdrawn amount: ₹", amount)
            print("Remaining balance: ₹", balance)
    elif choice == 2:
        print("Thank you for using the ATM!")
        print("Final balance: ₹", balance)
        break
    else:
        print("Invalid choice! Please select 1 or 2.")