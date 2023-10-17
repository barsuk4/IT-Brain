def retry(max_retries):
    def decorator(func):
        def wrapper(*args, **kwargs):
            retries = 0
            while retries < max_retries:
                try:
                    result = func(*args, **kwargs)
                    return result
                except Exception as e:
                    print(f"Помилка: {e}. Повторна спроба {retries + 1} з {max_retries}")
                    retries += 1
            raise Exception(f"Помилка: функція {func.__name__} не вдалася після {max_retries} спроб")
        return wrapper
    return decorator

# Приклад використання декоратора:
@retry(max_retries=3)
def divide(a, b):
    return a / b

result = divide(10, 0)  # Спроба поділу на нуль, але функція спробує виконатися до 3 разів
