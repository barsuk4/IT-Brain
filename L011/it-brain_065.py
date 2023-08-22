class Student:
    def __init__(self, first_name, last_name, grades=None):
        self.first_name = first_name
        self.last_name = last_name
        self.grades = grades if grades is not None else []

    def add_grade(self, grade):
        self.grades.append(grade)

    def __len__(self):
        return len(self.grades)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - Оцінки: {self.grades}"

# Створення списку студентів
students = [
    Student("Олександр", "Петров", [5, 4, 4, 5]),
    Student("Ірина", "Сергієнко", [4, 5]),
    Student("Анна", "Іванова", [5, 4, 4, 5, 3]),
    Student("Володимир", "Мельник")
]

# Додаємо оцінки для Володимира
students[3].add_grade(4)
students[3].add_grade(3)

# Сортуємо список студентів за кількістю оцінок
sorted_students = sorted(students, key=lambda student: len(student), reverse=True)

# Виведення відсортованого списку
for student in sorted_students:
    print(student)
