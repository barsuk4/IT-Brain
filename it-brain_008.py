while True:
    temp = input("Введіть температуру в градусах Цельсія: ")
    if temp.replace('.', '', 1).lstrip('-').isdigit():
        temp = float(temp)
        break
    else:
        print("Це не вірне число. Спробуйте ще раз.")

if temp <= 0:
    print("Це лід.")
elif 0 < temp <= 32:
    print("Це холодна вода.")
elif 32 < temp <= 40:
    print("Це тепла вода.")
elif 40 < temp < 99:
    print("Це гаряча вода.")
else:
    print("Це пара.")
