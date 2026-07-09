# Login Authentication System Example

def login_system():
    print("Welcome to the Login System")

    # Predefined credentials (in real app, use a database)
    users = {
        "Admin": "password123",
        "Technician": "pass456",
        "Farmer": "pass789"
    }

    # Attempt to login
    max_attempts = 3
    attempts = 0

    while attempts < max_attempts:
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        # Check if user name exists
        if username in users:
            if users[username] == password:
                print("Login successful")
                return True
            else:
                print("Incorrect password")
        else:
            print("Username not found")

        attempts += 1
        print(f"Attempt {attempts} of {max_attempts}")
    print("Maximum login attempts reached. Access denied.")
    return False
login_system()

#Real world application using control structures
# Assignment2 : Create a E-commerce that checks inputs like subtotal, discount, 
# and tax to calculate the final price of a product. 
# Include the coupon code for discount and tax rate for the calculation.
# Use nested conditions to handle different scenarios such as valid/invalid 
# coupon codes,
# different tax rates based on location, and various discount levels based on 
# the subtotal amount.
# Implement login system for the e-commerce platform that checks user credentials
#  and in the system, there are three types of users: Admin, Customers, and Cashiers.
#  Each user has his password and different access levels. 
# Admin can access all features, Customers can
