# Find the sum of odd numbers from 1 to 100 using a function

def sum_odd_numbers():
    total = 0

    for number in range(1, 101):
        if number % 2 != 0:
            total = total + number

    return total


print("Sum of odd numbers from 1 to 100:", sum_odd_numbers())
