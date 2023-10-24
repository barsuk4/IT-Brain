from abc import ABC, abstractmethod

class Car(ABC):
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        
    @abstractmethod
    def display_info(self):
        pass

class Sedan(Car):
    def __init__(self, brand, model, num_doors):
        super().__init__(brand, model)
        self.num_doors = num_doors

    def display_info(self):
        print(f"Марка: {self.brand}")
        print(f"Модель: {self.model}")
        print(f"Кількість дверей: {self.num_doors}")

class SUV(Car):
    def __init__(self, brand, model, num_seats):
        super().__init__(brand, model)
        self.num_seats = num_seats

    def display_info(self):
        print(f"Марка: {self.brand}")
        print(f"Модель: {self.model}")
        print(f"Кількість пасажирських місць: {self.num_seats}")

class SportsCar(Car):
    def __init__(self, brand, model, max_speed):
        super().__init__(brand, model)
        self.max_speed = max_speed

    def display_info(self):
        print(f"Марка: {self.brand}")
        print(f"Модель: {self.model}")
        print(f"Максимальна швидкість: {self.max_speed} км/год")

# Демонстрація
sedan = Sedan("Toyota", "Camry", 4)
suv = SUV("Lexus", "RX", 5)
sports_car = SportsCar("Ferrari", "488", 330)

print("Седан:")
sedan.display_info()
print("\nПозашляховик:")
suv.display_info()
print("\nСпортивний автомобіль:")
sports_car.display_info()
