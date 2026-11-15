# Find the sum of all even numbers from 1 to 100

total = 0

for number in range(1, 101):
    if number % 2 == 0:
        total = total + number

print("Sum of even numbers from 1 to 100:", total)
