# Find the largest element without using max()

numbers = [float(value) for value in input("Enter numbers separated by spaces: ").split()]

if len(numbers) == 0:
    print("The list is empty.")
else:
    largest = numbers[0]

    for number in numbers:
        if number > largest:
            largest = number

    print("Largest number:", largest)
