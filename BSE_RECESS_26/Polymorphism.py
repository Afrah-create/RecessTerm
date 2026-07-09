# Polymorphism 
# What is Polymorphism?

# Why Polymorphism?
'''
-Default parameters
-Variables length arguments ( *kwargs, *args)
-Type checking within a single method ( Checking data types)

'''

# Example 1
# In  java

# class Calculator {
#     int add( int a, int b)
#     int add(int a, int b, int c)
# }

# Method Overloading 
# What is method overloading?

# In Python 
# Approach 1: Default parameters
class Calculator:
    def add(self, a, b, c):
        return a + b + c
    
# Approach 2: Variable Length Arguments
class Calculator:
    def add(self, *args):
        if len(args) == 2:
            return args[0] + args[1]
        
        elif len(args) == 3:
            return args[0] + args[1] + args[3]
        elif len(args) > 3:
            return sum(args)
        else:
            return 0
        
# Approach 3: Type Checking 
class Calculator:
    def add(self, a, b):
        if isinstance(a, int) and isinstance(b, int):
            return a + b
        elif isinstance(a, float) or isinstance(b, float):
            return float(a) + float(b)
        elif isinstance(a, str) or isinstance(b, str):
            return str(a) + str(b)
        
# Method Overriding
# What is Method Overriding?
#  Key Points
'''
- The method signature ( name and parameter) must match
-super() allow calling the parent method
-Overrriding enable dynamic behaviours at ruturn
'''
# Real World Example:  Bank Account

class BankAccount:
    def calculate_interest(self, balance, rate):
        return balance * rate / 100
    def get_account_type(self):
        return 'Generic Bank Account'

class SavingAccount(BankAccount):
    def calculate_interest(self, balance, rate):
        monthly_rate = rate / 12 / 100
        return balance * ((1+ monthly_rate)**12-1)
    def get_account_type(self):
        return 'Saving Account'
    
class CheckingAccount(BankAccount):
    def calculate_interest(self, balance, rate):
        # Checking Account
        return 0
    
    def get_account_type(self):
        return 'Checking Account'
    
# Lab 1 Exercise 1: Create a method overloading and overriding the completes a banking system
# The parent class must be Transaction and the child class can be deposit, withdrwal and Transfer.
# Demonstrate an employer dpositing, witdrawing and transfering funds.

# Operator Overloading
'''
- Add +, Substract -, Mulitpy *, Division / 

Common Special Methods:
__add__(self, other)
__sub__(self,other)
__mul__(self, other)
__truediv__(self, other)
__str__(self,other)

'''

# Example 3
class Money:
    def __init__(self, amount, currency='UGX'):
        self.amount = amount
        self.currency = currency

    def __add__(self, other):
        if self.currency != other.currency:
            raise ValueError('Cannot add different currencies')
        return Money(self.amount + other.amount, self.currency)

    def __sub__(self, other):
        pass
    def __mul__(self, other):
        pass


# Automation and Webscrapping

# What is Automation in Python?

'''
The Automation Pipeline:

Input -> , Transform -> , Output -> , Reliability -> Run


# Key Libraries for Auomation
Library 
pathlib - file path
shutil - copy , move, archive
Schedule - task Schduling
Watchdog  - File System events monitoring
openpyxl - Excel file read / write


'''
# Example 4 / File Automation
# File Automation # Organising files on our computer
