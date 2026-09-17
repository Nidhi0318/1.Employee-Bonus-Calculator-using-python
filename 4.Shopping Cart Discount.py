
total = 0

n = int(input("Enter number of products: "))

for i in range(1, n + 1):
    price = float(input(f"Enter price of product {i}: ₹"))
    total += price

if total < 5000:
    discount_rate = 0
elif total < 10000:
    discount_rate = 10
elif total < 20000:
    discount_rate = 15
else:
    discount_rate = 20

member = input("Is the customer a member? (yes/no): ").lower()

if member == "yes":
    discount_rate += 5

discount = total * discount_rate / 100
final_amount = total - discount
print("\n--- Shopping Cart Bill ---")
print("Original Amount: ₹", total)
print("Discount:", discount_rate, "%")
print("Discount Amount: ₹", discount)
print("Final Amount: ₹", final_amount)