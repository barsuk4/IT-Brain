import math

def power(base, exponent):
    if base == 0:
        if exponent == 0:
            return 1
        elif exponent < 0:
            print("Помилка! Не можна використовувати від'ємний показник сутпіню якщо основа '0'")
            exit() 
    else:
        return round(math.exp(exponent * math.log(abs(base))), 10)

def get_valid_number(prompt):
    while True:
        num = input(prompt)
        if num.replace('.', '', 1).lstrip('-').isdigit():
            num = float(num)
            break
        else:
            print("Це не вірне число. Спробуйте ще раз.")
    return num 

a = get_valid_number('a: ')
b = get_valid_number('b: ')
print("Результат:", power(a, b))
