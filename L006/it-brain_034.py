def count_vowels(string):
    vowels = "aeiouаеєиіїоуюя"
    count = 0
    for char in string.lower():
        if char in vowels:
            count += 1
    return count

string = "Hello World! Привіт Світ!"
vowel_count = count_vowels(string)
print("Кількість голосних літер:", vowel_count)
