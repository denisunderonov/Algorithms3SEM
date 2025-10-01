import random

def generate_random_array(size=10, min_val=1, max_val=100):
    arr = []

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
        prevIndex = currentIndex - 1 #Индекс последнего элемента отсортированной части 
        
        while prevIndex >= 0 and arr[prevIndex] > current:
            arr[prevIndex + 1] = arr[prevIndex] # если элемент больше чем наш текущий, то сдвигаем -> j=0: 5 > 2? ДА → сдвигаем: [5, 5, 4, 1, 3], j=-1
            prevIndex -= 1
        
        arr[prevIndex + 1] = current
    
    return arr

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