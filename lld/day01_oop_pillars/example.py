"""Day 1 tiny example: all 4 OOP pillars in one car analogy.

Run:  python -m lld.day01_oop_pillars.example
"""
from abc import ABC, abstractmethod


class Vehicle(ABC):                       # ABSTRACTION: says WHAT a vehicle can do, not HOW
    def __init__(self, name: str):
        self.name = name
        self._speed = 0                   # ENCAPSULATION: internal state, changed only via methods

    @property
    def speed(self) -> int:               # read-only window into the internal state
        return self._speed

    def accelerate(self, amount: int) -> None:
        self._speed = min(self._speed + amount, self.max_speed())   # the rule lives in one place

    @abstractmethod
    def max_speed(self) -> int: ...

    @abstractmethod
    def horn(self) -> str: ...


class Bike(Vehicle):                      # INHERITANCE: a Bike IS-A Vehicle and reuses accelerate()
    def max_speed(self) -> int: return 120
    def horn(self) -> str: return "Beep beep!"


class Truck(Vehicle):
    def max_speed(self) -> int: return 80
    def horn(self) -> str: return "HOOONK!"


if __name__ == "__main__":
    for vehicle in [Bike("Pulsar"), Truck("Tata 407")]:   # POLYMORPHISM: same call, different behaviour
        vehicle.accelerate(100)
        print(f"{vehicle.name:<9} horn={vehicle.horn():<11} speed={vehicle.speed}")
