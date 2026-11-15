# Remove duplicate characters while keeping the first occurrence

text = input("Enter a string: ")
result = ""

for character in text:
    if character not in result:
        result = result + character

print("String without duplicate characters:", result)
