# Check whether a list is a palindrome

items = input("Enter list items separated by spaces: ").split()

if items == items[::-1]:
    print("The list is a palindrome.")
else:
    print("The list is not a palindrome.")
