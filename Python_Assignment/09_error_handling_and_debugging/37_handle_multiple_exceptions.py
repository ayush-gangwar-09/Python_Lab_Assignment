# Examples of handling ValueError, IndexError, and TypeError

try:
    number = int(input("Enter an integer: "))
    values = [10, 20, 30]
    position = int(input("Enter a list index (0 to 2): "))
    print("Selected value:", values[position])

    # This line demonstrates a TypeError.
    result = "Number: " + number
    print(result)

except ValueError:
    print("ValueError: Please enter a valid integer.")
except IndexError:
    print("IndexError: The selected index does not exist.")
except TypeError:
    print("TypeError: A string and an integer cannot be joined directly.")
