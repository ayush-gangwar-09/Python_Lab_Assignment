# Find the sum of all positive divisors of a number

number = int(input("Enter a positive integer: "))

if number <= 0:
    print("Please enter a positive integer.")
else:
    total = 0
    for divisor in range(1, number + 1):
        if number % divisor == 0:
            total = total + divisor
    print("Sum of divisors:", total)
