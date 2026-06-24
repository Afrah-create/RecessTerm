class Transaction:
    def deposit(self, amount):
        pass
    def withdraw(self, amount):
        pass
    def check_balance(self):
        pass
    def transfer(self, *args):
        pass
    def menu(self):
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Transfer")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            amount = float(input("Enter amount to deposit: "))
            self.deposit(amount)
        elif choice == '2':
            amount = float(input("Enter amount to withdraw: "))
            self.withdraw(amount)
        elif choice == '3':
            self.check_balance()
        elif choice == '4':
            amount = float(input("Enter amount to transfer: "))
            target_account_number = input("Enter target account number: ")
            target_account_holder = input("Enter target account holder name: ")
            target_account = BankAccount(target_account_number, target_account_holder)
            self.transfer(amount, target_account)

    
class BankAccount(Transaction):
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: {amount}. New Balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew: {amount}. New Balance: {self.balance}")
        else:
            print("Insufficient funds or invalid withdrawal amount.")

    def check_balance(self):
        print(f"Current Balance: {self.balance}")

    def transfer(self, *args):
        amount = args[0]
        target_account = args[1]
        if 0 < amount <= self.balance:
            self.balance -= amount
            target_account.deposit(amount)
            print(f"Transferred: {amount} to Account Number: {target_account.account_number}. New Balance: {self.balance}")
        else:
            print("Insufficient funds or invalid transfer amount.")
employee_account = BankAccount("32046342", "Afrah Rashid", 1000)

employee_account.menu()
