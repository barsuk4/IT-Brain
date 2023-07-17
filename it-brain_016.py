def count_vowels(text):
    vowels = 'аеиіїоуюяєї'  # Голосні літери української абетки
    count = 0

    for char in text:
        if char.lower() in vowels:
            count += 1

    return count

input_text = input("Введіть рядок: ")
vowel_count = count_vowels(input_text)

print("Кількість голосних: ", vowel_count)
