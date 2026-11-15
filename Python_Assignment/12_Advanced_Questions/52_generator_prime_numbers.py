# Question 2: Create a generator for prime numbers up to a given limit.


def prime_numbers(limit):
    for number in range(2, limit + 1):
        is_prime = True

        for divisor in range(2, int(number ** 0.5) + 1):
            if number % divisor == 0:
                is_prime = False
                break

        if is_prime:
            # yield returns one value at a time.
            yield number


limit = int(input("Generate prime numbers up to: "))

for prime in prime_numbers(limit):
    print(prime, end=" ")

print()
