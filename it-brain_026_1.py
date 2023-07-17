def find_second_smallest(numbers):
    # Перевіряємо, чи список має щонайменше два елементи
    if len(numbers) < 2:
        return None

    smallest = float('inf')
    second_smallest = float('inf')

    # Знаходимо найменший та другий найменший елементи
    for num in numbers:
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif num < second_smallest and num != smallest:
            second_smallest = num

    # Повертаємо другий найменший елемент
    return second_smallest

# Заданий список чисел
numbers = [5, 3, 8, 1, 9, 2, 7, 6, 4]

# Знаходимо другий найменший елемент
second_smallest = find_second_smallest(numbers)

# Виводимо результат
if second_smallest is not None:
    print("Другий найменший елемент:", second_smallest)
else:
    print("У списку недостатньо елементів.")
