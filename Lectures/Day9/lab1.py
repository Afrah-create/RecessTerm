file_name = "report.txt"

first_line = "I love python programming"
second_line = "\n I am becoming a data scientist!"
with open(file_name, "w") as file:
    file.write(first_line)
    file.write(second_line)
