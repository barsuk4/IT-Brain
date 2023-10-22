def count_digit_sum(число):
    if число == 0:
        return 0
    else:
        return число % 10 + count_digit_sum(число // 10)

# Тест
print(count_digit_sum(1968))  # Повинно вивести 24
