def even_odd_generator(n):
    for i in range(1, n+1):
        result = ""
        if i % 3 == 0:
            result += "Fizz"
        if i % 5 == 0:
            result += "Buzz"
        if not result:
            result = i
        yield result

# Приклад використання:
n = 20
for number in even_odd_generator(n):
    print(number)
