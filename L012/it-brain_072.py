from contextlib import contextmanager

@contextmanager
def DividerContext1(divider):
    print(divider)  # Виводимо роздільник перед виконанням коду
    yield
    print(divider)  # Виводимо роздільник після виконання коду

class DividerContext2:
    def __init__(self, divider):
        self.divider = divider

    def __enter__(self):
        print(self.divider)  # Виводимо роздільник перед виконанням коду

    def __exit__(self, exc_type, exc_value, traceback):
        print(self.divider)  # Виводимо роздільник після виконання коду

# Приклад використання обох варіантів:
with DividerContext1("*"):
    # Ваш основний код
    print("Це мій основний код")

with DividerContext2("-"):
    # Інший основний код
    print("Це інший основний код")
