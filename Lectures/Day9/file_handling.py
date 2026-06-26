'''
file handling modes
r ==== read
w ==== write
a ==== append
x ==== create
b ==== binary


'''

import os


#file_path = os.path.join(os.getcwd(), "student.txt")
#file = open(file_path, "r")
#content = file.read()
#print(content)
#file.close()

with open("student.txt", "r") as file:
    content = file.read()
    print(content)

# reading a file line by line
with open("student.txt", "r") as file:
    for line in file:
        print(line.strip())