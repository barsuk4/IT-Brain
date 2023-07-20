import re

def is_valid_phone_number(phone_number):
    pattern = r"\+\d{3} \d{2} \d{3}-\d{4}"
    return re.match(pattern, phone_number) is not None

# Приклади перевірки
phone_numbers = ["+380 99 123-4567", "3809434-12", "+380677777777", "+380 67 777-7777"]
for number in phone_numbers:
    if is_valid_phone_number(number):
        print(f"{number} - валідний")
    else:
        print(f"{number} - не валідний")
