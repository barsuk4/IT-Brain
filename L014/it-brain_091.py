class CamelCaseMeta(type):
    def __new__(cls, name, bases, attrs):
        if not name[0].isupper():
            raise ValueError(f"Назва класу '{name}' повинна починатися з великої літери (CamelCase формат).")
        return super().__new__(cls, name, bases, attrs)

# Вірно вказаний CamelCase:
class ProperCamelCase(metaclass=CamelCaseMeta):
    pass

# Невірно вказаний CamelCase (починається з малої літери):
try:
    class improperCamelCase(metaclass=CamelCaseMeta):
        pass
except ValueError as e:
    print(e)

# Інший приклад класу з правильною назвою:
class AnotherProperName(metaclass=CamelCaseMeta):
    pass

# Ще один невірний приклад:
try:
    class anotherImproperName(metaclass=CamelCaseMeta):
        pass
except ValueError as e:
    print(e)
