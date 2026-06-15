'''
marks = [85, 90, 78, 92, 88]
print("Marks:", marks)
print(type(marks))

# inserting a new mark at index 2
marks.insert(2, 95)
print("Updated Marks:", marks)

#updating the mark at index 3
marks[3] = 89
print("Updated Marks after changing index 3:", marks)


# removing the mark at index 1
del marks[1]
print("Updated Marks after removing index 1:", marks)


# Constructing a list using list() constructor
new_marks = list((75, 80, 85))
print("New Marks:", new_marks)

# looping through the list using for loop
for i in range(len(marks)):
    print(marks[i], end=", ")

for i in range(len(new_marks)):
    print(new_marks[i], end=", ")

'''
# Nested list
nested_marks = [[67, 90], [78, 80], [88, 85]]
print("Nested Marks:", nested_marks)
# Accessing elements in a nested list
print("First student's marks:", nested_marks[0])
print("Second student's second mark:", nested_marks[1][1])
print("Third student's first mark:", nested_marks[2][0])