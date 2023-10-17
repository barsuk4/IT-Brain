import datetime
import time

def rate_limit(max_calls, period):
    def decorator(func):
        call_times = []

        def wrapper(*args, **kwargs):
            now = datetime.datetime.now()
            call_times.append(now)

            # Видаляємо часи викликів, які вже не входять у визначений період
            while call_times and now - call_times[0] > period:
                call_times.pop(0)

            if len(call_times) <= max_calls:
                return func(*args, **kwargs)
            else:
                raise Exception(f"Перевищено ліміт викликів ({max_calls}) протягом періоду {period.total_seconds()} секунд")

        return wrapper

    return decorator

# Приклад використання декоратора:
@rate_limit(max_calls=3, period=datetime.timedelta(seconds=10))
def limited_function():
    print("Ця функція має обмеження на кількість викликів")
    

# Виклик функції
for _ in range(4):
    try:
        limited_function()
    except Exception as e:
        print(e)
