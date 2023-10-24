class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def display_dimensions(self):
        print(f"Ширина: {self.width} одиниць")
        print(f"Висота: {self.height} одиниць")


class Square(Rectangle):
    def __init__(self, side_length):
        super().__init__(side_length, side_length)  # Виклик конструктора батьківського класу
        self.side_length = side_length

    def display_dimensions(self):
        super().display_dimensions()  # Виклик методу батьківського класу
        print(f"Довжина сторони: {self.side_length} одиниць")


# Приклад використання класу "Square"
square = Square(5)
print("Інформація про квадрат:")
square.display_dimensions()
