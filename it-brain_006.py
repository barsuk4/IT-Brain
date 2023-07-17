while True:
    number = input("Будь ласка, введіть число: ")
    # перевірка, чи є введене значення числом
    if number.isdigit():
        number = int(number)
        # перевірка, чи є число парним
        if number % 2 == 0:
            print(f"Число {number} є парним.")
        else:
            print(f"Число {number} є непарним.")
        break
    else:
        print("Це не число. Будь ласка, спробуйте ще раз.")
