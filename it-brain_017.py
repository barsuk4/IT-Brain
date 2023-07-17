def is_palindrome(text):
    text = text.lower()  # Перетворюємо рядок на нижній регістр
    cleaned_text = ""

    for char in text:
        if char.isalpha():
            cleaned_text += char

    reversed_text = cleaned_text[::-1]  # Зворотній порядок символів

    return cleaned_text == reversed_text

input_text = input("Введіть рядок: ")
if is_palindrome(input_text):
    print("Рядок є паліндромом")
else:
    print("Рядок не є паліндромом")
