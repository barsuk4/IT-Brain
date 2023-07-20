import re

def is_valid_date(date):
    pattern = r"\b(0[1-9]|1[0-2])-(0[1-9]|1[0-9]|2[0-9]|3[01])-(\d{4})\b"
    match = re.match(pattern, date)
    if match:
        month = int(match.group(1))
        day = int(match.group(2))
        year = int(match.group(3))
        days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        # Перевірка високосного року для 29 лютого
        if month == 2 and day == 29:
            if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
                return True
            else:
                return False

        # Перевірка кількості днів у місяці
        if day > days_in_month[month - 1]:
            return False

        return True

    return False

# Приклади перевірки
dates = ["05-06-2023", "05.06.2023", "12-09-2022", "2023-06-05", "29-02-2020", "29-02-2021", "30-02-2028"]
for date in dates:
    if is_valid_date(date):
        print(f"{date} - валідна дата")
    else:
        print(f"{date} - не валідна дата")
