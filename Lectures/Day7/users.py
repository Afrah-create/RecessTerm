class User:
    firstNmae = ""
    lastName = ""
    def __init__(self, age, address):
        self.age = age
        self.address = address
    def describeUser(self):
        print(f"This is {self.firstNmae} {self.lastName} and am {self.age} years old. Lives in {self.address}.")
    def greetUser(self):
        print(f"Welcome {self.firstNmae} {self.lastName}!")
user1 = User(25, "Kampala")
user1.firstNmae = "Afrah"
user1.lastName = "Rashid"
user1.describeUser()
user1.greetUser()
