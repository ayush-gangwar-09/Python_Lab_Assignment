# Function to check whether a number is prime

def is_prime(number):
    if number <= 1:
        return False

    for divisor in range(2, number):
        if number % divisor == 0:
            return False

    return True


number = int(input("Enter a number: "))

if is_prime(number):
    print(number, "is prime.")
else:
    print(number, "is not prime.")
