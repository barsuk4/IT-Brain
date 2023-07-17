tuple1 = (1, 2, 3, 4, 5)
tuple2 = (3, 4, 5, 6, 7)

result_set = set(tuple1) - set(tuple2)

result_tuple = tuple(result_set)

print(tuple1)
print(tuple2)
print("Результат:", result_tuple)
