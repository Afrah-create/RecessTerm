# Advanced Functions
# Lambda function
# Recursive Function
# Built in Function
#Function based Projects


# What are Lambda Function?
# is a small function anonymous function defined using the keyword lambda, it has one expression
# Syntax
# lambda arguments: expression

'''
Key Characteristics
-No name(anonymous)
-Single expression
-Return value automatically
-Can be used where function objects are required

'''

# # Lab1 Activity:
# # Simple Lambda function
# # lambda arguments: expression

# square = lambda x: x*x
# print(square(5))


# #Tradition function
# def add(x,y):
#     return x + y

# print(add(5, 3))

# # Lambda equivalent
# add_lambda = lambda x,y: x + y

# print(add(5, 3))

# # Exe1: Write a lambda function to check if number is even

# # Practical Applications

# # Lab2 Activity
# # Using Lambda with filter

# numbers = [4, 7, 10, 15, 20, 30, 35]

# # Filter even numbers
# evens =list(filter(lambda x: x % 2 == 0, numbers))

# print(evens)


# # filter number that is greater than 20

# greater_than_20 = list(filter(lambda x: x > 20, numbers))

# print(greater_than_20)


# # Exe2: Using Lambda with sorted(), arrange using length of the words

# ['Cherry', 'Banana', 'Date', 'Apple', 'Mango', 'DragonFruit']


#Recursive Function
# Understanding Recursion
# What is Recursion?
# Recursion occurs when a function calls itself to solve a problem by breaking it down into smaller
# similar subproblems

# Components of Recusrion
'''
-Base Case: The condition that stops the recursion
-Recursive case: The function call itself with a smaller function


'''

# Lab3 Activity 3: Factorial calculation
#  5! = 5 x 4 x 3 x 2 x 1   #output:120


# Code Snipet

# def factorial(n):
#     #Base base
#     if n <= 1:
#         return 1
    
#     #Recursive case
#     else:
#         return n * factorial(n-1)
    
# print(factorial(5))


# # Method Two
# def factorial(n):
#     if n == 1:
#         return 1
#     return n * factorial(n-1)
# print(factorial(5))

# # Count Down 5 to 1
# def count_down(n):
#     if n == 0:
#         print('Finished')
#     else:
#         print(n)
#         count_down(n-1)

# count_down(10)


#Exe3; Using Fibonancci Sequence get the first 10 fibonacci number in the range of 10


# Fibonacci 
# Fn = Fn-1 + Fn-2

'''
0 + 1 = 1
1 + 1 = 2
1 + 2 = 3
2 + 3 = 5


'''


# Example 5 : Long Code for Searching Binary Algorithm

# (arrange, target, left, right)


def binary_search(arr, target, left, right):
    #Base case: element not found
    if left > right:
        return -1
    
    # Find middle
    mid = (left + right) // 2

    #Base case: element found
    if arr[mid] == target:
        return mid
  
    
    # Recursive cases
    elif arr[mid] > target:
        return binary_search(arr, target, left, mid - 1)
    else:
        return binary_search(arr, target, mid + 1, right)
    
    
# Test the function
sorted_array = [1, 3, 5, 7, 9, 11, 13, 15]

print(binary_search(sorted_array, 7, 0, len(sorted_array) -1))


# Assignment ; Use Function-based Project to create a contact management system

'''
Your Tasks
Your job is to extend the functionality of the ContactManager class by 
implementing the following requirements. Ensure you do not break the existing features.

Task 1: Data Validation (20 Points)
Currently, a user can enter any text for a phone number or email. 
Modify the code to add basic validation:

Phone Validation: In add_contact and update_contact, 
ensure the phone number contains only digits and hyphens (e.g., "+256-701"). 
If it contains illegal characters, print an error message and cancel the operation.

Email Validation: Ensure that if an email is provided, it contains an @ symbol and a . (period).


Task 2: Advanced Search (25 Points)
The current Contacts method only filters by name and phone number.

Modify Contactss so that it can also search by email.

Write a helper method or modify the search printout so it displays the search results in a clean, 
user-friendly format rather than just returning a raw Python list of tuples.


Task 3: Interactive CLI Menu (35 Points)
Create an interactive Command Line Interface (CLI) loop inside a function called main(). 
When run, the program should present the user with a recurring menu until they choose to exit.

The menu should look similar to this:

=== Contact Manager Menu ===CRUD
1. Add Contact
2. View Contact
3. Update Contact
4. Delete Contact
5. Search Contacts
6. List All Contacts
7. Exit
Choose an option (1-7):

Implement proper input handling for each menu item, 
prompting the user for necessary arguments (like name, phone, etc.) 
and passing them to your class methods.

Submission Guidelines:
1. Add a single python script to your github link, 
2. Submit a single Python file named name_contact_assignment.py.
'''