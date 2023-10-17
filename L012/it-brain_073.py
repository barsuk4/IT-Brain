def log_func(func):
    def wrapper(*args, **kwargs):
        print(f"Перед викликом функції {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Після виклику функції {func.__name__}")
        return result
    return wrapper

# Приклад використання декоратора:
@log_func
def add(a, b):
    return a + b

@log_func
def substr(a,b):
    return a - b


result1 = add(2, 3)
result2 = substr(4,5)
