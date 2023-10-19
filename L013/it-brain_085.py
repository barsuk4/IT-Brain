def is_prime(number):
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True

def prime_generator():
    num = 2
    while True:
        if is_prime(num):
            yield num
        num += 1

# Приклад використання:
n = 20  # Кількість простих чисел, які ви хочете згенерувати
prime_iter = prime_generator()

for _ in range(n):
    print(next(prime_iter))
