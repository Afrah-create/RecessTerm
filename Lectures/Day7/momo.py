class MobileMoney:
    def __init__(self):
        self.__balance = 0
    def deposit(self, amount):
        self.__balance += amount
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient balance.")
    def showBalance(self):
        print(f"Your balance is: {self.__balance}")
user1 = MobileMoney()
user1.deposit(5000)
user1.withdraw(2000)
user1.showBalance()