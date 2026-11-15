# Count the number of digits in an integer

number = int(input("Enter an integer: "))
number = abs(number)

if number == 0:
    digit_count = 1
else:
    digit_count = 0
    while number > 0:
        digit_count = digit_count + 1
        number = number // 10

print("Number of digits:", digit_count)
