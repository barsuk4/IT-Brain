while True:
    value = input("Enter your number: ")

    if value.isdigit():
        value = int(value)
        print("Конвертоване значення:", value)
        print("Тип даних після конвертації:", type(value))
        break
    else:
        print("Помилка! Введене значення не є числом. Спробуйте знову.")
