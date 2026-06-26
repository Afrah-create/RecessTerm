file_name = "output.txt"
text = "Hello, this is a sample text to be written to the file."
with open(file_name, "w") as file:
    file.write(text)
print(f"Text has been written to {file_name}.")

with open("output.txt", "r") as file:
    content = file.read()
print("Content of the file:")
print(content)


import os
import csv
csv_file_name = "data.csv"
data = [
    ["Name", "Age", "City"],
    ["Alice", 30, "New York"],
    ["Bob", 25, "Los Angeles"],
    ["Charlie", 35, "Chicago"]
]
with open(csv_file_name, "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(data)
print(f"CSV data has been written to {csv_file_name}.")


# cophying the content of output.txt to a new file
new_file_name = "copied_output.txt"
with open(file_name, "r") as source_file:
    content = source_file.read()
with open(new_file_name, "w") as dest_file:
    dest_file.write(content)
print(f"Content of {file_name} has been copied to {new_file_name}.")


# using shutil to copy the file
import shutil
shutil.copy(file_name, "shutil_copied_output.txt")
print(f"Content of {file_name} has been copied to shutil_copied_output.txt using shutil.")
