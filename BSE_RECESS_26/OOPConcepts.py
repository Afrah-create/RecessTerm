# Encapsulation
# Abstraction
# Inheritance
# Polymorphism

# Introduction to Encapsulation
# What is Encapsulation

# Why Encapsulation?

# Real World Examples
# Lab Activity One
# Student, name, reg_Number, Gender, Student-Number, Age, 

class Student:
    def __init__(self, name, age, student_number):
        self.name = name
        self.age = age
        self.student_number = student_number

student_1 = Student('Peter', 24, 240000717)

print(student_1.name)
