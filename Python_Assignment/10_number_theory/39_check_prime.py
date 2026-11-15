# Check whether a number is prime

number = int(input("Enter an integer: "))

is_prime = True

if number <= 1:
    is_prime = False
else:
    for divisor in range(2, number):
        if number % divisor == 0:
            is_prime = False
            break

if is_prime:
    print(number, "is prime.")
else:
    print(number, "is not prime.")
