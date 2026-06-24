class Calculator:
    name = ""
    def add(self, *args):
        return sum(args)
calculator = Calculator()
calculator.name = "my calculator"
print()
print(f"Result: {calculator.add(1, 2, 3)}")  # Output: 6
print(f"Calculator Name: {calculator.name.title()}")


class Calculator2:
    def add(self, a, b):
        if isinstance(a, int) and isinstance(b, int):
            return a + b
        elif isinstance(a, float) and isinstance(b, float):
            return a + b
        elif isinstance(a, str) and isinstance(b, str):
            return a + b
        else:
            raise TypeError("Both arguments must be of the same type (either int or str).")
calc = Calculator2()
print()
print(f"Result: {calc.add(1, 2)}")  # Output: 3
print(f"Result: {calc.add(1.5, 2.5)}")  # Output: 4.0
print(f"Result: {calc.add('Hello, ', 'World!')}")  # Output: Hello, World!

# method overriding
class Animal:
    def speak(self):
        return "Animal speaks"

class Dog(Animal):
    def speak(self):
        return "Dog barks"

class Cat(Animal):
    def speak(self):
        return "Cat meows"

# Creating instances of the classes
animal = Animal()
dog = Dog()
cat = Cat()

# Calling the speak method (polymorphism in action)
print(animal.speak())  # Output: Animal speaks
print(dog.speak())     # Output: Dog barks
print(cat.speak())     # Output: Cat meows