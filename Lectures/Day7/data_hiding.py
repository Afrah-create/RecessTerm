# data hiding
class Bank:
    def __init__(self):
        self.__balance = 100000

    def deposit(self, amount):
        self.__balance += amount
    def showBalance(self):
        print(f"Your balance is: {self.__balance}")
user1 = Bank()
user1.deposit(5000)
user1.showBalance()