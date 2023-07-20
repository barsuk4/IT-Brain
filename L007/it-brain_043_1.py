import string

def word_frequency_counter(text):
    # Створюємо список стоп-слів
    stop_words = ["the", "and", "a", "is", "in", "it", "і", "та", "як", "що"]

    # Розділяємо текст на окремі слова та видаляємо розділові знаки
    words = text.split()
    words = [word.strip(string.punctuation) for word in words]

    # Створюємо словник для зберігання частот слів
    word_frequency = {}

    # Перебираємо слова та оновлюємо частоти
    for word in words:
        # Якщо слово є стоп-словом, пропускаємо його
        if word.lower() in stop_words:
            continue

        # Якщо слова немає у словнику, додаємо його з частотою 1
        if word not in word_frequency:
            word_frequency[word] = 1
        else:
            # Якщо слово вже є у словнику, збільшуємо його частоту на 1
            word_frequency[word] += 1

    # Відсортовуємо словник за значеннями у порядку спадання
    sorted_word_frequency = dict(sorted(word_frequency.items(), key=lambda x: x[1], reverse=True))

    return sorted_word_frequency

# Ввід рядка з консолі
text = input("Введіть рядок тексту: ")

# Виведення введеного рядка
print("Введений рядок: ", text)

# Виклик функції та виведення результатів
frequency = word_frequency_counter(text)
print(frequency)
