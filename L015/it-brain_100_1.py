class CarMeta(type):
    def __init__(cls, name, bases, attrs):
        if not hasattr(cls, 'cars'):
            # Цей відділ виконується тільки для базового класу Car
            cls.cars = []
        else:
            # Цей відділ виконується для будь-якого класу, який успадковує від Car
            cls.cars.append(cls)

class Car(metaclass=CarMeta):
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        print(f"Марка: {self.brand}")
        print(f"Модель: {self.model}")

class Sedan(Car):
    def __init__(self, brand, model, num_doors):
        super().__init__(brand, model)
        self.num_doors = num_doors

    def display_info(self):
        super().display_info()
        print(f"Кількість дверей: {self.num_doors}")

class SUV(Car):
    def __init__(self, brand, model, num_seats):
        super().__init__(brand, model)
        self.num_seats = num_seats

    def display_info(self):
        super().display_info()
        print(f"Кількість пасажирських місць: {self.num_seats}")

class SportsCar(Car):
    def __init__(self, brand, model, max_speed):
        super().__init__(brand, model)
        self.max_speed = max_speed

    def display_info(self):
        super().display_info()
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
