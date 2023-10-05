# 2.1 Implement a class called BankAccount that represents a bank account. The class should have private attributes for account number, account holder name, and account balance. Include methods to deposit money, withdraw money, and display the account balance. Ensure that the account balance cannot be accessed directly from outside the class. Write a program to create an instance of the BankAccount class and test the deposit and withdrawal functionality.
class BankAccount:
    def __init__(self, account_number, account_holder_name, initial_balance=0):
        self.__account_number = account_number
        self.__account_holder_name = account_holder_name
        self.__account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
            return True
        else:
            return False  # Negative amounts are not allowed for deposit

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        else:
            return False  # Withdrawal not allowed if the amount is negative or exceeds the balance

    def display_balance(self):
        return f"Account Holder: {self.__account_holder_name}, Account Number: {self.__account_number}, Balance: ${self.__account_balance:.2f}"

# Create an instance of the BankAccount class
account = BankAccount("12345", "John Doe", 1000.00)

# Test deposit and withdrawal functionality
print(account.display_balance())  # Initial balance should be $1000.00

# Deposit $500
if account.deposit(500):
    print("Deposited $500 successfully.")
else:
    print("Invalid deposit amount.")

# Withdraw $200
if account.withdraw(200):
    print("Withdrawn $200 successfully.")
else:
    print("Invalid withdrawal amount.")

# Display the updated balance
print(account.display_balance())  # Updated balance should be $1300.00
