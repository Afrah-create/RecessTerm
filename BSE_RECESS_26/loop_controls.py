# Loop control Statements
# Loop control statements are used to alter the flow of a loop. They allow you to skip
# certain iterations or exit the loop entirely based on specific conditions. The main loop control statements in Python are:
# 1. break: Exits the loop immediately, regardless of the loop's condition.
# 2. continue: Skips the current iteration and moves to the next iteration of the loop.
# 3. pass: Does nothing and is used as a placeholder when a statement is required 
# syntactically but you don't want to execute any code.


# else is required syntactically but you don't want to execute any code.

# Example 6: Using break to exit a loop when a condition is met
# for num in range(1, 11):
#     if num == 4:
    
#         break  # Exit the loop when number 5 is found
#     print(num)

# Example 7: Using continue to skip an iteration when a condition is met
# Skipping even numbers
for num in range(1, 11):
    if num % 2 == 0:
        continue  # Skip the rest of the loop for even numbers
    print(num)


# Example 8: Using pass as a placeholder in a loop
# For future implementation, we will use pass to indicate that we will add code later
for num in range(1, 11):
    if num % 2 == 0:
        pass  # We will add code here later to handle even numbers
    else:
        print(num)  # Print odd numbers for now


# Assigment 3: Real world application of loop control statements:
# Write a program that simulates a simple country that will win world cup 2026. 
# Use a while loop to control the flow of the program and use break, continue,
#  and pass statements to manage the flow of the loop based on user input.
'''


PROBLEM STATEMENT
Scenario
You are the manager of a national football team competing in the 2026 FIFA World Cup. 
Your task is to guide your team through:

Pre-tournament preparation (training, friendlies, recovery)

Group stage matches (3 matches)

Knockout stages (Round of 16, Quarter-final, Semi-final, Final)

Challenge
Using loop control statements, create a simulation where:

User choices affect team performance (morale, injuries, strength)

Loop exits when tournament is won or lost (break)

Certain conditions skip to next iteration (continue)

Placeholders exist for future features (pass)

'''

'''
Loop control statements are essential for managing the flow of a program, especially in scenarios like a football tournament simulation where user choices can affect the outcome. By using break, continue, and pass statements, you can create a dynamic and interactive experience for the user while simulating the various stages of the tournament.

for
while
Nested loops

break
continue
pass

else

if

elif

else


'''