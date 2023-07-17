secret_number = 7

while True:
    guess = int(input("Вгадайте секретне число від 1 до 10: "))

    if guess == secret_number:
        print("Вітаємо, ви вгадали!")
        break
    elif guess == 0:
        print("Наступного разу пощастить!")
        break
    else:
        print("Неправильно, спробуйте ще раз.")
