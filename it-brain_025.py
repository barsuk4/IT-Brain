def remove_punctuation(input_string):
    # Створюємо рядок, який буде містити символи, що не є розділовими знаками
    no_punct = ""
    # Проходимо по кожному символу у вхідному рядку
    for char in input_string:
        # Перевіряємо, чи символ не є розділовим знаком
        if char.isalnum() or char.isspace():
            # Додавання символу до рядка без розділових знаків
            no_punct += char
    return no_punct

# Запитуємо користувача про ввід рядка
input_string = input("Введіть рядок: ")

# Видаляємо розділові знаки з рядка
result_string = remove_punctuation(input_string)

# Виводимо результат
print("Рядок без розділових знаків:", result_string)
