# Rectangle class with area, perimeter, and diagonal methods

import math


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def diagonal(self):
        return math.sqrt(self.length ** 2 + self.width ** 2)


length = float(input("Enter rectangle length: "))
width = float(input("Enter rectangle width: "))

if length < 0 or width < 0:
    print("Length and width cannot be negative.")
else:
    rectangle = Rectangle(length, width)
    print("Area:", rectangle.area())
    print("Perimeter:", rectangle.perimeter())
    print("Diagonal:", rectangle.diagonal())
