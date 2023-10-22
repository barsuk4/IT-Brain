class MetaLogger(type):
    def __new__(cls, name, bases, class_dict):
        print(f"Creating a new class: {name}")
        return super().__new__(cls, name, bases, class_dict)

# Використання метакласу для створення нових класів
class MyClass(metaclass=MetaLogger):
    pass

class AnotherClass(MyClass):
    pass
