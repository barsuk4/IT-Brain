class Student:
    # Атрибут класу для відстеження кількості студентів
    student_count = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        # Збільшуємо кількість студентів на 1 при кожному створенні екземпляра
        Student.student_count += 1

    @classmethod
    def total_students(cls):
        """Повертає загальну кількість студентів."""
        return cls.student_count

# Приклад використання:

student1 = Student("Олег", 20)
student2 = Student("Анна", 19)
student3 = Student("Ігор", 21)

print(f"Загальна кількість студентів: {Student.total_students()}")
