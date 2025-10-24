print("Создание упорядоченного массива")
size = int(input("Введите размер массива: "))

arr = []
print("Введите элементы массива в упорядоченном виде (от меньшего к большему):")
for i in range(size):
    element = int(input(f"Элемент {i+1}: "))
    arr.append(element)

print("Ваш упорядоченный массив:", arr)

while True:
    print("\n" + "="*40)
    print("ВЫБЕРИТЕ ОПЕРАЦИЮ:")
    print("1 - Линейный поиск")
    print("2 - Бинарный поиск") 
    print("3 - Вставка элемента")
    print("4 - Удаление элемента")
    print("5 - Показать массив")
    print("6 - Выход")
    print("="*40)
    
    choice = input("Ваш выбор (1-6): ")
    
    if choice == '1':
        value = int(input("Введите значение для поиска: "))
        positions = []
        
        for i in range(len(arr)):
            if arr[i] == value:
                positions.append(i)
        
        if len(positions) > 0:
            print(f"Элемент {value} найден на позициях: {positions}")
        else:
            print(f"Элемент {value} не найден")
    
    elif choice == '2':
        value = int(input("Введите значение для поиска: "))
        positions = []

        left = 0
        right = len(arr) - 1

        found_index = -1
        while left <= right:
            middle = (left + right) // 2
            if arr[middle] == value:
                found_index = middle
                break
            elif arr[middle] < value:
                left = middle + 1
            else:
                right = middle - 1
        
        if found_index != -1:
            positions.append(found_index)
            
            i = found_index - 1
            while i >= 0 and arr[i] == value:
                positions.append(i)
                i -= 1
            
            i = found_index + 1
            while i < len(arr) and arr[i] == value:
                positions.append(i)
                i += 1
            
            positions.sort()
            print(f"Элемент {value} найден на позициях: {positions}")
        else:
            print(f"Элемент {value} не найден")
    
    elif choice == '3':
        value = int(input("Введите значение для вставки: "))

        insert_position = 0
        for i in range(len(arr)):
            if arr[i] < value:
                insert_position = i + 1
            else:
                break

        arr.insert(insert_position, value)
        print(f"Элемент {value} вставлен на позицию {insert_position}")
        print("Массив после вставки:", arr)
    
    elif choice == '4':
        value = int(input("Введите значение для удаления: "))
        new_arr = []
        deleted_count = 0
        
        for i in range(len(arr)):
            if arr[i] != value:
                new_arr.append(arr[i])
            else:
                deleted_count += 1
        
        if deleted_count > 0:
            arr = new_arr
            print(f"Удалено {deleted_count} элементов со значением {value}")
            print("Массив после удаления:", arr)
        else:
            print(f"Элемент {value} не найден")
    
    elif choice == '5':
        print("Текущий массив:", arr)
        print(f"Размер массива: {len(arr)}")
    
    elif choice == '6':
        print("Итоговый массив:", arr)
        print("Программа завершена!")
        break
    
    else:
        print("Неверный выбор! Введите число от 1 до 6")