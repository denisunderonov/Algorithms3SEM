"""
ЛР21: Анализ сложности алгоритмов

Тестирование производительности на размерах: 100, 1000, 10000 элементов.

Алгоритмы:
1. Бинарное дерево поиска (BST): вставка, поиск, удаление
2. Хеш-таблица: вставка, поиск, обработка коллизий
3. Пирамидальная сортировка (heap sort)
4. Обходы графа: BFS, DFS (рекурсивный и итеративный)
"""

import time
import random
from typing import List, Tuple, Callable
import sys


# ============================================================================
# 1. БИНАРНОЕ ДЕРЕВО ПОИСКА (BST)
# ============================================================================

class BSTNode:
    """
    Узел бинарного дерева поиска.
    
    Структура узла:
    - value: хранимое значение
    - left: ссылка на левого ребёнка (меньшие значения)
    - right: ссылка на правого ребёнка (большие значения)
    """
    def __init__(self, value):
        self.value = value  # Значение, хранящееся в узле
        self.left = None    # Левый ребёнок (изначально отсутствует)
        self.right = None   # Правый ребёнок (изначально отсутствует)


class BinarySearchTree:
    """
    Бинарное дерево поиска (BST).
    
    СВОЙСТВО BST:
    - Все значения в левом поддереве < значения узла
    - Все значения в правом поддереве > значения узла
    
    Это свойство позволяет быстро искать элементы (как бинарный поиск).
    """
    def __init__(self):
        self.root = None  # Корень дерева (изначально дерево пустое)
    
    def insert(self, value):
        """
        Вставка элемента в BST.
        Сложность: O(log n) в среднем, O(n) в худшем (если дерево вырождается в список).
        """
        # Если дерево пустое — создаём корень
        if self.root is None:
            self.root = BSTNode(value)
        else:
            # Иначе вызываем рекурсивную вставку
            self._insert_recursive(self.root, value)
    
    def _insert_recursive(self, node, value):
        """
        Рекурсивная вставка элемента.
        Спускаемся по дереву, пока не найдём место для нового узла.
        """
        # Если новое значение меньше текущего узла — идём влево
        if value < node.value:
            if node.left is None:
                # Нашли место — создаём левого ребёнка
                node.left = BSTNode(value)
            else:
                # Продолжаем спуск влево (рекурсия)
                self._insert_recursive(node.left, value)
        else:
            # Иначе (value >= node.value) — идём вправо
            if node.right is None:
                # Нашли место — создаём правого ребёнка
                node.right = BSTNode(value)
            else:
                # Продолжаем спуск вправо (рекурсия)
                self._insert_recursive(node.right, value)
    
    def search(self, value) -> bool:
        """
        Поиск элемента в BST.
        Сложность: O(log n) в среднем, O(n) в худшем.
        """
        return self._search_recursive(self.root, value)
    
    def _search_recursive(self, node, value) -> bool:
        """Рекурсивный поиск элемента."""
        # Если дошли до конца (пустой узел) — элемент не найден
        if node is None:
            return False
        
        # Если значение совпало — нашли!
        if node.value == value:
            return True
        # Если искомое значение меньше — ищем в левом поддереве
        elif value < node.value:
            return self._search_recursive(node.left, value)
        # Иначе — ищем в правом поддереве
        else:
            return self._search_recursive(node.right, value)
    
    def delete(self, value):
        """
        Удаление элемента из BST.
        Сложность: O(log n) в среднем, O(n) в худшем.
        """
        self.root = self._delete_recursive(self.root, value)
    
    def _delete_recursive(self, node, value):
        """
        Рекурсивное удаление элемента.
        Возвращает новый корень поддерева после удаления.
        """
        # Если узел пустой — удалять нечего
        if node is None:
            return None
        
        # Ищем узел для удаления
        if value < node.value:
            # Удаляемый элемент в левом поддереве
            node.left = self._delete_recursive(node.left, value)
        elif value > node.value:
            # Удаляемый элемент в правом поддереве
            node.right = self._delete_recursive(node.right, value)
        else:
            # НАШЛИ узел для удаления!
            # Рассматриваем 3 случая:
            
            # Случай 1: нет левого ребёнка
            if node.left is None:
                # Заменяем узел его правым ребёнком (может быть None)
                return node.right
            
            # Случай 2: нет правого ребёнка
            elif node.right is None:
                # Заменяем узел его левым ребёнком
                return node.left
            
            else:
                # Случай 3: есть оба ребёнка (самый сложный)
                # Заменяем значение на минимум из правого поддерева
                # (это сохранит свойство BST)
                min_node = self._find_min(node.right)
                node.value = min_node.value  # Копируем значение
                # Удаляем минимальный узел из правого поддерева
                node.right = self._delete_recursive(node.right, min_node.value)
        
        return node
    
    def _find_min(self, node):
        """
        Найти узел с минимальным значением в поддереве.
        Минимум всегда в самом левом узле.
        """
        # Спускаемся влево, пока можем
        while node.left is not None:
            node = node.left
        return node


