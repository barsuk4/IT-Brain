import time

def timeit(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Час виконання функції {func.__name__}: {execution_time:.6f} секунд")
        return result
    return wrapper

# Приклад використання декоратора:
@timeit
def add(a, b):
    return a + b

result = add(2, 3)
