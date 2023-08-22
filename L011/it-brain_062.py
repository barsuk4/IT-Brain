class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

# Створюємо об'єкт Rectangle
rect = Rectangle(10, 5)

# Викликаємо методи об'єкта
print(f"Площа прямокутника: {rect.area()}")
print(f"Периметр прямокутника: {rect.perimeter()}")
