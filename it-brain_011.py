while True:
    num1 = input("Введіть перше число: ")
    if num1.replace('.', '', 1).isdigit() or num1.replace('.', '', 1).lstrip('-').isdigit():
        num1 = float(num1)
        break
    else:
        print("Неправильний ввід. Введіть число.")

while True:
    num2 = input("Введіть друге число: ")
    if num2.replace('.', '', 1).isdigit() or num2.replace('.', '', 1).lstrip('-').isdigit():
        num2 = float(num2)
        break
    else:
        print("Неправильний ввід. Введіть число.")

while True:
    operator = input("Введіть оператор (+, -, *, /): ")
    if operator in {"+", "-", "*", "/"}:
        break
    else:
        print("Неправильний ввід. Введіть один з наступних операторів: +, -, *, /.")

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Ділення на нуль!"

print(f"Результат: {result}")
