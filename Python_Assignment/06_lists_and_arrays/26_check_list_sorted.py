# Check whether a list is sorted in ascending order

def is_sorted(numbers):
    for i in range(len(numbers) - 1):
        if numbers[i] > numbers[i + 1]:
            return False
    return True


numbers = [int(value) for value in input("Enter numbers separated by spaces: ").split()]

if is_sorted(numbers):
    print("The list is sorted in ascending order.")
else:
    print("The list is not sorted in ascending order.")
