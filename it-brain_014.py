def merge_dicts(dict1, dict2):
    merged_dict = dict1.copy()  # Копіюємо dict1 для створення початкового словника об"єднання

    for key, value in dict2.items():
        merged_dict[key] = value

    return merged_dict

# Приклад вхідних словників
dict1 = {"ім'я": "John", "прізвище": "Doe", "вік": 25 }
dict2 = {"телефон": "+380677777777", "email": "john.doe@example.com", "стать": "чоловіча"}

# Об"єднуємо словники
merged_dict = merge_dicts(dict1, dict2)

#Виводимо словники
print("Словник1:", dict1)
print("Словник2:", dict2)

# Виводимо результат
print("Об'єднаний словник:", merged_dict)
