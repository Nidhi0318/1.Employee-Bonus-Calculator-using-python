num = int(input("Enter a positive integer: "))
original = num
count = 0
sum_digits = 0
largest = 0
smallest = 9
while num > 0:
    digit = num % 10
    count += 1
    sum_digits += digit
    if digit > largest:
        largest = digit
    if digit < smallest:
        smallest = digit

    num = num // 10
temp = original
reverse = 0

while temp > 0:
    digit = temp % 10
    reverse = reverse * 10 + digit
    temp = temp // 10

if original == reverse:
    palindrome = "Yes"
else:
    palindrome = "No"

print("\n--- Number Analysis ---")
print("Digits:", count)
print("Sum:", sum_digits)
print("Largest digit:", largest)
print("Smallest digit:", smallest)
print("Palindrome:", palindrome)