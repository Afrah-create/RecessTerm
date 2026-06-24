# method overriding in a bank account types
class BankAccount:
    def calculate_interest(self, balance):
        return balance * 0.02  # Default interest rate of 2%

class SavingsAccount(BankAccount):
    def calculate_interest(self, balance):
        return balance * 0.05  # Higher interest rate for savings accounts

class CurrentAccount(BankAccount):
    def calculate_interest(self, balance):
        return balance * 0.01  # Lower interest rate for current accounts
