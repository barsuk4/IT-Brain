def fib_generator(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# Приклад використання:
n = 20 # Кількість чисел Фібоначчі, які ви хочете згенерувати
for num in fib_generator(n):
    print(num)
