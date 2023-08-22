def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Ділення на нуль! Будь ласка, в наступний раз введіть не нульове значення для знаменника.")
        return None

def input_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Будь ласка, введіть дійсне число. Спробуйте ще раз.")

# Запитуємо користувача ввести два числа:
num1 = input_float("Введіть перше число: ")
num2 = input_float("Введіть друге число (знаменник): ")

result = safe_divide(num1, num2)
if result is not None:
    print(f"Результат ділення: {result}")
