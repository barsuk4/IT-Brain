class Car:
    def __init__(self, make, model, year, mileage=0):
        self._make = make  # Приватна властивість
        self._model = model  # Приватна властивість
        self.year = year  # Публічна властивість
        self.mileage = mileage  # Публічна властивість

    # Метод для отримання марки
    def get_make(self):
        return self._make

    # Метод для отримання моделі
    def get_model(self):
        return self._model

    # Метод для зміни марки
    def set_make(self, make):
        self._make = make

    # Метод для зміни моделі
    def set_model(self, model):
        self._model = model

    # Метод для здійснення поїздки
    def drive(self, distance):
        if self.mileage + distance <= 300000:
            self.mileage += distance
            print(f"Здійснено поїздку на {distance} км. Загальний пробіг: {self.mileage} км.")
        else:
            print("Помилка: Пробіг перевищив ліміт 300000 км.")

# Приклад використання класу "Car"
car = Car("Toyota", "Camry", 2020)
print(f"{car.get_make()} {car.get_model()}, Рік випуску: {car.year}, Пробіг: {car.mileage} км")

car.drive(10000)
car.drive(200000)
car.drive(200000)
