# EXCEPTION HANDLING
# Examples
'''
Division by Zero
File not found
Invalid input
Indx out of range

'''

# Code, try, catch, finally

# try block

# try:
#     number = int(input('Enter number: '))
#     result = 100/number
#     print(result)
# except ZeroDivisionError:
#     print('Cannot divide by zero')

# except ValueError:
#     print('Invalid number enetered.')



# Finally Block: executes whether an error occurs or not

# Lab Reading a file

# try:
#     file = open('student.json')
#     print(file.read())

# except FileNotFoundError:
#     print('File Missing')

# finally:
#     print('Finhished opening')


# Real World Example
# ATM Withdrawal

# class InsufficientBalance(Exception):
#     pass

# balance = 2000000
# withdraw = int(input("Amount: "))

# try:
#     if withdraw > balance:
#         raise InsufficientBalance('Insufficient Funds')
    
#     balance -= withdraw

#     print(' Remaining Balance: ', balance)

# except InsufficientBalance as error:
#     print(error)


# Exercise 3: Write a custom execeptions for a Ugandan to Drive a car, "Must be 18 years or older"
# class AgeError(Exception):

#     pass

# age = int(input("Enter Age: "))

# try:

#     if age < 18:

#         raise AgeError("Must be 18 years or older.")

#     print("Access Granted")

# except AgeError as error:

#     print(error)

##

## Debugging 
# What is Debugging? is process of finding and fixing program errors 

# Common Errors
# -SyntaxErrors -
# -Runtime Errors -
# -Logical Errors -


# Example 4:

# Grade Mark is = 70 , "A"

# Wrong

# Print Debugging

# number = [2, 4, 6, 8, 10]

# print('Current List', number)

# for n in number:
#     print('Current Number: ', n)

# Basic Errors
# Logging Systems

import logging
logging.basicConfig(
    filename='system.log',
    level=logging.INFO
)

logging.info('Application Started')
logging.warning('Low Memory')
logging.error('Database connection Failed')

'''

Assignment
Student Record Management System

Develop a menu-driven Python application that demonstrates all concepts covered in this lesson.

The system should:

Store student records in a CSV file.
Save additional student details (e.g., address, contact, program) in a JSON file.
Allow users to:
Add a new student.
View all students.
Search for a student by registration number.
Update student details.
Delete a student record.
Handle all possible errors using try, except, finally, and at least one custom exception.
Log all user actions and system errors to a log file (student_system.log).
Include clear comments throughout the code, user-friendly prompts, and appropriate input validation.

Submission Requirements

Python source code (student_management.py)
Sample students.csv
Sample students.json
Generated student_system.log
A short report (1–2 pages) explaining the program design, key functions, exception handling strategy, and testing results.

'''