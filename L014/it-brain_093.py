class MetaLogger(type):
    def __init__(cls, name, bases, attrs):
        print(f"Створено новий клас з іменем '{name}'!")
        super().__init__(name, bases, attrs)

# Використання метакласу для створення нових класів:

class MyClass1(metaclass=MetaLogger):
    def __init__(self, value):
        self.value = value

class MyClass2(metaclass=MetaLogger):
    pass

class MyClass3(metaclass=MetaLogger):
    def my_method(self):
        print("Це метод класу MyClass3!")
