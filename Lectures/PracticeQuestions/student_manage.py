class Person:
    def __init__(self, name, ID):
        self.name = name
        self.ID = ID

class Student(Person):
    def __init__(self, name, ID, major):
        super().__init__(name, ID)
        self.major = major

    def display_info(self):
        print(f"Name: {self.name}, ID: {self.ID}, Major: {self.major}")

class Lecturer(Person):
    def __init__(self, name, ID, department):
        super().__init__(name, ID)
        self.department = department

    def display_info(self):
        print(f"Name: {self.name}, ID: {self.ID}, Department: {self.department}")


student1 = Student("Awongo", "24/U/3234", "BSSE")
lecturer1 = Lecturer("Dr. Awongo", "EMP-4565", "Networks")

student1.display_info()
lecturer1.display_info()