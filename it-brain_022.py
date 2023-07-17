def count_character_frequency(string):
    frequency = {}

    for char in string:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1

    return frequency

input_string = input("Введіть рядок: ")
character_frequency = count_character_frequency(input_string)

print("Частота кожного символу:")
for char, count in character_frequency.items():
    print(f"{char}: {count}")
