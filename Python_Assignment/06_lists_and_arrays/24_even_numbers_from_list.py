# Create a new list containing only even numbers

numbers = [int(value) for value in input("Enter integers separated by spaces: ").split()]
even_numbers = []

for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)

print("Even numbers:", even_numbers)
