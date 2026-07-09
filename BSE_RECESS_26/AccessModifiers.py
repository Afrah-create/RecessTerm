# Access Modifiers
# Python Supports Three access modifiers
'''
Python Supports Three access modifiers
- Public, accessible everywhere
- Protected, accessible within the class and subclass
-Private , accessible only inside the class

'''

# Example Access modifiers

# Employee Example, name, salary, age
# Public Name
class Employee:
    def __init__(self):
        self.name = 'Peter'

emp = Employee()

print(emp.name)


# Protect Salary
class Employee:
    def __init__(self):
        self._salary = 600000

emp = Employee()

#print(emp._salary)

# Private Salary
class Employee:
    def __init__(self):
        self.__salary = 600000

emp = Employee()

#print(emp.__salary)


#Exercise : Create a class called car with, brand, model, price then make brand public, 
# model protected, price private, Display all values appropriately