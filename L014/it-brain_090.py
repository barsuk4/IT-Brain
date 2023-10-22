class NotDoubleUnderAttributes(type):
    def __init__(cls, name, bases, dct):
        for key in dct:
            if key.startswith('__') and not key.endswith('__'):
                raise ValueError(f"Cannot have attribute names starting with double underscore")
        super().__init__(name, bases, dct)

# Using the metaclass
class MyClass(metaclass=NotDoubleUnderAttributes):
    attribute = "Allowed attribute"
    _single_underscore = "This is also allowed"
    __double_underscore = "This will cause an error"  # This line will raise the error now
