class NoDoubleUnderscoreMeta(type):
    def __new__(cls, name, bases, class_dict):
        for key in class_dict:
            if key.startswith('__'):
                raise ValueError(f"Class attribute {key} starts with double underscores, which is not allowed.")
        return super().__new__(cls, name, bases, class_dict)

# Using the metaclass
class MyClass(metaclass=NoDoubleUnderscoreMeta):
    attribute = "Allowed attribute"
    _single_underscore = "This is also allowed"
    # __double_underscore = "This will cause an error"  # Uncommenting this line will raise the error

# Uncommenting the problematic line in MyClass will show the error:
# ValueError: Class attribute __double_underscore starts with double underscores, which is not allowed.
