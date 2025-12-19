import time
import random

def generate_array(size=10000):
    return [random.randint(1, 100000) for _ in range(size)]

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >=0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

def quick_sort(arr):
    if len(arr) <= 1: return arr
    pivot = arr[len(arr)//2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    #добавление остатков
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def heap_sort(arr):
    """
    Пирамидальная сортировка (Heap Sort)
    
    Алгоритм:
    1. Строим max-heap из массива (максимальный элемент в корне)
    2. Извлекаем максимум (корень) и помещаем в конец
    3. Восстанавливаем свойство кучи для оставшейся части
    4. Повторяем, пока вся куча не будет отсортирована
    
    Сложность: O(n log n) - гарантированно
    Память: O(1) - сортирует на месте
    """
    n = len(arr)
    
    # Шаг 1: Построение max-heap (снизу вверх)
    # Начинаем с последнего родителя и идем к корню
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    
    # Шаг 2: Извлечение элементов из кучи по одному
    for i in range(n - 1, 0, -1):
        # Меняем корень (максимум) с последним элементом
        arr[0], arr[i] = arr[i], arr[0]
        
        # Восстанавливаем свойство кучи для уменьшенной кучи
        heapify(arr, i, 0)
    
    return arr

def heapify(arr, n, i):
    """
    Просеивание вниз (sift down) для поддержания свойства max-heap
    
    Параметры:
    - arr: массив
    - n: размер кучи
    - i: индекс текущего узла
    
    Простыми словами:
    Если текущий элемент меньше своих детей, меняем его местами 
    с бОльшим ребенком и продолжаем просеивание вниз
    """
    largest = i  # Инициализируем наибольший как корень
    left = 2 * i + 1  # Левый потомок
    right = 2 * i + 2  # Правый потомок
    
    # Если левый потомок существует и больше корня
    if left < n and arr[left] > arr[largest]:
        largest = left
    
    # Если правый потомок существует и больше текущего наибольшего
    if right < n and arr[right] > arr[largest]:
        largest = right
    
    # Если наибольший элемент не корень
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Меняем местами
        
        # Рекурсивно просеиваем затронутое поддерево
        heapify(arr, n, largest)

arr = generate_array(10000)

print("Тестируем сортировки на массиве из 10,000 элементов:\n")

sorts = [
    ("Пузырьковая", bubble_sort),
    ("Выбором", selection_sort),
    ("Вставками", insertion_sort), 
    ("Быстрая", quick_sort),
    ("Слиянием", merge_sort),
    ("Пирамидальная", heap_sort),
]

for name, func in sorts:
    start = time.time()
    func(arr.copy())  
    end = time.time()
    print(f"{name}: {end-start:.2f} сек")