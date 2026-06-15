def add():
    print("Enter numbers to add")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    result = num1 + num2
    print(f"The sum of {num1} and {num2} is: {result}")
    iterate()

def subtract():
    print("Enter numbers to subtract")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    result = num1 - num2
    print(f"The difference of {num1} and {num2} is: {result}")
    iterate()

def multiply():
    print("Enter numbers to multiply")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    result = num1 * num2
    print(f"The product of {num1} and {num2} is: {result}")
    iterate()

def divide():
    print("Enter numbers to divide")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    if num2 != 0:
        result = num1 / num2
        print(f"The quotient of {num1} and {num2} is: {result}")
    else:
        print("Error: Division by zero is not allowed.")
    iterate()

def welcome_screen():
    print("Welcome, please select an option:")
    options = ["1. Add", "2. Subtract", "3. Multiply", "4. Divide", "5. Exit"]
    for option in options:
        print(option)
    option = input("Enter your choice (1-5): ")
    if option == "1":
        add()
    elif option == "2":
        subtract()
    elif option == "3":
        multiply()
    elif option == "4":
        divide()
    elif option == "5":
        print("Exiting the program.")
        exit()
    else:
        print("Invalid option, please try again.")



def iterate():
    print("Would you like to perform another operation? (1. yes/2. no)")
    choice = input()
    if choice == "1":
        welcome_screen()
    else:        
        print("Thank you for using the calculator. Goodbye!")
        exit()

welcome_screen()