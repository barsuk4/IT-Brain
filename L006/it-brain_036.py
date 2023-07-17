def is_anagram(str1, str2):
    # Видаляємо пробіли і перетворюємо рядки у нижній регістр
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    # Порівнюємо рядок з його зворотнім
    # return str1 == str2[::-1]
    return str1.replace(" ", "").lower() == str2.replace(" ", "").lower()[::-1]

# str1 = "tnelis"
str1 = "listen"
str2 = "silent"

print("Перший рядок: ",str1)
print("Другий рядок: ", str2)

if is_anagram(str1, str2):
    print("Рядки є анаграмами")
else:
    print("Рядки не є анаграмами")
