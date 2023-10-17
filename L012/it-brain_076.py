import time

def timing_decorator(func):
    def wrapper(*args, **kwargs):
        if args not in wrapper.cache:
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            elapsed_time = end_time - start_time
            print(f"Час виконання функції {func.__name__}: {elapsed_time:.6f} секунд з розрахунком")
            wrapper.cache[args] = result
        else:
            start_time = time.time()
            result = wrapper.cache[args]
            end_time = time.time()
            elapsed_time = end_time - start_time
            print(f"Час виконання функції {func.__name__}: {elapsed_time:.6f} секунд з кешем")
        return result

    wrapper.cache = {}
    return wrapper

def memoize(func):
    cache = {}

    def wrapper(*args):
        if args in cache:
            return cache[args]
        else:
            result = func(*args)
            cache[args] = result
            return result

    return wrapper

# Виклик функції з однаковими аргументами
@timing_decorator
@memoize
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Перший виклик функції
result1 = factorial(5)  # Результат буде закешований, і буде виміряно час для цього виклику

# Другий виклик функції з тими самими аргументами
result2 = factorial(5)  # Результат буде взятий з кешу, і буде виміряно час для цього виклику

print(result1)  # Виведе: 120
print(result2)  # Виведе: 120
