# Calculate the sum of natural numbers from 1 to N

number = int(input("Enter a positive integer N: "))

if number < 1:
    print("Please enter a positive integer.")
else:
    total = 0
    for value in range(1, number + 1):
        total = total + value
    print("Sum:", total)
