import os

def create_and_fill_file(filename):
    with open(filename, 'w') as file:
        for i in range(10):
            file.write(f"Це рядок номер {i + 1}\n")
    print(f"Файл {filename} створено та наповнено 10 рядками.")

def read_and_print_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
        print(f"Вміст файлу {filename}:\n{content}")
    except FileNotFoundError:
        print(f"Файл {filename} не знайдено. Створюємо його...")
        create_and_fill_file(filename)
        print(f"Повторна спроба читання файлу {filename}...")
        read_and_print_file(filename)
        os.remove(filename)
        print(f"Файл {filename} видалено.")

# Головна частина програми
filename = 'test.txt'
read_and_print_file(filename)
