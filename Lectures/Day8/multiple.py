class class1:
    def display(self):
        print("This is class1")
class class2(class1):
    def display(self):
        print("This is class2")
class class3(class1):
    def display(self):
        print("This is class3")
class class4(class2, class3):
    pass
obj = class4()
obj.display()
print(class4.__mro__)