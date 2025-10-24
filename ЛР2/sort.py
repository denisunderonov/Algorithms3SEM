import random

def generate_random_array(size=10, min_val=1, max_val=100):
    arr = []
    while True:
        try:
            size = int(input("Введите размер массива: "))
            if size <= 0:
                print("Размер должен быть положительным числом!")
                continue
            break
        except ValueError:
            print("Ошибка! Введите целое число!")
    
    for i in range(size):
        random_number = random.randint(min_val, max_val)
        arr.append(random_number)
    
    return arr

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = []
    for x in arr:
        if x < pivot:
            left.append(x)
    middle = []
    for x in arr:
        if x == pivot:
            middle.append(x)
    right = []
    for x in arr:
        if x > pivot:
            right.append(x)

    return quicksort(left) + middle + quicksort(right)

def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

def insertion_sort(arr):
    for currentIndex in range(1, len(arr)):
        current = arr[currentIndex]
        prevIndex = currentIndex - 1  
        
        while prevIndex >= 0 and arr[prevIndex] > current:
            arr[prevIndex + 1] = arr[prevIndex]
            prevIndex -= 1
        
        arr[prevIndex + 1] = current
    
    return arr

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:] 
    
    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)

    result = []
    i = 0  
    j = 0  
    
    while i < len(left_sorted) and j < len(right_sorted):
        if left_sorted[i] <= right_sorted[j]:
            result.append(left_sorted[i])
            i += 1
        else:
            result.append(right_sorted[j])
            j += 1
    
    result.extend(left_sorted[i:])
    result.extend(right_sorted[j:])
    
    return result

randomArr = generate_random_array()
print(f"Исходный массив: {randomArr}")
print("------------------------------")
print(f"Массив, отсортированный пузырьковой сортировкой: {bubble_sort(randomArr)}")
print("------------------------------")
print(f"Массив, отсортированный быстрой сортировкой: {quicksort(randomArr)}")
print("------------------------------")
print(f"Массив, отсортированный сортировкой вставками: {insertion_sort(randomArr)}")
print("------------------------------")
print(f"Массив, отсортированный сортировкой выбором: {selection_sort(randomArr)}")
print("------------------------------")
print(f"Массив, отсортированный сортировкой слиянием: {merge_sort(randomArr)}")