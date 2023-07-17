def get_even_numbers(numbers):
    even_numbers = []
    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)
    return even_numbers

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2]
even_numbers = get_even_numbers(numbers)
print("Список парних чисел:", even_numbers)
