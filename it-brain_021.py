total_sum = 0
n = 100
for number in range(1, n+1):
    if number % 3 == 0 and number % 5 != 0:
        # print(number)
        total_sum += number

print("Сума чисел:", total_sum)
