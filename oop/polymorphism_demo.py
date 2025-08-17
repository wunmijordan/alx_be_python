# polymorphism_demo.py

import math

class Shape:
    def area(self):
        """Base method for area, must be overridden in derived classes."""
        raise NotImplementedError("Subclasses must override this method")


class Rectangle(Shape):
    def __init__(self, length: float, width: float):
        self.length = length
        self.width = width

    def area(self):
        """Override area() to calculate area of a rectangle."""
        return self.length * self.width


class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def area(self):
        """Override area() to calculate area of a circle."""
        return math.pi * (self.radius ** 2)
