# Data Hiding
# Real World Bank Account, (Balance, deposit, )

class BankAccount:
    def __init__(self):
        self.__balance = 1000000
    
    # def deposit(self, amount):
    #     self.__balance += amount
    
    def show_balance(self):
        return self.__balance
    
acc = BankAccount()
# acc.deposit(500000)
# acc.deposit(100000)
print(acc.show_balance())


# Exercise 2: Create a Class MobileMoney, with attributes __balance, method, deposit, withdraw, 
# check_balance, Test your application to show balance after withdraw

