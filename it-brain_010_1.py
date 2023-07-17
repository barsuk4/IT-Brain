while True:
    year = input("Введіть рік: ")
    if year.isdigit():
        year = int(year)
        break
    else:
        print("Неправильний ввід. Рік повинен бути цілим числом.")

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
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        days = 29
    else:
        days = 28
else:
    days = 30

print(f"У місяці №{month} {year} року {days} днів.")

