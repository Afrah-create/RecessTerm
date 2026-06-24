# operator overloading
# used to define the behavior of operators for user-defined classes
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        return Point(self.x * scalar, self.y * scalar)

    def __truediv__(self, scalar):
        return Point(self.x / scalar, self.y / scalar)

    def __repr__(self):
        return f"Point({self.x}, {self.y})"
pt1 = Point(2, 3)
pt2 = Point(4, 5)
# addition
result_add = pt1 + pt2
print("Addition:", result_add)  # Output: Point(6, 8)
# subtraction
result_sub = pt1 - pt2
print("Subtraction:", result_sub)  # Output: Point(-2, -2)
# multiplication
result_mul = pt1 * 2
print("Multiplication:", result_mul)  # Output: Point(4, 6)
# division
result_div = pt1 / 2
print("Division:", result_div)  # Output: Point(1.0, 1.5)