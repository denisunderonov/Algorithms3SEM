import random

size = int(input("Введите размер массива: "))
arr = []
for i in range(size):
    arr.append(random.randint(1, 100))
print("Исходный массив:", arr)

while True:
    print("\nОперации: 1-поиск, 2-вставка, 3-удаление, 4-выход")
    choice = input("Выберите операцию: ")
    
    if choice == '1':
        value = int(input("Введите значение для поиска: "))
        positions = []
        for i in range(len(arr)):
            if arr[i] == value:
                positions.append(i)
        
        if len(positions) > 0:
            print("Элемент найден на позициях:", positions)
        else:
            print("Элемент не найден")
    
    elif choice == '2':
        value = int(input("Введите значение для вставки: "))
        arr.append(value)
        print("Массив после вставки:", arr)
    
    elif choice == '3':
        value = int(input("Введите значение для удаления: "))
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
        print("Итоговый массив:", arr)
        break
    
    else:
        print("Неверный выбор!")