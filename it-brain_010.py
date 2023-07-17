while True:
    month = input("Введіть порядковий номер місяця: ")
    if month.isdigit() and 1 <= int(month) <= 12:
        month = int(month)
        break
    else:
        print("Неправильний ввід. Порядковий номер місяця повинен бути числом від 1 до 12.")

if month in {1, 3, 5, 7, 8, 10, 12}:
    days = 31
elif month == 2:
    days = 28  # вибираємо невисокосний рік
else:
    days = 30

print(f"У місяці №{month} {days} днів.")
