def double_characters(text):
    doubled_text = ""

    for char in text:
        doubled_text += char * 2

    return doubled_text

input_text = input("Введіть рядок: ")
result = double_characters(input_text)
print("Результат:", result)
