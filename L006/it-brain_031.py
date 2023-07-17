def convert_to_uppercase(strings):
    uppercase_strings = []
    for string in strings:
        uppercase_string = string.upper()
        uppercase_strings.append(uppercase_string)
    return uppercase_strings

strings = ["Hi!", "I'm ", "Python"]
uppercase_strings = convert_to_uppercase(strings)
print("Список рядків", strings)
print("Новий список рядків:", uppercase_strings)
