from abc import ABC, abstractmethod
from typing import Self


class TransportVehicle(ABC):
    def __init__(self, brand: str, tank_capacity: float, fuel_level: float, speed: float, mileage: float):
        self.brand = brand
        self.tank_capacity = tank_capacity
        self.fuel_level = fuel_level
        self.speed = speed
        self.mileage = mileage

    def refuel(self, amount):
        self.fuel_level += self.tank_capacity - self.fuel_level if self.fuel_level + amount > self.tank_capacity else amount

    def transfer_fuel(self, other_vehicle: Self, amount):
        available_amount = other_vehicle.tank_capacity - other_vehicle.fuel_level
        required_amount_to_fuel = amount if available_amount >= amount else available_amount
        transfer_amount = required_amount_to_fuel if self.fuel_level - required_amount_to_fuel > 0 else self.fuel_level
        self.fuel_level -= transfer_amount
        other_vehicle.fuel_level += transfer_amount

    @abstractmethod
    def __str__(self):
        return f"{self.brand} - Fuel: {self.fuel_level}/{self.tank_capacity}, Speed: {self.speed}, Mileage: {self.mileage}"


class Car(TransportVehicle):
    def __init__(self, brand: str, tank_capacity: float, fuel_level: float, speed: float, mileage: float,
                 passenger_count: int, airbags: bool):
        super().__init__(brand, tank_capacity, fuel_level, speed, mileage)
        self.passenger_count = passenger_count
        self.airbags = airbags

    def __str__(self):
        return f"Car - {super().__str__()}, Passengers: {self.passenger_count}, Airbags: {self.airbags}"


class Motorcycle(TransportVehicle):
    def __init__(self, brand: str, tank_capacity: float, fuel_level: float, speed: float, mileage: float,
                 sidecar: bool):
        super().__init__(brand, tank_capacity, fuel_level, speed, mileage)
        self.sidecar = sidecar

    def __str__(self):
        return f"Motorcycle - {super().__str__()}, Sidecar: {self.sidecar}"


car1 = Car("Toyota", 60, 30, 120, 15000, 5, True)
car2 = Car("Honda", 50, 20, 100, 12000, 4, False)

motorcycle1 = Motorcycle("Harley", 20, 15, 80, 8000, True)

car1.refuel(10)
car1.transfer_fuel(car2, 5)
car1.transfer_fuel(car2, 21)
