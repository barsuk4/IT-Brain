def count_vowels(*words):
    vowels = ['a', 'e', 'i', 'o', 'u', 'y', 'а', 'е', 'є', 'и', 'і', 'ї', 'о', 'у', 'ю', 'я']
    vowel_counts = {}
    for word in words:
        for char in word:
            if char.lower() in vowels:
                vowel_counts[char.lower()] = vowel_counts.get(char.lower(), 0) + 1
    return vowel_counts

result = count_vowels("Hello", "world", "Привіт", "світ")
print(result)
