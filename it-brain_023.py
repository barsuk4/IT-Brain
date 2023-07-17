def reverse_words(string):
    words = string.split()  # Розбиваємо рядок на окремі слова
    reversed_words = words[::-1]  # Обертаємо порядок слів

    reversed_string = " ".join(reversed_words)  # З'єднуємо слова зворотньо

    return reversed_string

input_string = input("Введіть рядок: ")
reversed_string = reverse_words(input_string)

print("Слова у зворотному порядку:", reversed_string)
