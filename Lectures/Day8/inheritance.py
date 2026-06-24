class Animal:
    def __init__(self, name, species, sound):
        self.name = name
        self.species = species
        self.sound = sound

    def move(self):
        pass

    def sound(self):
        pass

class Dog(Animal):
    def __init__(self, name):
        self.name = name
        super().__init__(name, "Dog", "Woof!")
class Cat(Animal):
    def __init__(self, name):
        self.name = name
        super().__init__(name, "Cat", "Meow!")
dog = Dog("Buddy")
cat = Cat("Whiskers")
print(dog.move())
print(cat.move())