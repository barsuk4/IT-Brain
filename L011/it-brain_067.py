class Circle:
    # Атрибут класу для зберігання значення π
    PI = 3.141592653589793

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Обчислює площу кола."""
        return Circle.PI * (self.radius ** 2)

    def circumference(self):
        """Обчислює довжину кола (периметр)."""
        return 2 * Circle.PI * self.radius

# Приклад використання:

circle = Circle(5)
print(f"Площа кола з радіусом 5: {circle.area():.2f}")
print(f"Довжина кола з радіусом 5: {circle.circumference():.2f}")
