def factorial(n):
    if n < 0:
        return None
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

# Запитуємо користувача про ввід числа
num = int(input("Введіть число: "))

# Обчислюємо факторіал числа
factorial_result = factorial(num)

# Виводимо результат
if factorial_result is not None:
    print("Факторіал числа", num, "дорівнює", factorial_result)
else:
    print("Факторіал не може бути обчислений для від'ємного числа.")
