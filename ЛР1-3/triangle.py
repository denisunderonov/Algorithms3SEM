while True:
    try:
        a = int(input("Введите длину первого отрезка: "))
        if a > 0:
            break
        else:
            print("Ошибка! Длина должна быть положительным числом!")
    except ValueError:
        print("Ошибка! Введите целое число!")

while True:
    try:
        b = int(input("Введите длину второго отрезка: "))
        if b > 0:
            break
        else:
            print("Ошибка! Длина должна быть положительным числом!")
    except ValueError:
        print("Ошибка! Введите целое число!")

while True:
    try:
        c = int(input("Введите длину третьего отрезка: "))
        if c > 0:
            break
        else:
            print("Ошибка! Длина должна быть положительным числом!")
    except ValueError:
        print("Ошибка! Введите целое число!")

if a + b > c and a + c > b and b + c > a:
    print("да")
else:
    print("нет")