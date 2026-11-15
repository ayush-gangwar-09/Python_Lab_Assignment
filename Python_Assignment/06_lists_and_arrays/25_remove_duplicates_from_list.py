# Remove duplicate values from a list

numbers = input("Enter values separated by spaces: ").split()
unique_numbers = []

for item in numbers:
    if item not in unique_numbers:
        unique_numbers.append(item)

print("List after removing duplicates:", unique_numbers)
