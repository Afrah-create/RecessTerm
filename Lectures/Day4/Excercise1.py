
# user enters length and width
def Area_of_rec():
    length = int(input("Enter the length of the rectange: "))
    width = int(input("Enter the width of the rectangle: "))
    area = length * width
    return area
print("The area of the rectangle is:", Area_of_rec())


# with parameters
def Area_of_rec(length, width):
    area = length * width
    return area
print("The area of the rectangle is:", Area_of_rec(5, 3))


#What is a return statement?
# A return statement is used to exit a function and return a
# value to the caller. It allows you to send a result back to the 
# part of the program that called the function. When a return statement is executed, 
# the function terminates and the specified value is returned to the caller. This is 
# useful for functions that perform calculations or operations and need to provide a 
# result that can be used elsewhere in the program. For example, in the Area_of_rec function, 
# the return statement allows us to get the calculated area and use it in other parts of the program, such as printing it or storing it in a variable.