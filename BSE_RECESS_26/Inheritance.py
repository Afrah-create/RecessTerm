# Inheritance
# What is Inheritance?
'''
Parent/Super/Base class

Child/sub/Derived class

'''

# Parent Class
class Person:
    def __init__(self, name):
        self.name = name
    
    def display(self):
        print('Name: ', self.name)

# Child Class
class Student(Person):
    def study(self):
        print(' I am studying python')

student = Student('Patience')

student.display()
student.study()