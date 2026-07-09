# Exercise 3: Write a program that uses a while loop to demonstrate a Bank Account Balance.
#  The program should allow the user to deposit and withdraw money until the balance is zero.

balance = 1000  # Initial balance

while balance > 0:
    print(f"Current balance: ${balance}")
    action = input("Do you want to deposit or withdraw? (deposit/withdraw): ").lower()
    
    if action == "deposit":
        amount = float(input("Enter the amount to deposit: "))
        balance += amount
        print(f"You deposited ${amount}.")
    elif action == "withdraw":
        amount = float(input("Enter the amount to withdraw: "))
        if amount > balance:
            print("Insufficient funds. You cannot withdraw that amount.")
        else:
            balance -= amount
            print(f"You withdrew ${amount}.")
    else:
        print("Invalid action. Please enter 'deposit' or 'withdraw'.")



