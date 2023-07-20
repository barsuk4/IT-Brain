import re

def is_valid_string(string):
    pattern = r'^[a-zA-Zа-яА-ЯґєіїҐЄІЇ\s]*$'
    match = re.fullmatch(pattern, string)
    return match is not None

# Приклади перевірки
strings = ["Привіт", "Hello", "Привіт, світе!", "1234", "Привіт 123"]
for string in strings:
    if is_valid_string(string):
        print(f'"{string}" - валідний рядок')
    else:
        print(f'"{string}" - невалідний рядок')
