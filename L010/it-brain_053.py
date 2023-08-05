spisok = [1, 2, 3, 4, 6]

try:
    index = 10
    print(spisok[index])
except IndexError:
    print(f"Ви намагаєтеся отримати доступ до індексу {index}, але довжина списку лише {len(spisok)}.")

    """
    https://github.com/barsuk4/IT-Brain/commit/85ce0d82d7cf9830234a9c18e39ee5aaa395480b
    """