# Nested Condition Example

# What is a nested condition?

# A nested condition is a conditional statement that is contained within 
# another conditional statement.


# It allows you to check multiple conditions in a hierarchical manner.
# For example, you might want to check if a student has passed an exam, 
# and if they have, you might want to check their grade to provide specific 
# feedback.

# LabActivity2: Write a program for Login Authentication that takes a username  
# and password as input and checks if they match a predefined set of credentials. 
# If the credentials are correct, print "Login successful". 
#  If the username is correct but the password is incorrect, 
# print "Incorrect password". If the username is incorrect,
#  print "Username not found".

# Check if user name exists
username = input("Enter your username: ")
password = input("Enter your password: ")

if username == "admin":
    if password == "password123":
        print("Login successful")
    else:
        print("Incorrect password")
else:
    print("Username not found")