# ============================================================================
# 2. ХЕШ-ТАБЛИЦА
# ============================================================================

class HashTable:
    """
    Хеш-таблица с методом цепочек для разрешения коллизий.
    
    ЧТО ТАКОЕ ХЕШ-ТАБЛИЦА?
    - Структура данных для быстрого поиска по ключу
    - Использует хеш-функцию для преобразования ключа в индекс массива
    - Сложность операций: O(1) в среднем!
    
    КОЛЛИЗИЯ — когда два разных ключа имеют один хеш.
    Решение: метод цепочек (в каждой ячейке — список элементов).
    """
    def __init__(self, size=100):
        """
        Инициализация хеш-таблицы.
        size — размер внутреннего массива (количество "корзин").
        """
        self.size = size  # Размер таблицы
        # Создаём массив пустых списков (цепочки для коллизий)
        self.table = [[] for _ in range(size)]
    
    def _hash(self, value):
        """
        Хеш-функция — преобразует значение в индекс таблицы.
        
        Работа:
        1. hash(value) — встроенная функция Python (возвращает большое число)
        2. % self.size — берём остаток от деления (получаем индекс от 0 до size-1)
        
        Сложность: O(1)
        """
        return hash(value) % self.size
    
    def insert(self, value):
        """
        Вставка элемента в хеш-таблицу.
        Сложность: O(1) в среднем, O(n) в худшем при больших коллизиях.
        """
        # Вычисляем индекс, куда положить элемент
        index = self._hash(value)
        
        # Проверяем: элемент уже есть в этой цепочке?
        if value not in self.table[index]:
            # Нет — добавляем в конец списка (цепочки)
            self.table[index].append(value)
        # Если элемент уже есть — ничего не делаем (избегаем дубликатов)
    
    def search(self, value) -> bool:
        """
        Поиск элемента в хеш-таблице.
        Сложность: O(1) в среднем, O(n) в худшем при длинной цепочке.
        """
        # Вычисляем индекс, где должен быть элемент
        index = self._hash(value)
        
        # Проверяем наличие в цепочке (списке)
        # Оператор 'in' для списка работает за O(длина_списка)
        return value in self.table[index]
    
    def delete(self, value):
        """
        Удаление элемента из хеш-таблицы.
        Сложность: O(1) в среднем, O(n) в худшем при длинной цепочке.
        """
        # Вычисляем индекс
        index = self._hash(value)
        
        # Если элемент есть в цепочке — удаляем
        if value in self.table[index]:
            self.table[index].remove(value)


# ============================================================================
# 3. ПИРАМИДАЛЬНАЯ СОРТИРОВКА
# ============================================================================

def heapify(arr: List[int], n: int, i: int):
    """
    Процедура просеивания (heapify) для построения кучи.
    
    ЧТО ТАКОЕ КУЧА (HEAP)?
    - Двоичное дерево, где родитель >= детей (max-heap)
    - Можно хранить в массиве: для элемента i дети находятся в 2*i+1 и 2*i+2
    
    ПРОСЕИВАНИЕ — "опускаем" элемент вниз, пока он не станет больше детей.
    
    Параметры:
    - arr: массив (представление кучи)
    - n: размер кучи (может быть меньше len(arr))
    - i: индекс элемента, который нужно просеять
    
    Сложность: O(log n) — высота дерева
    """
    # Предполагаем, что самый большой элемент — текущий (i)
    largest = i
    
    # Вычисляем индексы детей в массиве
    # Левый ребёнок находится на позиции 2*i + 1
    left = 2 * i + 1
    # Правый ребёнок находится на позиции 2*i + 2
    right = 2 * i + 2
    
    # Проверяем левого ребёнка:
    # Если он существует (left < n) И больше текущего largest
    if left < n and arr[left] > arr[largest]:
        # То левый ребёнок — новый кандидат на самый большой
        largest = left
    
    # Проверяем правого ребёнка:
    # Если он существует (right < n) И больше текущего largest
    if right < n and arr[right] > arr[largest]:
        # То правый ребёнок — новый самый большой
        largest = right
    
    # Если самый большой элемент НЕ текущий (largest изменился)
    if largest != i:
        # Меняем местами текущий элемент и самый большой
        arr[i], arr[largest] = arr[largest], arr[i]
        
        # РЕКУРСИЯ: продолжаем просеивать элемент дальше вниз
        # Теперь наш элемент находится на позиции largest
        heapify(arr, n, largest)


