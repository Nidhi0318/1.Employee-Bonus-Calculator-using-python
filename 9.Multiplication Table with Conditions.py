num = int(input("Enter a number: "))
for i in range(1, 21):
    result = num * i
    if result > 100:
        break
    if i % 3 == 0:
        continue
    if result % 2 == 0:
        continue
    print(num, "x", i, "=", result)