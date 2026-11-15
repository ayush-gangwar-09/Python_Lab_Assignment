# Count the occurrences of the letter 'o'

text = input("Enter a string: ")
count = 0

for character in text:
    if character == "o":
        count = count + 1

print("Number of lowercase 'o' characters:", count)
