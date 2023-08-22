class Vehicle:
    def __init__(self, name, speed, cost):
        self.name = name
        self.speed = speed
        self.cost = cost

    def __gt__(self, other):
        if self.speed == other.speed:
            return self.cost > other.cost
        return self.speed > other.speed

    def __str__(self):
        return f"{self.name} - Швидкість: {self.speed} км/год, Вартість: {self.cost} грн."

# Створення списку транспортних засобів
vehicles = [
    Vehicle("CarA", 180, 500000),
    Vehicle("CarB", 180, 400000),
    Vehicle("Bicycle", 25, 3000),
    Vehicle("MotorcycleA", 120, 150000),
    Vehicle("MotorcycleB", 120, 100000),
    Vehicle("Plane", 800, 5000000)
]

# Сортування списку транспортних засобів за швидкістю і вартістю
sorted_vehicles = sorted(vehicles, reverse=True)

# Виведення відсортованого списку
for vehicle in sorted_vehicles:
    print(vehicle)
