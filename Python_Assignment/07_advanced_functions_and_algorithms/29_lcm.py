# Find the LCM of two numbers

def find_gcd(first, second):
    while second != 0:
        first, second = second, first % second
    return abs(first)


def find_lcm(first, second):
    if first == 0 or second == 0:
        return 0
    return abs(first * second) // find_gcd(first, second)


a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
print("LCM:", find_lcm(a, b))
