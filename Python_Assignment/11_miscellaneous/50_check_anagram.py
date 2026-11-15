# Check whether two strings are anagrams

first_text = input("Enter the first string: ")
second_text = input("Enter the second string: ")

# Ignore spaces and letter case before comparing.
first_clean = first_text.replace(" ", "").lower()
second_clean = second_text.replace(" ", "").lower()

if sorted(first_clean) == sorted(second_clean):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")
