def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def get_valid_number(prompt):
    while True:
        num = input(prompt)
        if num.replace('.', '', 1).lstrip('-').isdigit():
            num = float(num)
            break
        else:
            print("Це не вірне число. Спробуйте ще раз.")
    return num 

prompt = "Введіть число:"
number = int(get_valid_number(prompt))

is_prime_number = is_prime(number)
print("Число", number, "є простим?", is_prime_number)
