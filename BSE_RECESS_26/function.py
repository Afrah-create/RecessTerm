'''
Functions in Python

Defining Functions
Parameters and Arguments
Return Statements
Scope of Variables

'''
# What is a function?
# A function is a reusable block of code that performs a specific task. 
# It allows you to organize your code into smaller, manageable pieces and promotes code reusability.

# Why use functions?
# Functions help break down complex problems into smaller, more manageable parts.
# They allow you to reuse code, which can save time and reduce errors.
# Functions can also improve the readability of your code by giving meaningful names to blocks of code.
# Simplify debugging and testing by isolating specific functionality.

# Syntax of a function
# def function_name(parameters):
#     # Function body
#     return value

# Built-in functions
# Python provides a wide range of built-in functions that you can use without needing to define them yourself. Some common built-in functions include:
# print(): Used to display output to the console.
# len(): Returns the length of an object (e.g., string, list).
# type(): Returns the type of an object.
# input(): Used to take user input from the console.
# range(): Generates a sequence of numbers, often used in loops.    

# Example of built-in function
# print("Hello, World!")  # This will print "Hello, World!" to the console.
# len("Hello")  # This will return 5, which is the length of the string "Hello".

#Defining a function
# Example 2: Syntax of a function
# def function_name(parameters):
#     # Function body
#     return value

# Components of a function
# Function Name: The name you give to your function, which should be descriptive of its purpose.
# Parameters: Variables that you define in the function definition to accept input values when the function is called.
# Function Body: The block of code that performs the task of the function. It is indented under the function definition.
# Return Statement: A statement that specifies the value to be returned by the function. 
# Indentation: The code inside the function must be indented to indicate that it belongs to the function body.

#Lab Activity 1: Simple Function Example
# def greet():
#     print("Welcome to the Python Programming!")

# #Calling the function
# greet()  # This will call the greet function and print "Welcome to the Python Programming
# greet()  # You can call the function multiple times to reuse the code.
# greet()

# Lab Activity2: Mathematical Function
# Square of Number num = 5

def square_number():
    num = 5
    square = num * num 
    print(square)

#Calling the function
square_number()



# Exercise 1: Write a function that takes in input and culculate area of a Rectangle

# Parameter and Argument

# What is a Parameter?
# Variables listed inside the function definition

# Example
def greet_user(name):
    print(f'My name is', name)


# Arguments
# What are Arguments?
# Arguments are actual values passed to a function

# Example
# greet("Sam Mukisa")

# A function with a single parameter
def greet(name):
    print(f'My name is', name)

greet('Mukisa Sam')


# Multiple Parameters

def add_numbers(a, b):
    print(a + b)

add_numbers(10, 2)


# Exe 2: Create a program that uses function to display student information, your ouput should
# dispay , Name, Age, Course, StudentNumber.


# Lab Activity
# Positional Arguments
# Example
def display(name, age=18):
    print(name)
    print(age)#

display(name='Sulinna', age=22)



# Keyword Arguments
# What is a Keyword Arguments?
# Arguments that can be specified using parameter name


# Default Parameter
# What is a default parameter?
# is assigned if no argument is provided

def greet(name='Tom'):
    print(f'Hello', name)


greet()
greet('Petra')



# Return Statements
#What is a return statement?
# sends a value back to the caller
# Example Syntax
# def function_name():
#     return value


# Lab Activity
def add(a,b):
    return a * b

result = add(5 * 10)

print(result)


# Difference between print() and return

# print() the value cannot be reused easily, returbn you can easil reuse the value

def add(a, b):
    print(a + b)

add(5, 4)


# Return Multiple Return

def calculate(a, b):
    return a+b , a-b
sum_result, diff_result = calculate(20, 15)

print(sum_result)
print(diff_result)


# Scope of a Variable and the types

# What is variable scope?

# Exe3; Create a function that calulates the area of a circle.

#Exe4: Write a program demonstrating the difference between local and global variable:


#Assignment3: Create a menu-driven(GUI) calculator using function for addition, substraction, 
# multiplication, and division