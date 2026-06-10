Admin_password = "admin@afrah"
Cashier_password = "cashier@afrah"
customer_password = "customer@afrah"
def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    
    if username == "admin" and password == Admin_password:
        print("Welcome, Admin!")
        # Admin functionalities can be added here
    elif username == "cashier" and password == Cashier_password:
        print("Welcome, Cashier!")
        # Cashier functionalities can be added here
    elif username == "customer" and password == customer_password:
        print("Welcome, Customer!")
        # Customer functionalities can be added here
    else:
        print("Invalid username or password. Please try again.")
login()