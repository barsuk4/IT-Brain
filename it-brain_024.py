total_sum = 0

while True:
    input_value = input("Введіть число: ")

    if input_value == "":
        continue

    if input_value.replace('.', '', 1).lstrip('-').isdigit():
        number = float(input_value)
        if number < 0:
            break
        total_sum += number
    else:
        print("Це не вірне число. Спробуйте ще раз.")

print("Остаточна сума:", total_sum)
