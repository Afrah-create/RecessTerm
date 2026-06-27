'''
Assignment
Student Record Management System
Develop a menu-driven Python application that demonstrates all concepts covered in this lesson.

The system should:

Store student records in a CSV file.
Save additional student details (e.g., address, contact, program) in a JSON file.
Allow users to: Add a new student. View all students. Search for a student by registration number. Update student details. Delete a student record.
Handle all possible errors using try, except, finally, and at least one custom exception.
Log all user actions and system errors to a log file (student_system.log).
Include clear comments throughout the code, user-friendly prompts, and appropriate input validation.
Submission Requirements

Python source code (student_management.py)
Sample students.csv
Sample students.json
Generated student_system.log
A short report (1–2 pages) explaining the program design, key functions, exception handling strategy, and testing results.

'''
import csv
import json
import os



student_records = []
contact_details = {}
def menu():
    print("Welcome to the Student Record Management System")
    print("1. Add a new student")
    print("2. View all students")
    print("3. Search for a student by registration number")
    print("4. Update student details")
    print("5. Delete a student record")
    print("6. Exit")
    return input("Please select an option: ")
def add_student():
    file_name = 'students.csv'
    contact_file = 'students.json'
    try:
        with open(file_name, 'a') as file:
            reg_no = input("Enter registration number: ")
            name = input("Enter student name: ")
            age = int(input("Enter student age: "))
            address = input("Enter student address: ")
            contact = input("Enter student contact: ")
            program = input("Enter student program: ")
            file.write(f"{reg_no},{name},{age},{address},{contact},{program}\n")
            contact_details[reg_no] = {'address': address, 'contact': contact, 'program': program}
            with open(contact_file, 'a') as json_file:
                json.dump(contact_details, json_file)
            print("Student added successfully.")
    except Exception as e:
        print(f"An error occurred while adding the student: {e}")
    

def view_students():

    file_name = 'students.csv'
    try:
        with open(file_name, 'r') as file:
            reader = csv.reader(file)
            print("Registration Number | Name | Age | Address | Contact | Program")
            for row in reader:
                print(" | ".join(row))
    except FileNotFoundError:
        print("No student records found.")
    except Exception as e:
        print(f"An error occurred while viewing students: {e}")


def search_student():
    file_name = 'students.csv'
    reg_no = input("Enter registration number to search: ")
    try:
        with open(file_name, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == reg_no:
                    print("Student found:")
                    print("Registration Number | Name | Age | Address | Contact | Program")
                    print(" | ".join(row))
                    return
            print("Student not found.")
    except FileNotFoundError:
        print("No student records found.")
    except Exception as e:
        print(f"An error occurred while searching for the student: {e}")

def update_student():
    file_name = 'students.csv'
    reg_no = input("Enter registration number to update: ")
    try:
        updated = False
        with open(file_name, 'r') as file:
            reader = list(csv.reader(file))
        with open(file_name, 'w', newline='') as file:
            writer = csv.writer(file)
            for row in reader:
                if row[0] == reg_no:
                    name = input("Enter new student name: ")
                    age = int(input("Enter new student age: "))
                    address = input("Enter new student address: ")
                    contact = input("Enter new student contact: ")
                    program = input("Enter new student program: ")
                    writer.writerow([reg_no, name, age, address, contact, program])
                    updated = True
                else:
                    writer.writerow(row)
        if updated:
            print("Student details updated successfully.")
        else:
            print("Student not found.")
    except FileNotFoundError:
        print("No student records found.")
    except Exception as e:
        print(f"An error occurred while updating the student: {e}")
# main entrance
while True:
    choice = menu()
    if choice == '1':
        add_student()
    elif choice == '2':
        view_students()
 
    elif choice == '3':
        search_student()
        break
    elif choice == '4':
        update_student()
    elif choice == '6':
        print("Exiting the application.")
        break
    else:
        print("Invalid option. Please try again.")