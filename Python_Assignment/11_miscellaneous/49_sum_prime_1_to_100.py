# Find the sum of all prime numbers from 1 to 100

total = 0

for number in range(2, 101):
    is_prime = True

    for divisor in range(2, number):
        if number % divisor == 0:
            is_prime = False
            break

    if is_prime:
        total = total + number

print("Sum of prime numbers from 1 to 100:", total)
