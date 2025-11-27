# ДВОИЧНОЕ ДЕРЕВО ПОИСКА (Binary Search Tree)
# Каждый узел имеет максимум 2 детей: левый и правый
# Правило: левый < родитель < правый

def create_node(value):
    """Создать узел дерева"""
    return {
        'value': value,
        'left': None,   # левый ребёнок
        'right': None   # правый ребёнок
    }


def insert(root, value):
    """Вставка элемента в дерево"""
    # Если дерево пустое - создаём корень
    if root is None:
        return create_node(value)
    
    # Рекурсивная вставка
    if value < root['value']:
        # Если меньше - идём влево
        root['left'] = insert(root['left'], value)
    elif value > root['value']:
        # Если больше - идём вправо
        root['right'] = insert(root['right'], value)
    else:
        # Если равно - не добавляем дубликаты
        print(f"Значение {value} уже есть в дереве")
    
    return root


def find_min(node):
    """Найти минимальный элемент (самый левый)"""
    current = node
    while current['left'] is not None:
        current = current['left']
    return current


def delete(root, value):
    """Удаление элемента из дерева"""
    if root is None:
        print(f"Значение {value} не найдено")
        return None
    
    # Ищем элемент для удаления
    if value < root['value']:
        root['left'] = delete(root['left'], value)
    elif value > root['value']:
        root['right'] = delete(root['right'], value)
    else:
        # Нашли элемент! Удаляем
        print(f"Удаляем {value}")
        
        # Случай 1: нет детей (лист)
        if root['left'] is None and root['right'] is None:
            return None
        
        # Случай 2: один ребёнок
        if root['left'] is None:
            return root['right']
        if root['right'] is None:
            return root['left']
        
        # Случай 3: два ребёнка
        # Находим минимум в правом поддереве
        min_node = find_min(root['right'])
        root['value'] = min_node['value']
        root['right'] = delete(root['right'], min_node['value'])
    
    return root


# ============== ПОИСК В ГЛУБИНУ (DFS - Depth First Search) ==============

def dfs_inorder_recursive(node, result=None):
    """Симметричный обход (In-order): ЛЕВЫЙ -> КОРЕНЬ -> ПРАВЫЙ
    Результат: отсортированный список"""
    if result is None:
        result = []
    
    if node is not None:
        dfs_inorder_recursive(node['left'], result)    # Левое поддерево
        result.append(node['value'])                    # Корень
        dfs_inorder_recursive(node['right'], result)   # Правое поддерево
    
    return result


def dfs_preorder_recursive(node, result=None):
    """Прямой обход (Pre-order): КОРЕНЬ -> ЛЕВЫЙ -> ПРАВЫЙ
    Используется для копирования дерева"""
    if result is None:
        result = []
    
    if node is not None:
        result.append(node['value'])                     # Корень
        dfs_preorder_recursive(node['left'], result)    # Левое поддерево
        dfs_preorder_recursive(node['right'], result)   # Правое поддерево
    
    return result


def dfs_postorder_recursive(node, result=None):
    """Обратный обход (Post-order): ЛЕВЫЙ -> ПРАВЫЙ -> КОРЕНЬ
    Используется для удаления дерева"""
    if result is None:
        result = []
    
    if node is not None:
        dfs_postorder_recursive(node['left'], result)   # Левое поддерево
        dfs_postorder_recursive(node['right'], result)  # Правое поддерево
        result.append(node['value'])                     # Корень
    
    return result


def dfs_inorder_iterative(root):
    """Симметричный обход (итеративный) - используем стек"""
    result = []
    stack = []
    current = root
    
    while current is not None or stack:
        # Идём максимально влево
        while current is not None:
            stack.append(current)
            current = current['left']
        
        # Берём узел из стека
        current = stack.pop()
        result.append(current['value'])
        
        # Переходим вправо
        current = current['right']
    
    return result


def dfs_preorder_iterative(root):
    """Прямой обход (итеративный) - используем стек"""
    if root is None:
        return []
    
    result = []
    stack = [root]
    
    while stack:
        node = stack.pop()
        result.append(node['value'])
        
        # Сначала правый (чтобы левый обработался первым)
        if node['right']:
            stack.append(node['right'])
        if node['left']:
            stack.append(node['left'])
    
    return result


def dfs_postorder_iterative(root):
    """Обратный обход (итеративный) - используем два стека"""
    if root is None:
        return []
    
    result = []
    stack1 = [root]
    stack2 = []
    
    while stack1:
        node = stack1.pop()
        stack2.append(node)
        
        if node['left']:
            stack1.append(node['left'])
        if node['right']:
            stack1.append(node['right'])
    
    while stack2:
        result.append(stack2.pop()['value'])
    
    return result


