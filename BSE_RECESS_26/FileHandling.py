# MODULE: FILE HANDLING, DATA PROCESSING, EXCEPTION HANDLING, LOGGING AND DEBUGGING

'''
Outcomes
- Read data from a file
-Append data to file
- Process CSV file
-Read and Write JSON file


'''
# FILE HANDLING

# COMMON FILES TYPES
'''
- Text file (.txt)
- CSV file (.csv)
- JSON file (.json)
- Excel file (.xlsx)

'''

# Opening a file

# Syntax
# file = open(filename, mode)


'''
Mode              Meaning
r                 Read
w                 Write
a                 Append
x                 Create new file
rb                Read binary
wb                Write binary



'''

# Example1 Read a student.txt file

# file = open("student.txt", "r")

# content = file.read()

# print(content)

# file.close()


# Recommended method
# 'with' automatically closes the file

# with open('student.txt', 'r') as file:
#     data = file.read()

# print(data)


# Reading Line by Line
# with open('student.txt', 'r') as file:
    
#     # Read one line at a time
#     for line in file:
#         print(line.strip())


# Lab Exercise 1: Write a file with the conten 'I love Python Programming' first line,
# ' I am becoming a data Scientist' , second line. , save your file as report.txt

# Appending a file , use the sample report.txt append
# append ' Every Data Scientist Must learn python'


# Real World Example
# Attendance System
# Live Demo

# name = input('Enter Student: ')
# with open('attendance.txt', 'a') as file:
#     # Save
#     file.write(name + '\n')
# print('Attendance Saved Successfully')


# Work with a CSV File
# What is CSV? Comma Seprated Values

# Reading a CSV File

# import csv

# # Open CSV File
# with open('students.csv', 'r') as file:
#     reader = csv.reader(file)

#     # loops through each row 
#     for row in reader:
#         print(row)

# Lab activity add your ['RegistrationNo', 'Name', 'Gender', 'Age', 'Course', 'Score'] 
# to the students.csv, using a dictionary csv writer


# JSON PROCSSING 

# What is JSON (), JavaScript Object Notation
'''
JSON Format
{
    "name": "Jeff"
    "Age":  "24"
    "Course": "Python"
}

'''
# Writing a JSON file
import json

student = {
    "name": "Jeff",
    "Age":  "24",
    "Course": "Python"
}

with open('student.json', 'w') as file:
    json.dump(student,file,indent=4)

print('JSON file created successfully')