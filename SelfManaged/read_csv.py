import re
import pandas as pd

# Читаємо прейскурант з файлу
with open("прейскурант.txt", "r", encoding="utf-8") as file:
    price_list = file.read()

# Функція для нормалізації рядка
def normalize_line(line):
    normalized_line = re.sub(r"\s+", " ", line.strip())
    normalized_line = re.sub(r"–", "-", normalized_line)
    normalized_line = re.sub(r"^\s+|\s+$", "", normalized_line)
    normalized_line = re.sub(r"\s+([,.;:]+)", r"\1", normalized_line)
    normalized_line = re.sub(r'^[.,:;()_-]|[.,:;()_-]$', '', normalized_line)
    normalized_line = normalized_line.strip()
    return normalized_line

# Регулярний вираз для знаходження ціни та одиниці вимірювання
regex_price = r'(\d+)\s?грн\s?(кг|гр|г|грам|шт)?'

# Розділяємо прейскурант на рядки
lines = price_list.split("\n")

# Створюємо списки для збереження даних
categories = []
products = []
prices = []
units = []

current_category = None

# Проходимо по кожному рядку
for line in lines:
    normalized_line = normalize_line(line)

    # Якщо рядок є порожнім, пропускаємо його
    if not normalized_line:
        continue

    # Знаходимо ціну та одиницю вимірювання за допомогою регулярних виразів
    price_match = re.search(regex_price, normalized_line)

    # Перевіряємо, чи є ціна та одиниця вимірювання у рядку
    if price_match:
        price = price_match.group(1)
        unit = price_match.group(2) if price_match.group(2) else None
        product = normalize_line(re.sub(regex_price, '', normalized_line).strip()).strip()
    else:
        # Якщо ціни немає, тоді використовуємо останню знайдену категорію
        price = "" #None
        unit = "" #None
        product = "" #None
        current_category = normalized_line

    # Записуємо дані у відповідні списки
    categories.append(current_category)
    products.append(product)
    prices.append(price)
    units.append(unit)

# Створюємо DataFrame зі зібраних даних
df = pd.DataFrame({"Категорія": categories, "Страва": products, "Ціна, грн": prices, "Одиниця вимірювання": units})

# Виводимо результат
print(df)

# Збережемо дані у форматі CSV
df.to_csv("прейскурант.csv", index=False)
