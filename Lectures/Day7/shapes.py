from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    def area(self, radius):
        return 3.14 * radius ** 2

    def perimeter(self, radius):
        return 2 * 3.14 * radius


class Triangle(Shape):
    def area(self, base, height):
        return 0.5 * base * height

    def perimeter(self, side1, side2, side3):
        return side1 + side2 + side3