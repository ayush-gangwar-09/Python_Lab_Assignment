# Calculate factorial using recursion

def factorial(number):
    if number < 0:
        return None
    if number == 0 or number == 1:
        return 1
    return number * factorial(number - 1)


number = int(input("Enter a non-negative integer: "))
answer = factorial(number)

if answer is None:
    print("Factorial is not defined for negative numbers.")
else:
    print("Factorial:", answer)
