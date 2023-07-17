def multiplication_table(number):
    table = ""
    for i in range(1, 11):
        result = number * i
        row = f"{number} * {i} = {result}\n"
        table += row
    return table

input_number = int(input("Введіть число: "))
table = multiplication_table(input_number)
print(table)
