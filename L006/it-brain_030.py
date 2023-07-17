def find_max(numbers):
    if len(numbers) == 0:
        return None

    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num

    return max_num

numbers = [0, 2, 9, 1, 7]
# numbers = [10, 2, 9, 1, 7]
max_number = find_max(numbers)
print("Найбільше число:", max_number)
