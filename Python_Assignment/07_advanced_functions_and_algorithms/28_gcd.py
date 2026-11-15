# Find the GCD of two numbers using the Euclidean algorithm

def find_gcd(first, second):
    first = abs(first)
    second = abs(second)

    while second != 0:
        first, second = second, first % second

    return first


a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
print("GCD:", find_gcd(a, b))
