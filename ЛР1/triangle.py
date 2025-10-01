a = float(input("Введите длину первого отрезка: "))
b = float(input("Введите длину второго отрезка: "))
c = float(input("Введите длину третьего отрезка: "))

if a > 0 and b > 0 and c > 0:

    if a + b > c and a + c > b and b + c > a:
        print("да")
    else:
        print("нет")
else:
    print("нет")