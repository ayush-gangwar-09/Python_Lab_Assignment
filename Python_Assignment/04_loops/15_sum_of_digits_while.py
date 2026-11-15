# Find the sum of digits using a while loop

number = abs(int(input("Enter an integer: ")))
digit_sum = 0

while number > 0:
    digit = number % 10
    digit_sum = digit_sum + digit
    number = number // 10

print("Sum of digits:", digit_sum)
