'''

# tuples
marks = (85, 90, 78, 92, 88)
print("Marks:", marks)
print(type(marks))

# Constructing a tuple using tuple() constructor
new_marks = tuple((75, 80, 85))
print("New Marks:", new_marks)

# looping through the tuple using for loop
for i in range(len(marks)):
    print(marks[i], end=", ")

for i in range(len(new_marks)):
    print(new_marks[i], end=", ")


# Nested tuple
nested_marks = (("Awongo", 90), ("Brenda", 78), ("Caleb", 88))
print("Nested Marks:", nested_marks)
# Accessing elements in a nested tuple
print("First student's marks:", nested_marks[0])
print("Second student's second mark:", nested_marks[1][1])
print("Third student's first name:", nested_marks[2][0])


# converting a list to a tuple
marks_list = [85, 90, 78, 92, 88]
marks_tuple = tuple(marks_list)
print("Marks Tuple:", marks_tuple)


# accessing elements in a tuple using negative indexing
print("Last mark:", marks[-1])
print("Second to last mark:", marks[-2])
print("Third to last mark:", marks[-3])


# deleting a tuple
del marks


'''
# concatenating two tuples
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
result = tuple1 + tuple2
print("Concatenated Tuple:", result)

modified = list(result)
modified.append(7)
result = tuple(modified)
print("Modified Tuple:", result)