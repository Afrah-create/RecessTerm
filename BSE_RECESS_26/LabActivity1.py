# LabActivity2: Grading System that takes a student's score as input and assigns 
# a grade based on the following criteria:
# 90-100: A
# 80-89: B
# 70-79: C
# 60-69: D
# Below 60: F
score = int(input("Enter the student's score: "))

if score >= 90:
    grade = "A"
    message = "Excellent work!"
elif score >= 80:
    grade = "B"
    message = "Good work!"
elif score >= 70:
    grade = "C"
    message = "Satisfactory work!"
elif score >= 60:
    grade = "D"
    message = "You need to improve."
else:
    grade = "F"
    message = "Failed."

print(f"The student's grade is: {grade}")   
print(message)

# Switch-case example using case   on grade user enters a score and outputs the corresponding grade and message
# 90-100: A
# 80-89: B
# 70-79: C
# 60-69: D
# Below 60: F
score = int(input("Enter the student's score: "))

match score:
    case score if score >= 90:
        grade = "A"
        message = "Excellent work!"
    case score if score >= 80:
        grade = "B"
        message = "Good work!"
    case score if score >= 70:
        grade = "C"   
        message = "Satisfactory work!"
    case score if score >= 60:
        grade = "D"
        message = "You need to improve."
    case _:
        grade = "F"
        message = "Failed."
print(f"The student's grade is: {grade}")   
print(message)  



