'''
def student_records(name, age, regNo, course):
    name = input("Enter Your Name: ")
    age = int(input("Enter Your Age: "))
    regNo = input("Enter Your Registration Number: ")
    course = input("Enter Your Course: ")
    return f"Name: {name}, Age: {age}, Registration Number: {regNo}, Course: {course}"
print(student_records("name", "age", "regNo", "course"))


'''



# Difference between return and print statements
# A return statement is used to exit a function and return a value to the caller, while
# a print statement is used to display output to the console. The return statement allows you to send a result back to the part of the program that called the function, while the print statement simply outputs information to the console without affecting the flow of the program. For example, in the student_records function, the return statement allows us to get the formatted string with the student's information and use it elsewhere in the program, while a print statement would only display the information without allowing us to use it in other parts of the program.

def calculate(num1, num2):
    return num1 + num2, num1 - num2, num1 * num2, num1 / num2
result = calculate(10, 5)
print("Addition:", result[0])
print("Subtraction:", result[1])
print("Multiplication:", result[2])
print("Division:", result[3])



