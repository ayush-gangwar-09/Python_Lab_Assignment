# Display Fibonacci sequence up to N terms

terms = int(input("How many terms do you want? "))

first = 0
second = 1

if terms <= 0:
    print("Please enter a positive number of terms.")
else:
    for i in range(terms):
        print(first, end=" ")
        next_number = first + second
        first = second
        second = next_number
    print()
