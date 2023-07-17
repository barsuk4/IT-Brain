while True:
    number = input("Введіть натуральне число: ")
    if number.isdigit() and int(number) > 0:
        number = int(number)
        break
    else:
        print("Некоректне введення. Спробуйте ще раз.")

i = 1
while i <= number:
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
    i += 1