# ============== ПОИСК В ШИРИНУ (BFS - Breadth First Search) ==============

def bfs_iterative(root):
    """Поиск в ширину (итеративный) - используем очередь
    Обходим дерево уровень за уровнем"""
    if root is None:
        return []
    
    result = []
    queue = [root]  # Используем список как очередь
    
    while queue:
        node = queue.pop(0)  # Берём первый элемент
        result.append(node['value'])
        
        # Добавляем детей в очередь
        if node['left']:
            queue.append(node['left'])
        if node['right']:
            queue.append(node['right'])
    
    return result


def bfs_recursive(root):
    """Поиск в ширину (рекурсивный) - обход по уровням"""
    if root is None:
        return []
    
    result = []
    
    def process_level(nodes):
        if not nodes:
            return
        
        next_level = []
        for node in nodes:
            result.append(node['value'])
            if node['left']:
                next_level.append(node['left'])
            if node['right']:
                next_level.append(node['right'])
        
        process_level(next_level)
    
    process_level([root])
    return result


# ============== ВИЗУАЛИЗАЦИЯ ДЕРЕВА ==============

def display_tree(root, level=0, prefix="Root: "):
    """Красивый вывод дерева в консоль"""
    if root is None:
        return
    
    print(" " * (level * 4) + prefix + str(root['value']))
    
    if root['left'] is not None or root['right'] is not None:
        if root['left']:
            display_tree(root['left'], level + 1, "L--- ")
        else:
            print(" " * ((level + 1) * 4) + "L--- None")
        
        if root['right']:
            display_tree(root['right'], level + 1, "R--- ")
        else:
            print(" " * ((level + 1) * 4) + "R--- None")


def display_tree_compact(root):
    """Компактный вывод дерева"""
    if root is None:
        print("Дерево пустое")
        return
    
    print("\n" + "="*50)
    display_tree(root)
    print("="*50 + "\n")


# ============== ГЛАВНАЯ ПРОГРАММА ==============

if __name__ == "__main__":
    print("🌳 ДВОИЧНОЕ ДЕРЕВО ПОИСКА 🌳\n")
    
    # Создаём дерево
    tree = None
    
    # Вставляем элементы
    print("=== ВСТАВКА ЭЛЕМЕНТОВ ===")
    values = [50, 30, 70, 20, 40, 60, 80]
    for val in values:
        tree = insert(tree, val)
        print(f"Вставлен {val}")
    
    display_tree_compact(tree)
    
    # Пытаемся вставить дубликат
    print("\n=== ПОПЫТКА ВСТАВИТЬ ДУБЛИКАТ ===")
    tree = insert(tree, 50)
    
    # Поиск в глубину (DFS)
    print("\n=== ПОИСК В ГЛУБИНУ (DFS) - РЕКУРСИВНЫЙ ===")
    print("Симметричный (In-order):", dfs_inorder_recursive(tree))
    print("Прямой (Pre-order):", dfs_preorder_recursive(tree))
    print("Обратный (Post-order):", dfs_postorder_recursive(tree))
    
    print("\n=== ПОИСК В ГЛУБИНУ (DFS) - ИТЕРАТИВНЫЙ ===")
    print("Симметричный (In-order):", dfs_inorder_iterative(tree))
    print("Прямой (Pre-order):", dfs_preorder_iterative(tree))
    print("Обратный (Post-order):", dfs_postorder_iterative(tree))
    
    # Поиск в ширину (BFS)
    print("\n=== ПОИСК В ШИРИНУ (BFS) ===")
    print("Итеративный:", bfs_iterative(tree))
    print("Рекурсивный:", bfs_recursive(tree))
    
    # Удаление элементов
    print("\n=== УДАЛЕНИЕ ЭЛЕМЕНТОВ ===")
    
    print("\n1. Удаление листа (20):")
    tree = delete(tree, 20)
    display_tree_compact(tree)
    
    print("\n2. Удаление узла с одним ребёнком (30):")
    tree = delete(tree, 30)
    display_tree_compact(tree)
    
    print("\n3. Удаление узла с двумя детьми (50 - корень):")
    tree = delete(tree, 50)
    display_tree_compact(tree)
    
    print("\n4. Попытка удалить несуществующий элемент (100):")
    tree = delete(tree, 100)
    
    print("\n=== ФИНАЛЬНОЕ ДЕРЕВО ===")
    display_tree_compact(tree)
    print("Симметричный обход (отсортированные значения):", dfs_inorder_recursive(tree))
