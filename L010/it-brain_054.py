def input_integer(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Будь ласка, введіть ціле число. Спробуйте ще раз.")

# введення чисел користувачем
num1 = input_integer("Будь ласка, введіть перше ціле число: ")
num2 = input_integer("Будь ласка, введіть друге ціле число: ")

# вивід результатів
print(f"Ви ввели: {num1} і {num2}")
