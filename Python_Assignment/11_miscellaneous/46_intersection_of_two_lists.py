# Find common elements between two lists

def find_intersection(first_list, second_list):
    common_items = []

    for item in first_list:
        if item in second_list and item not in common_items:
            common_items.append(item)

    return common_items


first_list = input("Enter first list values separated by spaces: ").split()
second_list = input("Enter second list values separated by spaces: ").split()

print("Common elements:", find_intersection(first_list, second_list))
