# Convert Celsius to Fahrenheit using a function

def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


temperature = float(input("Enter temperature in Celsius: "))
print("Temperature in Fahrenheit:", celsius_to_fahrenheit(temperature))
