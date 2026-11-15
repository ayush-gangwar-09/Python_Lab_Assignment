# Handle division by zero using try-except

try:
    first = float(input("Enter the first number: "))
    second = float(input("Enter the second number: "))
    result = first / second
    print("Result:", result)
except ZeroDivisionError:
    print("Error: A number cannot be divided by zero.")
except ValueError:
    print("Error: Please enter valid numbers.")
