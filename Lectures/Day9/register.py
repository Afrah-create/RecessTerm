
file_name = "Attendance.txt"

name = input("Enter your name: ")
age = input("Enter your age: ")
with open(file_name, "a") as file:
    file.write(f"\n{name} is {age} years old.")

import csv
csv_file = "students.csv"
with open(csv_file, "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)