import json

student = {
    "name": "awongo",
    "age": 20,
    "gender": "male",
}

with open("student.json", "w") as file:
    json.dump(student, file)
print("JSON file created successfully.")