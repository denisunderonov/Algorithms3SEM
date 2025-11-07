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

arr = generate_array(10000)

print("Тестируем сортировки на массиве из 10,000 элементов:\n")

sorts = [
    ("Пузырьковая", bubble_sort),
    ("Выбором", selection_sort),
    ("Вставками", insertion_sort), 
    ("Быстрая", quick_sort),
    ("Слиянием", merge_sort), 
]

for name, func in sorts:
    start = time.time()
    func(arr.copy())  
    end = time.time()
    print(f"{name}: {end-start:.2f} сек")