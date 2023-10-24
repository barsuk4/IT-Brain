class Person:
    def __init__(self, name, age):
        # Приватні властивості з позначкою "_"
        self._name = name
        self._age = age

    # Метод для отримання імені
    def get_name(self):
        return self._name

    # Метод для встановлення імені
    def set_name(self, name):
        self._name = name

    # Метод для отримання віку
    def get_age(self):
        return self._age

    # Метод для встановлення віку
    def set_age(self, age):
        self._age = age

# Приклад використання класу "Person"
person = Person("Вася", 25)

# Отримання імені та віку
name = person.get_name()
age = person.get_age()
print(name)
print(age)
# Зміна імені та віку
person.set_name("Петя")
person.set_age(30)
# Друк оновлених значень
print(person.get_name())
print(person.get_age())

