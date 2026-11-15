# A simple banking system using a class

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance = self.balance + amount
            print("Amount deposited successfully.")
        else:
            print("Please enter an amount greater than zero.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Please enter an amount greater than zero.")
        elif amount > self.balance:
            print("Not enough balance.")
        else:
            self.balance = self.balance - amount
            print("Please collect your cash.")

    def show_balance(self):
        print("Account holder:", self.owner)
        print("Current balance:", self.balance)


name = input("Enter account holder name: ")
account = BankAccount(name)

while True:
    print("\n1. Deposit")
    print("2. Withdraw")
    print("3. Check balance")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        amount = float(input("Enter deposit amount: "))
        account.deposit(amount)
    elif choice == "2":
        amount = float(input("Enter withdrawal amount: "))
        account.withdraw(amount)
    elif choice == "3":
        account.show_balance()
    elif choice == "4":
        print("Thank you for using the banking program.")
        break
    else:
        print("Invalid choice. Try again.")
