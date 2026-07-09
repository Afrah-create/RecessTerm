#Introduction to Control Structures

# What are control structures?
# Control structures are programming constructs that allow you to control the 
# flow of your program. 
# They enable you to make decisions, repeat actions, and manage the execution of
#  your code based on certain conditions.

# Types of Control flow structures
# 1. Conditional Statements (if, elif, else) #Selective
# 2. Loops (for, while) #Iterative
# 3. Sequencing (the order of execution of statements) #Sequential
# 4. Functions #Modular
#5. Switch-case (not available in Python, but can be simulated using if-elif-else)
# 
# Why Conditional Statements?
# Conditional statements allow you to execute different blocks of code based on
# certain conditions. This is essential for making decisions in your program.
# For example, you might want to check if a user is old enough to access a
# website, or if a number is positive, negative, or zero.
#Handle different user inputs, perform different actions based on conditions, and create more
# Implementing busines rules in your code.
# Create inelligent programs that can adapt to different situations.

# The if statement
# The if statement is used to execute a block of code if a specified condition is true.
# Syntax:

# Voting and driving age example
age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote.")
elif age >= 18:
    print("You are also eligible to drive.")
elif age >= 18:
    print("You are allowed to get National ID.")
else:
    print("You are not eligible to vote or drive.")

# Lab1Exe1: Write a program that takes a number as input and 
# checks if it is positive, negative, or zero.

# LabActivity2: Grading System that takes a student's score as input and assigns 
# a grade based on the following criteria:
# 90-100: A
# 80-89: B
# 70-79: C
# 60-69: D
# Below 60: F
score = int(input("Enter the student's score: "))

if score >= 90:
    grade = "A"
    message = "Excellent work!"
elif score >= 80:
    grade = "B"
    message = "Good work!"
elif score >= 70:
    grade = "C"
    message = "Satisfactory work!"
elif score >= 60:
    grade = "D"
    message = "You need to improve."
else:
    grade = "F"
    message = "Failed."

print(f"The student's grade is: {grade}")   
print(message)