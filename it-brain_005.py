number1 = input("Введіть перше число: ")
number2 = input("Введіть друге число: ")

# Перевірка на введення цифр
if not number1.isdigit() or not number2.isdigit():
    print("Помилка! Введені значення повинні бути числами.")
else:
    number1 = int(number1)
    number2 = int(number2)

    # Арифметичні операції
    sum_result = number1 + number2
    diff_result = number1 - number2
    mul_result = number1 * number2
    div_result = number1 / number2

    # Виведення результатів українською мовою
    print("Сума:", sum_result)
    print("Різниця:", diff_result)
    print("Добуток:", mul_result)
    print("Ділення:", div_result)