def heap_sort(arr: List[int]):
    """
    Пирамидальная сортировка (Heap Sort).
    
    АЛГОРИТМ:
    1. Строим max-heap из массива (самый большой элемент — в корне)
    2. Берём корень (максимум), ставим в конец массива
    3. Уменьшаем размер кучи и восстанавливаем свойство кучи
    4. Повторяем, пока куча не опустеет
    
    Результат: отсортированный массив (от меньшего к большему).
    
    Сложность: O(n log n) всегда (даже в худшем случае)
    """
    n = len(arr)
    
    # ЭТАП 1: Построение max-heap
    # Проходим от середины массива к началу
    # (элементы после n//2 — это листья, их просеивать не нужно)
    for i in range(n // 2 - 1, -1, -1):
        # Просеиваем каждый элемент (он "опустится" на своё место)
        heapify(arr, n, i)
    
    # ЭТАП 2: Извлечение элементов из кучи
    # Идём с конца массива к началу
    for i in range(n - 1, 0, -1):
        # Меняем местами корень (максимум) и последний элемент кучи
        # Максимум теперь на своём месте в конце
        arr[0], arr[i] = arr[i], arr[0]
        
        # Восстанавливаем свойство кучи для оставшихся элементов
        # Размер кучи теперь i (последний элемент уже на месте)
        heapify(arr, i, 0)


# ============================================================================
# 4. ОБХОДЫ ГРАФА
# ============================================================================

from collections import deque


class Graph:
    """
    Граф, представленный матрицей смежности.
    Используется для тестирования обходов BFS и DFS.
    """
    def __init__(self, n: int):
        """
        Создать пустой граф с n вершинами.
        """
        self.n = n  # Количество вершин
        # Создаём матрицу смежности n×n, заполненную нулями
        # matrix[i][j] = 1 означает "есть ребро между i и j"
        self.matrix = [[0] * n for _ in range(n)]
    
    def add_edge(self, u: int, v: int):
        """
        Добавить ребро между вершинами u и v.
        Граф неориентированный — добавляем в обе стороны.
        """
        self.matrix[u][v] = 1  # Ребро u -> v
        self.matrix[v][u] = 1  # Ребро v -> u (неориентированный граф)
    
    def neighbors(self, v: int) -> List[int]:
        """
        Получить всех соседей вершины v.
        Сложность: O(n) для матрицы смежности (проверяем всю строку).
        """
        # Проходим по строке v и собираем индексы, где matrix[v][i] == 1
        return [i for i in range(self.n) if self.matrix[v][i]]
    
    def bfs(self, start: int) -> List[int]:
        """
        Обход в ширину (BFS).
        Сложность: O(n²) для матрицы смежности (для каждой вершины проверяем n соседей).
        """
        # Массив посещённых вершин
        visited = [False] * self.n
        # Порядок обхода
        order = []
        # Очередь для BFS
        q = deque([start])
        visited[start] = True
        
        # Пока очередь не пуста
        while q:
            # Берём первую вершину из очереди
            v = q.popleft()
            # Записываем её в результат
            order.append(v)
            # Проходим по всем соседям
            for u in self.neighbors(v):
                # Если сосед не посещён
                if not visited[u]:
                    # Помечаем как посещённый
                    visited[u] = True
                    # Добавляем в очередь
                    q.append(u)
        
        return order
    
    def dfs_recursive(self, start: int) -> List[int]:
        """
        Обход в глубину (рекурсивный).
        Сложность: O(n²) для матрицы смежности.
        """
        visited = [False] * self.n
        order = []
        
        def _dfs(v: int):
            """Внутренняя рекурсивная функция DFS."""
            # Помечаем вершину как посещённую
            visited[v] = True
            # Добавляем в результат
            order.append(v)
            # Рекурсивно обходим соседей
            for u in self.neighbors(v):
                if not visited[u]:
                    _dfs(u)
        
        # Запускаем обход от стартовой вершины
        _dfs(start)
        return order
    
    def dfs_iterative(self, start: int) -> List[int]:
        """
        Обход в глубину (итеративный, со стеком).
        Сложность: O(n²) для матрицы смежности.
        """
        visited = [False] * self.n
        order = []
        # Стек для DFS (используем список)
        stack = [start]
        
        # Пока стек не пуст
        while stack:
            # Берём вершину с верха стека
            v = stack.pop()
            # Если уже посещали — пропускаем
            if visited[v]:
                continue
            # Помечаем как посещённую
            visited[v] = True
            # Записываем в результат
            order.append(v)
            
            # Добавляем соседей в стек (в обратном порядке)
            for u in reversed(self.neighbors(v)):
                if not visited[u]:
                    stack.append(u)
        
        return order


# ============================================================================
# ТЕСТИРОВАНИЕ И ЗАМЕРЫ
# ============================================================================

def measure_time(func: Callable, *args) -> float:
    """Измерить время выполнения функции в секундах."""
    start = time.perf_counter()
    func(*args)
    end = time.perf_counter()
    return end - start


def test_bst(size: int) -> dict:
    """Тестирование бинарного дерева поиска."""
    print(f"\n--- Бинарное дерево поиска (BST), размер: {size} ---")
    
    bst = BinarySearchTree()
    data = list(range(size))
    random.shuffle(data)
    
    # Вставка
    insert_time = measure_time(lambda: [bst.insert(x) for x in data])
    print(f"  Вставка {size} элементов: {insert_time:.6f} сек")
    
    # Поиск
    search_data = random.sample(data, min(100, size))
    search_time = measure_time(lambda: [bst.search(x) for x in search_data])
    print(f"  Поиск {len(search_data)} элементов: {search_time:.6f} сек")
    
    # Удаление
    delete_data = random.sample(data, min(100, size))
    delete_time = measure_time(lambda: [bst.delete(x) for x in delete_data])
    print(f"  Удаление {len(delete_data)} элементов: {delete_time:.6f} сек")
    
    return {
        'insert': insert_time,
        'search': search_time,
        'delete': delete_time
    }


def test_hash_table(size: int) -> dict:
    """Тестирование хеш-таблицы."""
    print(f"\n--- Хеш-таблица, размер: {size} ---")
    
    # Размер таблицы ~10% от количества элементов для демонстрации коллизий
    table_size = max(10, size // 10)
    ht = HashTable(table_size)
    data = list(range(size))
    random.shuffle(data)
    
    # Вставка
    insert_time = measure_time(lambda: [ht.insert(x) for x in data])
    print(f"  Вставка {size} элементов: {insert_time:.6f} сек")
    
    # Поиск
    search_data = random.sample(data, min(100, size))
    search_time = measure_time(lambda: [ht.search(x) for x in search_data])
    print(f"  Поиск {len(search_data)} элементов: {search_time:.6f} сек")
    
    # Удаление
    delete_data = random.sample(data, min(100, size))
    delete_time = measure_time(lambda: [ht.delete(x) for x in delete_data])
    print(f"  Удаление {len(delete_data)} элементов: {delete_time:.6f} сек")
    
    # Анализ коллизий
    collisions = sum(1 for bucket in ht.table if len(bucket) > 1)
    max_chain = max(len(bucket) for bucket in ht.table)
    print(f"  Коллизий: {collisions}/{table_size} ({collisions/table_size*100:.1f}%)")
    print(f"  Макс. длина цепочки: {max_chain}")
    
    return {
        'insert': insert_time,
        'search': search_time,
        'delete': delete_time,
        'collisions': collisions,
        'max_chain': max_chain
    }


def test_heap_sort(size: int) -> dict:
    """Тестирование пирамидальной сортировки."""
    print(f"\n--- Пирамидальная сортировка, размер: {size} ---")
    
    data = list(range(size))
    random.shuffle(data)
    
    # Сортировка
    sort_time = measure_time(heap_sort, data.copy())
    print(f"  Сортировка {size} элементов: {sort_time:.6f} сек")
    
    return {
        'sort': sort_time
    }


def test_graph_traversal(size: int) -> dict:
    """Тестирование обходов графа."""
    print(f"\n--- Обходы графа, размер: {size} вершин ---")
    
    # Создаём связный граф (каждая вершина связана со следующей)
    g = Graph(size)
    for i in range(size - 1):
        g.add_edge(i, i + 1)
    
    # Добавляем случайные рёбра для усложнения
    num_extra_edges = min(size // 2, 100)
    for _ in range(num_extra_edges):
        u = random.randint(0, size - 1)
        v = random.randint(0, size - 1)
        if u != v:
            g.add_edge(u, v)
    
    # BFS
    bfs_time = measure_time(g.bfs, 0)
    print(f"  BFS: {bfs_time:.6f} сек")
    
    # DFS рекурсивный
    sys.setrecursionlimit(max(1000, size + 100))
    dfs_rec_time = measure_time(g.dfs_recursive, 0)
    print(f"  DFS (рекурсивный): {dfs_rec_time:.6f} сек")
    
    # DFS итеративный
    dfs_iter_time = measure_time(g.dfs_iterative, 0)
    print(f"  DFS (итеративный): {dfs_iter_time:.6f} сек")
    
    return {
        'bfs': bfs_time,
        'dfs_recursive': dfs_rec_time,
        'dfs_iterative': dfs_iter_time
    }


# ============================================================================
# ГЛАВНАЯ ФУНКЦИЯ
# ============================================================================

def main():
    """Запуск всех тестов на размерах 100, 1000, 10000."""
    print("ЛР21: АНАЛИЗ СЛОЖНОСТИ АЛГОРИТМОВ")
    print("=" * 60)
    
    sizes = [100, 1000, 10000]
    results = {size: {} for size in sizes}
    
    for size in sizes:
        print(f"\nТестирование на {size} элементах:")
        print("-" * 60)
        
        # 1. Бинарное дерево поиска
        results[size]['bst'] = test_bst(size)
        
        # 2. Хеш-таблица
        results[size]['hash'] = test_hash_table(size)
        
        # 3. Пирамидальная сортировка
        results[size]['heap_sort'] = test_heap_sort(size)
        
        # 4. Обходы графа (только для 100 и 1000)
        if size <= 1000:
            results[size]['graph'] = test_graph_traversal(size)
        else:
            print(f"\n--- Обходы графа (пропущены для {size}) ---")
            results[size]['graph'] = {'bfs': None, 'dfs_recursive': None, 'dfs_iterative': None}
    
    # Сводная таблица
    print("\n" + "=" * 60)
    print("РЕЗУЛЬТАТЫ")
    print("=" * 60)
    
    print("\nБинарное дерево поиска:")
    print("  Операция      n=100      n=1000     n=10000")
    print(f"  Вставка      {results[100]['bst']['insert']:.6f}   {results[1000]['bst']['insert']:.6f}   {results[10000]['bst']['insert']:.6f}")
    print(f"  Поиск        {results[100]['bst']['search']:.6f}   {results[1000]['bst']['search']:.6f}   {results[10000]['bst']['search']:.6f}")
    print(f"  Удаление     {results[100]['bst']['delete']:.6f}   {results[1000]['bst']['delete']:.6f}   {results[10000]['bst']['delete']:.6f}")
    
    print("\nХеш-таблица:")
    print("  Операция      n=100      n=1000     n=10000")
    print(f"  Вставка      {results[100]['hash']['insert']:.6f}   {results[1000]['hash']['insert']:.6f}   {results[10000]['hash']['insert']:.6f}")
    print(f"  Поиск        {results[100]['hash']['search']:.6f}   {results[1000]['hash']['search']:.6f}   {results[10000]['hash']['search']:.6f}")
    
    print("\nПирамидальная сортировка:")
    print("  Размер        Время")
    print(f"  n=100        {results[100]['heap_sort']['sort']:.6f}")
    print(f"  n=1000       {results[1000]['heap_sort']['sort']:.6f}")
    print(f"  n=10000      {results[10000]['heap_sort']['sort']:.6f}")
    
    print("\nОбходы графа:")
    print("  Метод         n=100      n=1000")
    print(f"  BFS          {results[100]['graph']['bfs']:.6f}   {results[1000]['graph']['bfs']:.6f}")
    print(f"  DFS (рек)    {results[100]['graph']['dfs_recursive']:.6f}   {results[1000]['graph']['dfs_recursive']:.6f}")
    print(f"  DFS (итер)   {results[100]['graph']['dfs_iterative']:.6f}   {results[1000]['graph']['dfs_iterative']:.6f}")
    
    print("\n" + "=" * 60)
    print("Сложность алгоритмов:")
    print("  BST: O(log n) средняя, O(n) худшая")
    print("  Хеш-таблица: O(1) средняя, O(n) худшая")
    print("  Heap Sort: O(n log n) всегда")
    print("  BFS/DFS: O(V + E)")
    print("=" * 60)


if __name__ == "__main__":
    main()

