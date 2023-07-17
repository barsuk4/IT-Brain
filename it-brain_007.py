while True:
    number1 = input("Будь ласка, введіть перше число: ")
    if number1.isdigit():
        number1 = int(number1)
        break
    else:
        print("Це не число. Будь ласка, спробуйте ще раз.")

while True:
    number2 = input("Будь ласка, введіть друге число: ")
    if number2.isdigit():
        number2 = int(number2)
        break
    else:
        print("Це не число. Будь ласка, спробуйте ще раз.")

result = f"Більше число: {number1}" if number1 > number2 else f"Більше число: {number2}" if number2 > number1 else "Числа рівні."
print(result)
