class Shape:
    def __init__(self, color):
        self.color = color  # Властивість колір

    def display_color(self):
        print(f"Колір фігури: {self.color}")


class Rectangle(Shape):
    def __init__(self, color, width, height):
        super().__init__(color)  # Виклик конструктора батьківського класу
        self.width = width  # Властивість ширина
        self.height = height  # Властивість висота

    def display_dimensions(self):
        print(f"Ширина прямокутника: {self.width} одиниць")
        print(f"Висота прямокутника: {self.height} одиниць")


# Приклад використання класів
shape = Shape("червоний")
shape.display_color()

rectangle = Rectangle("чорний", 5, 10)
rectangle.display_color()
rectangle.display_dimensions()
