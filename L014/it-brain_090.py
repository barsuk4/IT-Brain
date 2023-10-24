class NoDunderAttributes(type):
    def __init__(cls, name, bases, dct):
        for key in dct:
            if key.startswith('__') and not key.endswith('__'):
                raise ValueError(f"Cannot have attribute names starting with double underscore")
        super().__init__(name, bases, dct)

# Using the metaclass
class MyClass(metaclass=NoDunderAttributes):
    attribute = "Allowed attribute"
    _single_underscore = "This is also allowed"
    # __double_underscore = "This will cause an error"  # Uncommenting this line will raise the error

# Some test classes
class TestClass1(metaclass=NoDunderAttributes):
    regular_attribute = "This is fine"

class TestClass2(metaclass=NoDunderAttributes):
    _single_underscore_attr = "This is also okay"

# Uncommenting the following class definition will raise the error due to __double_underscore_attr
class TestClass3(metaclass=NoDunderAttributes):
    __double_underscore_attr = "This will cause an error"

print("All classes created successfully without error.")
