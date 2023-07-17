from datetime import datetime

name = input("Введіть ваше ім'я: ")

while True:
    birth_year = input("Введіть ваш рік народження: ")
    if birth_year.isdigit():
        break
    else:
        print("Помилка! Рік народження повинен бути числом. Спробуйте знову.")

current_year = datetime.now().year
age = current_year - int(birth_year)

print("Your name:", name, "ваш вік", age)
