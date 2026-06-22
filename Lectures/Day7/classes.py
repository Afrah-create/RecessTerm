class Student:
    def __init__(self, name, age, regNo, course):
        self.name = name
        self.age = age
        self.regNo = regNo
        self.course = course

    # Class method (available to all Student objects)
    def printDetails(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Registration Number: {self.regNo}")
        print(f"Course: {self.course}")
        
# Create an object
std1 = Student("Awongo", 20, "24/U/2279822", "Software Engineering")

# Object attributes
std1.department = "Networks Department"
std1.dob = "01/12/2002"

# Object method
def greet():
    print(f"Hello, {std1.name}! Welcome to {std1.department}.")

# Attach the function as an object method
std1.greet = greet

# Call the object method
std1.greet()