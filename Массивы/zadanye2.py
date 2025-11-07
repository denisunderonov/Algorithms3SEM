import random

# Проверка размера массива
while True:
    try:
        size = int(input("Введите размер массива: "))
        if size <= 0:
            print("Размер массива должен быть положительным числом!")
            continue
        break
    except ValueError:
        print("Пожалуйста, введите целое число!")

# Создание массива
arr = []
for i in range(size):
    arr.append(random.randint(1, 100))
print("Исходный массив:", arr)

# Основной цикл программы
while True:
    print("\nОперации: 1-поиск, 2-вставка, 3-удаление, 4-выход")
    choice = input("Выберите операцию: ")
    
    if choice == '1':
        # Поиск элемента
        try:
            value = int(input("Введите значение для поиска: "))
        except ValueError:
            print("Пожалуйста, введите целое число!")
            continue
            
        positions = []
        for i in range(len(arr)):
            if arr[i] == value:
                positions.append(i)
        
        if len(positions) > 0:
            print("Элемент найден на позициях:", positions)
        else:
            print("Элемент не найден")
    
    elif choice == '2':
        # Вставка элемента
        try:
            value = int(input("Введите значение для вставки: "))
        except ValueError:
            print("Пожалуйста, введите целое число!")
            continue
            
        arr.append(value)
        print("Массив после вставки:", arr)
    
    elif choice == '3':
        # Удаление элемента
        try:
            value = int(input("Введите значение для удаления: "))
        except ValueError:
            print("Пожалуйста, введите целое число!")
            continue
            
        new_arr = []
        found = False
        
        for i in range(len(arr)):
            if arr[i] != value:
                new_arr.append(arr[i])
            else:
                found = True
        
        if found:
            arr = new_arr
            print("Массив после удаления:", arr)
        else:
            print("Элемент не найден")
    
    elif choice == '4':
        # Выход из программы
        print("Итоговый массив:", arr)
        print("Программа завершена.")
        break
    
    else:
        print("Неверный выбор! Пожалуйста, выберите 1, 2, 3 или 4.")