# Question 6: Build a small library system using classes and inheritance.


class LibraryItem:
    def __init__(self, title):
        self.title = title
        self.is_issued = False

    def issue(self):
        if self.is_issued:
            print(self.title, "is already issued.")
        else:
            self.is_issued = True
            print(self.title, "has been issued.")

    def return_item(self):
        if not self.is_issued:
            print(self.title, "was not issued.")
        else:
            self.is_issued = False
            print(self.title, "has been returned.")


class Book(LibraryItem):
    def __init__(self, title, author):
        super().__init__(title)
        self.author = author

    def show_details(self):
        print("Title:", self.title)
        print("Author:", self.author)
        print("Status:", "Issued" if self.is_issued else "Available")


book = Book(input("Enter book title: "), input("Enter author name: "))

while True:
    print("\n1. Show book details")
    print("2. Issue book")
    print("3. Return book")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        book.show_details()
    elif choice == "2":
        book.issue()
    elif choice == "3":
        book.return_item()
    elif choice == "4":
        break
    else:
        print("Invalid choice.")
