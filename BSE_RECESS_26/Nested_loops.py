# Nested loops: A loop inside another loop is called a nested loop. The inner loop will be executed for each iteration of the outer loop.   
# Example: Print a multiplication table from 1 to 5 using nested loops
for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i} x {j} = {i * j}")
    print()  # Print a new line after each row of the multiplication table

# Example 4:  Print a pattern using nested loops
# Pattern:
# *
# **
# ***
# ****

for i in range(1, 5):
    for j in range(i):
        print("*", end="")
    print()  # Print a new line after each row of the pattern


# Exercise 4: Write a program that uses nested loops to print a pattern of numbers.
#  For example, the output should look like this:
1
12
123
1234
12345