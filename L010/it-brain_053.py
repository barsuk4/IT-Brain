spisok = [1, 2, 3, 4, 6]

try:
    index = 10
    print(spisok[index])
except IndexError:
    print(f"Ви намагаєтеся отримати доступ до індексу {index}, але довжина списку лише {len(spisok)}.")
