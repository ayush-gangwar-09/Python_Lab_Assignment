# Question 4: Create a bank account with custom exceptions.


class InsufficientBalanceError(Exception):
    pass


class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than zero.")
        self.balance = self.balance + amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than zero.")
        if amount > self.balance:
            raise InsufficientBalanceError("You do not have enough balance.")
        self.balance = self.balance - amount

    def show_balance(self):
        print("Account holder:", self.owner)
        print("Balance:", self.balance)


account = BankAccount(input("Enter account holder name: "), 1000)

try:
    amount = float(input("Enter amount to withdraw: "))
    account.withdraw(amount)
    print("Withdrawal successful.")
except InsufficientBalanceError as error:
    print("Bank error:", error)
except ValueError as error:
    print("Input error:", error)

account.show_balance()
