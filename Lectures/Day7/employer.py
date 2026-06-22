class Employee:
    def __init__(self):
        self.firstName = ""
        self.lastName = ""
        self.age = 0
        self.address = ""
# protected attribute        self._salary = 0
    def describeEmployee(self):
        print(f"This is {self.firstName} {self.lastName} and am {self.age} years old. Lives in {self.address}.")
    def greetEmployee(self):
        print(f"Welcome {self.firstName} {self.lastName}!")
employee1 = Employee()
employee1.firstName = "Afrah"
employee1.lastName = "Rashid"
employee1.age = 25
employee1.address = "Kampala"
employee1.describeEmployee()
employee1.greetEmployee()