def squares_generator(N):
    for i in range(1, N + 1):
        yield i ** 2

# Приклад використання:
N = 5  # Верхній ліміт чисел
for square in squares_generator(N):
    print(square)
