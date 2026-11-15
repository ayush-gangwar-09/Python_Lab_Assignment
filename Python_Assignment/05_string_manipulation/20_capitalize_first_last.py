# Capitalize the first and last letters of a string

text = input("Enter a string: ")

if len(text) == 0:
    print("The string is empty.")
elif len(text) == 1:
    print(text.upper())
else:
    result = text[0].upper() + text[1:-1] + text[-1].upper()
    print("Updated string:", result)
