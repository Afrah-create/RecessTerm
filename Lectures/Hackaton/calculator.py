"""
Idea 4: The "Error-Proof" Calculator API
Focus: Exceptions, Decorators, and Error Handling
"""

import functools


# Custom Exception + @validate_inputs decorator

class InvalidInputError(Exception):
    """Custom error for when inputs are not numbers."""
    pass


def validate_inputs(func):
    """Checks that both arguments are numbers before running the function."""
    @functools.wraps(func)
    def wrapper(a, b):
        if not isinstance(a, (int, float)):
            raise InvalidInputError(f"'{a}' is not a number.")
        if not isinstance(b, (int, float)):
            raise InvalidInputError(f"'{b}' is not a number.")
        return func(a, b)
    return wrapper


# @safe_divide decorator + logging to file

def safe_divide(func):
    """Returns a math error message instead of crashing when dividing by zero."""
    @functools.wraps(func)
    def wrapper(a, b):
        if b == 0:
            return "Math Error: You cannot divide by zero."
        return func(a, b)
    return wrapper


def log_to_file(func_name, a, b, result):
    """Saves every calculation to log.txt."""
    with open("log.txt", "a") as f:
        f.write(f"{func_name}({a}, {b}) = {result}\n")


def log_call(func):
    """Logs the function name, arguments, and result after every call."""
    @functools.wraps(func)
    def wrapper(a, b):
        result = func(a, b)
        log_to_file(func.__name__, a, b, result)
        return result
    return wrapper


# add() and subtract()

@log_call
@validate_inputs
def add(a, b):
    return a + b


@log_call
@validate_inputs
def subtract(a, b):
    return a - b


# multiply() and divide()

@log_call
@validate_inputs
def multiply(a, b):
    return a * b


@log_call
@validate_inputs
@safe_divide
def divide(a, b):
    return a / b


# Testing Harness (interactive loop)

def get_number(prompt):
    """Asks the user for a number and converts it. Returns None if invalid."""
    raw = input(prompt)
    try:
        return float(raw)
    except ValueError:
        return raw 


def main():
    print("=== Error-Proof Calculator ===")
    print("Operations: 1. add, 2. subtract, 3. multiply, 4. divide")
    print("Enter 'q' to exit\n")

    while True:
        operation = input("Enter operation: ").strip().lower()

        if operation == "q":
            print("Goodbye!")
            break

        if operation not in ("1", "2", "3", "4"):
            print("  Unknown operation. Choose: 1. add, 2. subtract, 3. multiply, 4. divide\n")
            continue

        a = get_number("Enter first number : ")
        b = get_number("Enter second number: ")

        try:
            if operation == "1":
                result = add(a, b)
            elif operation == "2":
                result = subtract(a, b)
            elif operation == "3":
                result = multiply(a, b)
            elif operation == "4":
                result = divide(a, b)

            print(f"  Result: {result}\n")

        except InvalidInputError as e:
            print(f"  Input Error: {e}\n")


if __name__ == "__main__":
    main()