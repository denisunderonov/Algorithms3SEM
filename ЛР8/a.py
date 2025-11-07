import time
import random

def generate_array(size=10000):
    """Создает случайный массив"""
    return [random.randint(1, 100000) for _ in range(size)]

def linear_search_all(arr, target):
    """Линейный поиск - находит ВСЕ вхождения элемента"""
    indices = []
    for i in range(len(arr)):
        if arr[i] == target:
            indices.append(i)
    return indices

def binary_search_first(arr, target):
    """Бинарный поиск - находит ПЕРВОЕ вхождение в отсортированном массиве"""
    left, right = 0, len(arr) - 1
    result = -1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            result = mid
            right = mid - 1  # Продолжаем искать слева
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return result

def find_all_in_ordered(arr, target):
    """Находит ВСЕ вхождения в отсортированном массиве"""
    first_index = binary_search_first(arr, target)
    if first_index == -1:
        return []
    
    # В отсортированном массиве все одинаковые элементы идут подряд
    indices = []
    i = first_index
    while i < len(arr) and arr[i] == target:
        indices.append(i)
        i += 1
    
    return indices

def pure_linear_search_all(arr, target):
    """Чистый линейный поиск без копирования"""
    indices = []
    for i in range(len(arr)):
        if arr[i] == target:
            indices.append(i)
    return indices

def pure_binary_search_ordered(arr, target):
    """Чистый бинарный поиск в отсортированном массиве"""
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def pure_insert_into_ordered(arr, element):
    """Чистая вставка в упорядоченный массив - работает с переданным массивом"""
    # Используем бинарный поиск для нахождения позиции вставки
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < element:
            left = mid + 1
        else:
            right = mid
    
    # Вставляем элемент на найденную позицию
    arr.insert(left, element)
    return arr

def pure_append_to_unordered(arr, element):
    """Чистое добавление в конец неупорядоченного массива"""
    arr.append(element)
    return arr

def pure_delete_all_from_unordered(arr, element):
    """Чистое удаление ВСЕХ вхождений из неупорядоченного массива"""
    # Находим все индексы для удаления
    indices = []
    for i in range(len(arr)):
        if arr[i] == element:
            indices.append(i)
    
    # Удаляем с конца, чтобы индексы не сдвигались
    for index in sorted(indices, reverse=True):
        del arr[index]
    
    return arr

def pure_delete_all_from_ordered(arr, element):
    """Чистое удаление ВСЕХ вхождений из упорядоченного массива"""
    # Находим все индексы для удаления
    first_index = binary_search_first(arr, element)
    if first_index == -1:
        return arr
    
    indices = []
    i = first_index
    while i < len(arr) and arr[i] == element:
        indices.append(i)
        i += 1
    
    # Удаляем с конца, чтобы индексы не сдвигались
    for index in sorted(indices, reverse=True):
        del arr[index]
    
    return arr

def measure_pure_time(func, arr, *args):
    """Измеряет чистое время выполнения функции (без копирования)"""
    start = time.time()
    result = func(arr, *args)
    end = time.time()
    return end - start

# Основная программа
print("=== ТЕСТИРОВАНИЕ ОПЕРАЦИЙ С МАССИВАМИ (ЧИСТОЕ ВРЕМЯ) ===\n")

