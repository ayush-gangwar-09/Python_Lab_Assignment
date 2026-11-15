# Swap two variables without using a temporary variable

first_number = input("Enter the first value: ")
second_number = input("Enter the second value: ")

first_number, second_number = second_number, first_number

print("After swapping:")
print("First value:", first_number)
print("Second value:", second_number)
