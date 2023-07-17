def merge_dicts(dict1, dict2):
    merged_dict = {}

    # Додаємо ключі та значення з першого словника
    for key, value in dict1.items():
        merged_dict[key] = value

    # Додаємо ключі та значення з другого словника та обробляємо співпадіння ключів
    for key, value in dict2.items():
        if key in merged_dict:
            merged_dict[key] += value
        else:
            merged_dict[key] = value

    return merged_dict
dict1 = {"a": 10, "b": 20, "c": 30}
dict2 = {"b": 5, "d": 15, "e": 25, "f":16}

merged_dict = merge_dicts(dict1, dict2)
print(merged_dict)
