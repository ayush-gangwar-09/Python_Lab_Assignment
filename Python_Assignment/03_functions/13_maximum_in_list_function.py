# Find the largest element in a list using a function

def find_largest(numbers):
    if len(numbers) == 0:
        return None

    largest = numbers[0]
    for number in numbers:
        if number > largest:
            largest = number

    return largest


numbers = [float(value) for value in input("Enter numbers separated by spaces: ").split()]
answer = find_largest(numbers)

if answer is None:
    print("The list is empty.")
else:
    print("Largest element:", answer)
