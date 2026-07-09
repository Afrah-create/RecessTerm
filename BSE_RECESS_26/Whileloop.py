# The While Loop?
# What is a while loop?
'''
A while loop executes a block of code as long as the specified condition is true. 

A while loop is a control flow statement that allows code to be executed repeatedly based on a given Boolean condition.
The while loop will continue to execute as long as the condition is true. Once the condition becomes false, the loop will stop.
'''

# Example 1: Count from 1 to 5 using a while loop
count = 1
while count <= 5:
    print(count)
    count += 1  # Increment the count to avoid an infinite loop


# Example 2: Password PIN reset attempts
correct_pin = "1234"
attempts = 0
max_attempts = 3
while attempts < max_attempts:
    entered_pin = input("Enter your PIN: ")
    if entered_pin == correct_pin:
        print("PIN accepted. You can reset your password.")
        break  # Exit the loop if the PIN is correct
    else:
        attempts += 1
        print(f"Incorrect PIN. You have {max_attempts - attempts} attempts left.")
else:
    print("Too many incorrect attempts. Your account is locked.")


