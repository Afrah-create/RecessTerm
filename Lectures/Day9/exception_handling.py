'''
Exception Handling
1. Division by Zero
2. File Not Found
3. Invalid Input
4. Index Out of Range


'''

try:
    num1 = 1
    num2 = 0
    result = num1 / num2
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
finally:
    print("Execution completed.")

class InsufficientFunds(Exception):
    pass
balance = 200000
amount = input("Enter the amount to withdraw: ")
try:
    amount = float(amount)
    if amount > balance:
        raise InsufficientFunds("Insufficient balance.")
    balance -= amount
    print("Withdrawal successful. Remaining balance:", balance)
except InsufficientFunds as e:
    print("Error:", str(e))