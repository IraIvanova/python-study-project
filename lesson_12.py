class Car:
    def __init__(self, manufacturer: str, model: str, fuel_consumption: float, production_year: int = 2020):
        self.manufacturer = manufacturer
        self.model = model
        self.fuel_consumption = fuel_consumption
        self.production_year = production_year
        self.mileage = 0

    def __str__(self):
        return f"{self.manufacturer} {self.model} ({self.production_year}) - Пробіг: {self.mileage} км, Витрата палива: {self.fuel_consumption} л"

    def signal(self):
        print(f"{self.manufacturer} {self.model} робить біп-біп!")
        return self


car1 = Car("Toyota", "Camry", 8.5, production_year=2018)
car2 = Car("Honda", "Civic", 7.2)
car3 = Car("Mazda", "CX-7", production_year=2015, fuel_consumption=12.0)
