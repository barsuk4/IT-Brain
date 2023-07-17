while True:
    num = input("Введіть число: ")
    if num.replace('.', '', 1).lstrip('-').isdigit():
        num = float(num)
        break
    else:
        print("Це не вірне число. Спробуйте ще раз.")

if num % 5 == 0:
    print("Число є кратним 5.")
else:
    print("Число не є кратним 5.")
