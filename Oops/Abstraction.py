# Abstraction in Python

from abc import ABC, abstractmethod

# --------------------------------------------------
# 1. Creating an Abstract Class
# --------------------------------------------------

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


# --------------------------------------------------
# 2. Implementing Abstract Method in Child Classes
# --------------------------------------------------

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


# --------------------------------------------------
# 3. Using the Classes
# --------------------------------------------------

rect = Rectangle(10, 5)
circle = Circle(7)

print("Rectangle Area:", rect.area())
print("Circle Area:", circle.area())

print("\nAbstraction examples completed.")
