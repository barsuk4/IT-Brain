def multiply_by_two(numbers):
    multiplied_numbers = []
    for num in numbers:
        multiplied_numbers.append(num * 2)
    return multiplied_numbers
numbers = [1, 2, 3, 4, 5]
multiplied_numbers = multiply_by_two(numbers)
print("Похідний список", numbers)
print("Результат:", multiplied_numbers)
