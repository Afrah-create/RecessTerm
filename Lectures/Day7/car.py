class Car:
    def __init__(self, brand, model, price):
        self.brand = brand
        self._model = model
        self.__price = price
    def printCarDetails(self):
        print(f"This is a {self.brand} {self._model} and costs ${self.__price}.")
car = Car("Toyota", "Corolla", 20000)
car.printCarDetails()
print(car.brand)  # Accessing public attribute
print(car._model)  # Accessing protected attribute (not recommended)
# print(car.__price)  # This will raise an AttributeError because __price is private