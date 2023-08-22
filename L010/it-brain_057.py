import os

def count_words_in_file(filename):
    """Читає вміст файлу та повертає кількість слів у ньому."""
    with open(filename, 'r') as file:
        content = file.read()
        words = content.split()
        return len(words)

# Перевіряємо наявність файлу
filename = 'temp_file.txt'
if not os.path.exists(filename):
    # Якщо файл не існує, створюємо його
    with open(filename, 'w') as file:
        file.write("Це тестовий файл, створений для демонстрації.")

# Читаємо вміст файлу та виводимо кількість слів
word_count = count_words_in_file(filename)
print(f"Кількість слів у файлі: {word_count}")

# Видаляємо файл
os.remove(filename)
print(f"Файл {filename} видалено.")
