while True:
    year = input("Введіть рік: ")
    if year.isdigit():
        year = int(year)
        break
    else:
        print("Неправильний ввід. Рік повинен бути цілим числом.")

if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print(f"Рік {year} є високосним.")
else:
    print(f"Рік {year} не є високосним.")
