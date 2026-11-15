# Question 3: Create a custom context manager for writing to a file.


class FileWriter:
    def __init__(self, file_name):
        self.file_name = file_name
        self.file = None

    def __enter__(self):
        # Open the file when the with block starts.
        self.file = open(self.file_name, "w", encoding="utf-8")
        return self.file

    def __exit__(self, exception_type, exception_value, traceback):
        # Close the file even if an error happens inside the with block.
        if self.file:
            self.file.close()

        # False means Python should not hide any exception.
        return False


message = input("Enter a message to save: ")

with FileWriter("my_message.txt") as file:
    file.write(message)

print("Message saved in my_message.txt")
