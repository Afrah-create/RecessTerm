#without a loop
'''
print("1")
print("2")
print("3")
print("4")
print("5\n")

#with a loop
for i in range(1,6):
    print(f"Day{i}: Python")

for num in range(1, 11):
    print(num)

    


    print("Even numbers")

for i in range(1, 10):
    if i % 2 ==0:
        print(i)




name = "Kamwada is Tall"

for letter in name:
    print(letter, end=" ")




count = 0
while count < 5:
    print(f"Count: {count}")
    count += 1

'''

account_balance = 1000
while account_balance > 0:

    print(f"Welcome to the bank!. Your current balance is {account_balance}")
    print(f"Choose transaction type: 1. Deposit 2. Withdraw")

    transaction_type = input().lower()
    if transaction_type == "deposit":
        deposit_amount = float(input("Enter the amount to deposit: "))
        account_balance += deposit_amount
        print(f"You have deposited {deposit_amount}. Your new balance is {account_balance}")
    elif transaction_type == "withdraw":
        withdrawal_amount = float(input("Enter the amount to withdraw: "))
        if withdrawal_amount <= account_balance:
            account_balance -= withdrawal_amount
            print(f"You have withdrawn {withdrawal_amount} and your remaining balance is {account_balance}")
        else:
            print("Insufficient funds.")
    print(f"Do you want to make another transaction? (yes/no) ")
    response = input().lower()
    if transaction_type == "deposit":
        deposit_amount = float(input("Enter the amount to deposit: "))
        account_balance += deposit_amount
        print(f"You have deposited {deposit_amount}. Your new balance is {account_balance}")
    elif transaction_type == "withdraw":
        if withdrawal_amount <= account_balance:
            account_balance -= withdrawal_amount
            print(f"You have withdrawn {withdrawal_amount} and your remaining balance is {account_balance}")
        else:
            print("Insufficient funds.")
    if response != "yes":
        print("Thank you for banking with us!")
        break