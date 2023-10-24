class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def get_name(self):
        return self._name

    def set_name(self, name):
        # Перевірка, чи ім'я не містить цифр
        if any(char.isdigit() for char in sorted(set(name))):
            print("Помилка: Ім'я не може містити цифри.")
        else:
            self._name = name

    def get_age(self):
        return self._age

    def set_age(self, age):
        # Перевірка, чи вік знаходиться в діапазоні [0, 120]
        if 0 <= age <= 120:
            self._age = age
        else:
            print("Помилка: Вік повинен бути в діапазоні від 0 до 120.")

# Приклад використання класу "Person" з валідацією
person = Person("Вася", 25)

# Зміна імені з валідацією
person.set_name("Петятя")  # Допустима зміна імені
person.set_name("Мар'ян2")  # Помилка: Ім'я не може містити цифри

# Зміна віку з валідацією
person.set_age(30)  # Допустима зміна віку
person.set_age(150)  # Помилка: Вік повинен бути в діапазоні від 0 до 120.
