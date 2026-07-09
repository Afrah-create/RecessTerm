# Abstraction
# What is Abstraction?

# Lab Activity 3
#Multiple Abstract Methods

from abc import ABC, abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
    @abstractmethod
    def stop(self):
        pass

# car = Vehicle()

# car.start()
# car.stop()

class Car(Vehicle):
    def start(self):
        print('Car Started')
    def stop(self):
        print('Car stopped')
car = Car()
car.start()
car.stop()


# Exercise 3 : Using Multiple abstract method
# Create an abstract class for shapes, should have method area(), perimeter()
#Create a Rectangle and Circle to implement both methods