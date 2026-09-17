start = int(input("Enter start number: "))
end = int(input("Enter end number: "))

primes = []
total = 0

for num in range(start, end + 1):
    if num < 2:
        continue

    is_prime = True

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        primes.append(num)
        total += num

if primes:
    print("Primes:", *primes)
    print("Count:", len(primes))
    print("Sum:", total)
    print("Largest:", max(primes))
else:
    print("No prime numbers found")