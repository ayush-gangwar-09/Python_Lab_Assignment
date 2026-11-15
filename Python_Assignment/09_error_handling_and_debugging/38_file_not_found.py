# Handle FileNotFoundError using try-except

file_name = input("Enter the file name to open: ")

try:
    file = open(file_name, "r")
    content = file.read()
    file.close()
    print(content)
except FileNotFoundError:
    print("Error: The file was not found.")
