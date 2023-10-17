import time

class Timer:
    def __enter__(self):
        self.start_time = time.time()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        end_time = time.time()
        elapsed_time = end_time - self.start_time
        print(f"Час виконання: {elapsed_time} секунд")

# Приклад використання:
with Timer():
    # Ваш код, який потрібно виміряти
    time.sleep(0)  # Приклад затримки в 2 секунди
