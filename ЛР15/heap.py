# -*- coding: utf-8 -*-
"""
ПИРАМИДЫ (КУЧИ) - Binary Heap
Минимальная и максимальная куча с пирамидальной сортировкой
"""
import random
import time


class BinaryHeap:
    """Класс для работы с двоичной пирамидой"""
    
    def __init__(self, heap_type='max'):
        """
        heap_type: 'max' для максимальной кучи, 'min' для минимальной
        """
        self.heap = []
        self.heap_type = heap_type
    
    def compare(self, a, b):
        """Сравнение в зависимости от типа кучи"""
        if self.heap_type == 'max':
            return a > b  # Для max-heap родитель больше детей
        else:
            return a < b  # Для min-heap родитель меньше детей
    
    def parent(self, i):
        """Индекс родителя"""
        return (i - 1) // 2
    
    def left_child(self, i):
        """Индекс левого ребёнка"""
        return 2 * i + 1
    
    def right_child(self, i):
        """Индекс правого ребёнка"""
        return 2 * i + 2
    
    def sift_up(self, i):
        """
        Просеивание вверх (используется при вставке)
        Поднимаем элемент, пока не выполнится свойство кучи
        """
        while i > 0:
            parent_idx = self.parent(i)
            if self.compare(self.heap[i], self.heap[parent_idx]):
                # Меняем местами с родителем
                self.heap[i], self.heap[parent_idx] = self.heap[parent_idx], self.heap[i]
                i = parent_idx
            else:
                break
    
    def sift_down(self, i):
        """
        Просеивание вниз (используется при удалении)
        Опускаем элемент, пока не выполнится свойство кучи
        """
        n = len(self.heap)
        
        while True:
            largest = i  # Для max-heap
            left = self.left_child(i)
            right = self.right_child(i)
            
            # Находим наибольший/наименьший среди узла и его детей
            if left < n and self.compare(self.heap[left], self.heap[largest]):
                largest = left
            
            if right < n and self.compare(self.heap[right], self.heap[largest]):
                largest = right
            
            # Если нужно, меняем местами
            if largest != i:
                self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
                i = largest
            else:
                break
    
    def insert(self, value):
        """Вставка элемента в кучу"""
        self.heap.append(value)
        self.sift_up(len(self.heap) - 1)
        print(f"✅ Вставлен элемент: {value}")
    
    def extract_root(self):
        """Удаление корня (максимум для max-heap, минимум для min-heap)"""
        if not self.heap:
            print("⚠️  Куча пустая!")
            return None
        
        root = self.heap[0]
        
        # Заменяем корень последним элементом
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        
        # Просеиваем вниз
        if self.heap:
            self.sift_down(0)
        
        return root
    
    def peek(self):
        """Посмотреть корень без удаления"""
        if not self.heap:
            return None
        return self.heap[0]
    
    def search(self, value):
        """Поиск элемента в куче (линейный поиск)"""
        try:
            index = self.heap.index(value)
            return index
        except ValueError:
            return -1
    
    def delete(self, value):
        """Удаление конкретного элемента"""
        index = self.search(value)
        
        if index == -1:
            print(f"❌ Элемент {value} не найден!")
            return False
        
        # Заменяем удаляемый элемент последним
        self.heap[index] = self.heap[-1]
        self.heap.pop()
        
        # Восстанавливаем свойство кучи
        if index < len(self.heap):
            # Пробуем просеять вверх
            parent_idx = self.parent(index)
            if index > 0 and self.compare(self.heap[index], self.heap[parent_idx]):
                self.sift_up(index)
            else:
                self.sift_down(index)
        
        print(f"✅ Удалён элемент: {value}")
        return True
    
    def build_heap(self, array):
        """Построение кучи из массива (heapify)"""
        self.heap = array.copy()
        
        # Начинаем с последнего не-листа и идём к корню
        for i in range(len(self.heap) // 2 - 1, -1, -1):
            self.sift_down(i)
        
        print(f"✅ Куча построена из массива: {array}")
    
    def is_empty(self):
        """Проверка на пустоту"""
        return len(self.heap) == 0
    
    def size(self):
        """Размер кучи"""
        return len(self.heap)
    
    def get_array(self):
        """Получить массив кучи"""
        return self.heap.copy()


def heap_sort(array, reverse=False):
    """
    Пирамидальная сортировка
    reverse=False: по возрастанию (используем max-heap)
    reverse=True: по убыванию (используем min-heap)
    """
    start_time = time.time()
    
    # Создаём кучу
    heap_type = 'max' if not reverse else 'min'
    heap = BinaryHeap(heap_type)
    heap.build_heap(array)
    
    sorted_array = []
    
    # Извлекаем элементы из кучи
    while not heap.is_empty():
        sorted_array.append(heap.extract_root())
    
    end_time = time.time()
    execution_time = (end_time - start_time) * 1000  # в миллисекундах
    
    return sorted_array, execution_time


def display_heap_tree(heap_obj, index=0, indent="", last=True):
    """Визуализация кучи в виде дерева"""
    if index >= len(heap_obj.heap):
        return
    
    array = heap_obj.heap
    
    # Правое поддерево
    right_idx = heap_obj.right_child(index)
    if right_idx < len(array):
        display_heap_tree(heap_obj, right_idx, indent + ("     " if last else " │   "), False)
    
    # Текущий узел
    if index == 0:
        print(array[index])
    else:
        print(indent + (" └── " if last else " ┌── ") + str(array[index]))
    
    # Левое поддерево
    left_idx = heap_obj.left_child(index)
    if left_idx < len(array):
        display_heap_tree(heap_obj, left_idx, indent + (" │   " if last else "     "), True)


def display_heap(heap_obj):
    """Отображение кучи"""
    if heap_obj.is_empty():
        print("\n" + "="*50)
        print("Куча пустая")
        print("="*50 + "\n")
        return
    
    heap_type_name = "МАКСИМАЛЬНАЯ" if heap_obj.heap_type == 'max' else "МИНИМАЛЬНАЯ"
    print("\n" + "="*50)
    print(f"{heap_type_name} КУЧА:")
    print("="*50)
    print(f"Массив: {heap_obj.heap}")
    print(f"Размер: {heap_obj.size()}")
    print(f"Корень: {heap_obj.peek()}")
    print("\nДерево:")
    display_heap_tree(heap_obj)
    print("="*50 + "\n")


def print_menu():
    """Главное меню"""
    print("\n" + "╔" + "="*58 + "╗")
    print("║" + " "*20 + "🔺 ПИРАМИДЫ (КУЧИ) 🔺" + " "*18 + "║")
    print("╚" + "="*58 + "╝")
    print("\n┌─────────────────────────────────────────────────────────┐")
    print("│  СОЗДАНИЕ КУЧИ:                                         │")
    print("│  1.  Создать максимальную кучу (max-heap)               │")
    print("│  2.  Создать минимальную кучу (min-heap)                │")
    print("│  3.  Построить кучу из случайного массива               │")
    print("├─────────────────────────────────────────────────────────┤")
    print("│  ОПЕРАЦИИ:                                              │")
    print("│  4.  Вставить элемент                                   │")
    print("│  5.  Удалить корень (extract max/min)                   │")
    print("│  6.  Удалить конкретный элемент                         │")
    print("│  7.  Поиск элемента                                     │")
    print("│  8.  Показать кучу                                      │")
    print("├─────────────────────────────────────────────────────────┤")
    print("│  ПИРАМИДАЛЬНАЯ СОРТИРОВКА:                              │")
    print("│  9.  Сортировать массив (по возрастанию)                │")
    print("│  10. Сортировать массив (по убыванию)                   │")
    print("├─────────────────────────────────────────────────────────┤")
    print("│  0.  Выход                                              │")
    print("└─────────────────────────────────────────────────────────┘")


def main():
    """Главная функция"""
    heap = None
    
    print("\n" + "🔺"*30)
    print("  ПРОГРАММА РАБОТЫ С ПИРАМИДАМИ (КУЧАМИ)")
    print("🔺"*30)
    
    print("\n📚 КРАТКАЯ ТЕОРИЯ:")
    print("───────────────────────────────────────────────────────────")
    print("ПИРАМИДА (КУЧА) - это двоичное дерево, где:")
    print("• MAX-HEAP: родитель ≥ детей (корень - максимум)")
    print("• MIN-HEAP: родитель ≤ детей (корень - минимум)")
    print("\nОСНОВНЫЕ ОПЕРАЦИИ:")
    print("• Вставка: O(log n) - добавляем в конец, просеиваем вверх")
    print("• Удаление корня: O(log n) - заменяем последним, просеиваем вниз")
    print("• Heapify: O(n) - превращение массива в кучу")
    print("• Heap Sort: O(n log n) - сортировка через кучу")
    print("───────────────────────────────────────────────────────────\n")
    
    while True:
        print_menu()
        choice = input("\n➤ Выберите действие: ").strip()
        
        try:
            if choice == '1':
                # Максимальная куча
                heap = BinaryHeap('max')
                print("\n✅ Создана МАКСИМАЛЬНАЯ куча (max-heap)")
                print("   Свойство: родитель ≥ детей, корень - максимум")
                display_heap(heap)
            
            elif choice == '2':
                # Минимальная куча
                heap = BinaryHeap('min')
                print("\n✅ Создана МИНИМАЛЬНАЯ куча (min-heap)")
                print("   Свойство: родитель ≤ детей, корень - минимум")
                display_heap(heap)
            
            elif choice == '3':
                # Построить из массива
                if heap is None:
                    print("\n⚠️  Сначала создайте кучу (выберите 1 или 2)!")
                    continue
                
                size = int(input("Размер массива: "))
                array = [random.randint(1, 100) for _ in range(size)]
                print(f"\n📊 Случайный массив: {array}")
                
                heap.build_heap(array)
                display_heap(heap)
            
            elif choice == '4':
                # Вставка
                if heap is None:
                    print("\n⚠️  Сначала создайте кучу!")
                    continue
                
                display_heap(heap)
                value = int(input("Введите значение для вставки: "))
                heap.insert(value)
                display_heap(heap)
            
            elif choice == '5':
                # Удаление корня
                if heap is None or heap.is_empty():
                    print("\n⚠️  Куча пустая!")
                    continue
                
                display_heap(heap)
                root_name = "максимум" if heap.heap_type == 'max' else "минимум"
                root = heap.extract_root()
                print(f"\n✅ Удалён корень ({root_name}): {root}")
                display_heap(heap)
            
            elif choice == '6':
                # Удаление элемента
                if heap is None or heap.is_empty():
                    print("\n⚠️  Куча пустая!")
                    continue
                
                display_heap(heap)
                value = int(input("Введите значение для удаления: "))
                heap.delete(value)
                display_heap(heap)
            
            elif choice == '7':
                # Поиск
                if heap is None or heap.is_empty():
                    print("\n⚠️  Куча пустая!")
                    continue
                
                value = int(input("Введите значение для поиска: "))
                index = heap.search(value)
                
                if index != -1:
                    print(f"\n✅ Элемент {value} найден на позиции {index}")
                    print(f"   Массив: {heap.heap}")
                else:
                    print(f"\n❌ Элемент {value} не найден")
            
            elif choice == '8':
                # Показать кучу
                if heap is None:
                    print("\n⚠️  Куча не создана!")
                    continue
                display_heap(heap)
            
            elif choice == '9':
                # Сортировка по возрастанию
                size = int(input("Размер массива для сортировки: "))
                array = [random.randint(1, 100) for _ in range(size)]
                
                print(f"\n📊 Исходный массив: {array}")
                sorted_array, exec_time = heap_sort(array, reverse=False)
                print(f"\n✅ Отсортированный массив (↑): {sorted_array}")
                print(f"⏱️  Время выполнения: {exec_time:.4f} мс")
            
            elif choice == '10':
                # Сортировка по убыванию
                size = int(input("Размер массива для сортировки: "))
                array = [random.randint(1, 100) for _ in range(size)]
                
                print(f"\n📊 Исходный массив: {array}")
                sorted_array, exec_time = heap_sort(array, reverse=True)
                print(f"\n✅ Отсортированный массив (↓): {sorted_array}")
                print(f"⏱️  Время выполнения: {exec_time:.4f} мс")
            
            elif choice == '0':
                print("\n👋 До свидания!\n")
                break
            
            else:
                print("\n❌ Неверный выбор!")
        
        except ValueError:
            print("\n❌ Ошибка: введите целое число!")
        except KeyboardInterrupt:
            print("\n\n👋 Программа прервана. До свидания!\n")
            break
        except Exception as e:
            print(f"\n❌ Произошла ошибка: {e}")


if __name__ == "__main__":
    main()