# Создаем массивы с возможными дубликатами
size = 10000
base_unordered = generate_array(size)
# Добавим несколько дубликатов для тестирования
base_unordered.extend([base_unordered[0], base_unordered[size//2], base_unordered[-1]])
base_ordered = sorted(base_unordered)

print(f"Созданы базовые массивы из {len(base_unordered)} элементов (с дубликатами)\n")

# Выбираем конкретные элементы для операций
element_to_insert = 99999
element_to_delete1 = base_unordered[0]
element_to_delete2 = base_unordered[size//2]
element_to_delete3 = base_unordered[-1]

print(f"Элементы для операций:")
print(f"  Вставка: {element_to_insert}")
print(f"  Удаление: {element_to_delete1}, {element_to_delete2}, {element_to_delete3}")

# Покажем сколько дубликатов каждого элемента
print(f"\nКоличество вхождений элементов в исходных массивах:")
count1 = len(pure_linear_search_all(base_unordered.copy(), element_to_delete1))
count2 = len(pure_linear_search_all(base_unordered.copy(), element_to_delete2))
count3 = len(pure_linear_search_all(base_unordered.copy(), element_to_delete3))
print(f"  {element_to_delete1}: {count1} раз(а)")
print(f"  {element_to_delete2}: {count2} раз(а)")
print(f"  {element_to_delete3}: {count3} раз(а)\n")

# Тестируем поиск
print("--- ПОИСК ЭЛЕМЕНТОВ (чистое время) ---")

# Ищем разные элементы
targets = [element_to_delete1, element_to_delete2, element_to_delete3]

for target in targets:
    print(f"\nПоиск числа {target}:")
    
    # Создаем копии ДО измерения времени
    unordered_copy = base_unordered.copy()
    ordered_copy = base_ordered.copy()
    
    # Линейный поиск ВСЕХ вхождений в неупорядоченном
    time1 = measure_pure_time(pure_linear_search_all, unordered_copy, target)
    found_count1 = len(pure_linear_search_all(base_unordered.copy(), target))
    print(f"  Линейный (неупор.): {time1:.6f} сек, найдено: {found_count1}")
    
    # Линейный поиск ВСЕХ вхождений в упорядоченном  
    time2 = measure_pure_time(pure_linear_search_all, ordered_copy, target)
    found_count2 = len(pure_linear_search_all(base_ordered.copy(), target))
    print(f"  Линейный (упор.):   {time2:.6f} сек, найдено: {found_count2}")
    
    # Поиск в упорядоченном (бинарный поиск первого вхождения)
    ordered_copy2 = base_ordered.copy()
    time3 = measure_pure_time(pure_binary_search_ordered, ordered_copy2, target)
    print(f"  Бинарный (упор.):   {time3:.6f} сек")

# Тестируем вставку
print("\n--- ВСТАВКА ЭЛЕМЕНТА (чистое время) ---")
print(f"Вставка элемента {element_to_insert}:")

# Создаем копии ДО измерения времени
unordered_copy = base_unordered.copy()
ordered_copy = base_ordered.copy()

# Вставка в неупорядоченный массив (в конец)
time_insert_unordered = measure_pure_time(pure_append_to_unordered, unordered_copy, element_to_insert)
print(f"  Неупорядоченный (в конец): {time_insert_unordered:.6f} сек")

# Вставка в упорядоченный массив (с поиском позиции)
time_insert_ordered = measure_pure_time(pure_insert_into_ordered, ordered_copy, element_to_insert)
print(f"  Упорядоченный (с поиском позиции): {time_insert_ordered:.6f} сек")

# Проверяем, что порядок сохранился
test_arr = base_ordered.copy()
pure_insert_into_ordered(test_arr, element_to_insert)
is_sorted = test_arr == sorted(test_arr)
print(f"  Проверка сохранения порядка: {'✓ УСПЕХ' if is_sorted else '✗ ОШИБКА'}")

# Тестируем удаление
print("\n--- УДАЛЕНИЕ ЭЛЕМЕНТОВ (чистое время) ---")

elements_to_delete = [element_to_delete1, element_to_delete2, element_to_delete3]

for element in elements_to_delete:
    print(f"\nУдаление элемента {element}:")
    
    # Создаем копии ДО измерения времени
    unordered_copy = base_unordered.copy()
    ordered_copy = base_ordered.copy()
    
    # Удаление ВСЕХ вхождений из неупорядоченного массива
    original_count = len(pure_linear_search_all(base_unordered.copy(), element))
    time_delete_unordered = measure_pure_time(pure_delete_all_from_unordered, unordered_copy, element)
    print(f"  Неупорядоченный: {time_delete_unordered:.6f} сек, удалено: {original_count}")
    
    # Удаление ВСЕХ вхождений из упорядоченного массива
    original_count_ordered = len(find_all_in_ordered(base_ordered.copy(), element))
    time_delete_ordered = measure_pure_time(pure_delete_all_from_ordered, ordered_copy, element)
    print(f"  Упорядоченный:   {time_delete_ordered:.6f} сек, удалено: {original_count_ordered}")

print("\n=== ТЕСТИРОВАНИЕ ЗАВЕРШЕНО ===")

# Дополнительный тест - сравнение времени копирования и операций
print("\n" + "="*60)
print("ДОПОЛНИТЕЛЬНЫЙ АНАЛИЗ: ВРЕМЯ КОПИРОВАНИЯ МАССИВОВ")
print("="*60)

# Измеряем время копирования
start = time.time()
copy_unordered = base_unordered.copy()
copy_time_unordered = time.time() - start

start = time.time()
copy_ordered = base_ordered.copy()
copy_time_ordered = time.time() - start

print(f"Время копирования неупорядоченного массива: {copy_time_unordered:.6f} сек")
print(f"Время копирования упорядоченного массива: {copy_time_ordered:.6f} сек")
print(f"Размер массивов: {len(base_unordered)} элементов")