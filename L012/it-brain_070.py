from contextlib import contextmanager
import time

@contextmanager
def Timer():
    start_time = time.time()
    yield
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Час виконання: {elapsed_time} секунд")

# Приклад використання:
with Timer():
    # Ваш код, який потрібно виміряти
    time.sleep(3)  # Приклад затримки в 2 секунди
