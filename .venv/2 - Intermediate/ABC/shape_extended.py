from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    @abstractmethod
    def get_area(self):
        pass

    @abstractmethod
    def get_perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return pi * self.radius**2

    def get_perimeter(self):
        return 2 * pi * self.radius


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def get_area(self):
        return self.side**2

    def get_perimeter(self):
        return 4 * self.side


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * (self.width + self.height)


class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def get_perimeter(self):
        return self.a + self.b + self.c

    def get_area(self):
        s = self.get_perimeter() / 2
        return (s * (s - self.a) * (s - self.b) * (s - self.c)) ** 0.5


class Parallelogram(Shape):
    def __init__(self, base, height, side):
        self.base = base
        self.height = height
        self.side = side

    def get_area(self):
        return self.base * self.height

    def get_perimeter(self):
        return 2 * (self.base + self.side)


shapes = [
    Rectangle(5, 3),
    Square(4),
    Circle(3),
    Triangle(3, 4, 5),
    Parallelogram(6, 3, 4),
]

for shape in shapes:
    name = shape.__class__.__name__
    area = shape.get_area()
    perimeter = shape.get_perimeter()

    print(f"{name} — Area: {area:.2f}, Perimeter: {perimeter:.2f}")
