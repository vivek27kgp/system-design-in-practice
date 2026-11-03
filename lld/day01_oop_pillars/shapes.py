"""Shapes: abstraction + polymorphism.

`Shape` is the contract ("every shape can tell its area and perimeter").
Each concrete shape decides HOW. Code that uses shapes never checks the type.
"""
import math
from abc import ABC, abstractmethod
from collections.abc import Iterable
from dataclasses import dataclass


class Shape(ABC):
    @abstractmethod
    def area(self) -> float: ...

    @abstractmethod
    def perimeter(self) -> float: ...

    def describe(self) -> str:
        # Shared behaviour written once in the parent; it calls methods the children provide.
        return f"{type(self).__name__}: area={self.area():.2f}, perimeter={self.perimeter():.2f}"


# frozen=True → immutable value objects, and dataclass generates __eq__ and __hash__ for us:
# Circle(2) == Circle(2) is True, and circles can be used as dict keys / set members.
@dataclass(frozen=True)
class Circle(Shape):
    radius: float

    def __post_init__(self) -> None:
        if self.radius <= 0:
            raise ValueError("radius must be positive")

    def area(self) -> float:
        return math.pi * self.radius**2

    def perimeter(self) -> float:
        return 2 * math.pi * self.radius


@dataclass(frozen=True)
class Rectangle(Shape):
    width: float
    height: float

    def __post_init__(self) -> None:
        if self.width <= 0 or self.height <= 0:
            raise ValueError("width and height must be positive")

    def area(self) -> float:
        return self.width * self.height

    def perimeter(self) -> float:
        return 2 * (self.width + self.height)


@dataclass(frozen=True)
class Triangle(Shape):
    a: float
    b: float
    c: float

    def __post_init__(self) -> None:
        sides = sorted((self.a, self.b, self.c))
        if sides[0] <= 0 or sides[0] + sides[1] <= sides[2]:
            raise ValueError(f"sides {self.a}, {self.b}, {self.c} cannot form a triangle")

    def area(self) -> float:
        s = self.perimeter() / 2  # Heron's formula
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def perimeter(self) -> float:
        return self.a + self.b + self.c


def total_area(shapes: Iterable[Shape]) -> float:
    """Polymorphism in action: works for any Shape, including ones written next year."""
    return sum(shape.area() for shape in shapes)
