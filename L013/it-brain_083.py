def fibonacci_generator(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

def filter_odd_numbers(sequence):
    for number in sequence:
        if number % 2 == 0:
            yield number

# Приклад використання:
n = 10  # Кількість чисел Фібоначчі, які ви хочете згенерувати
fib_sequence = fibonacci_generator(n)
filtered_sequence = filter_odd_numbers(fib_sequence)

for num in filtered_sequence:
    print(num)
