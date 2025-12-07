# -*- coding: utf-8 -*-# ИНТЕРАКТИВНАЯ ПРОГРАММА ДЛЯ РАБОТЫ С ДВОИЧНЫМ ДЕРЕВОМ

"""# Здесь вы можете сами вставлять/удалять элементы

ИНТЕРАКТИВНОЕ ДВОИЧНОЕ ДЕРЕВО ПОИСКА

С визуализацией и всеми видами обходаfrom binary_tree import *

"""

def print_menu():

def create_node(value):    """Показать меню"""

    """Создать узел дерева"""    print("\n" + "="*50)

    return {    print("🌳 МЕНЮ ДВОИЧНОГО ДЕРЕВА")

        'value': value,    print("="*50)

        'left': None,    print("1. Вставить элемент")

        'right': None    print("2. Удалить элемент")

    }    print("3. Показать дерево")

    print("4. DFS - Симметричный обход (in-order)")

    print("5. DFS - Прямой обход (pre-order)")

def insert(root, value):    print("6. DFS - Обратный обход (post-order)")

    """Вставка элемента в дерево"""    print("7. BFS - Поиск в ширину")

    if root is None:    print("8. Показать все обходы")

        return create_node(value)    print("9. Создать дерево из списка")

        print("0. Выход")

    if value < root['value']:    print("="*50)

        root['left'] = insert(root['left'], value)

    elif value > root['value']:

        root['right'] = insert(root['right'], value)def show_all_traversals(tree):

    else:    """Показать все виды обходов"""

        print(f"⚠️  Значение {value} уже существует в дереве!")    if tree is None:

            print("❌ Дерево пустое!")

    return root        return

    

    print("\n" + "="*50)

def find_min(node):    print("📊 ВСЕ ВИДЫ ОБХОДОВ")

    """Найти минимальный элемент (самый левый)"""    print("="*50)

    current = node    

    while current['left'] is not None:    print("\n🔄 ПОИСК В ГЛУБИНУ (DFS) - Рекурсивный:")

        current = current['left']    print("├─ Симметричный (In-order):  ", dfs_inorder_recursive(tree))

    return current    print("├─ Прямой (Pre-order):       ", dfs_preorder_recursive(tree))

    print("└─ Обратный (Post-order):    ", dfs_postorder_recursive(tree))

    

def delete(root, value):    print("\n🔄 ПОИСК В ГЛУБИНУ (DFS) - Итеративный:")

    """Удаление элемента из дерева"""    print("├─ Симметричный (In-order):  ", dfs_inorder_iterative(tree))

    if root is None:    print("├─ Прямой (Pre-order):       ", dfs_preorder_iterative(tree))

        return None, False    print("└─ Обратный (Post-order):    ", dfs_postorder_iterative(tree))

    

    deleted = False    print("\n🌊 ПОИСК В ШИРИНУ (BFS):")

        print("├─ Итеративный:              ", bfs_iterative(tree))

    if value < root['value']:    print("└─ Рекурсивный:              ", bfs_recursive(tree))

        root['left'], deleted = delete(root['left'], value)    print("="*50)

    elif value > root['value']:

        root['right'], deleted = delete(root['right'], value)

    else:def main():

        # Нашли элемент!    """Главная функция"""

        deleted = True    tree = None

            

        # Случай 1: нет детей (лист)    print("\n🌳 ИНТЕРАКТИВНАЯ ПРОГРАММА - ДВОИЧНОЕ ДЕРЕВО 🌳")

        if root['left'] is None and root['right'] is None:    print("\nДобро пожаловать! Сейчас дерево пустое.")

            return None, deleted    print("Начните с добавления элементов (пункт 1) или создайте дерево из списка (пункт 9)")

            

        # Случай 2: один ребёнок    while True:

        if root['left'] is None:        print_menu()

            return root['right'], deleted        

        if root['right'] is None:        try:

            return root['left'], deleted            choice = input("\n👉 Выберите действие (0-9): ").strip()

                    

        # Случай 3: два ребёнка            if choice == '0':

        min_node = find_min(root['right'])                print("\n👋 До свидания!")

        root['value'] = min_node['value']                break

        root['right'], _ = delete(root['right'], min_node['value'])            

                elif choice == '1':

    return root, deleted                # Вставка

                value = int(input("Введите число для вставки: "))

                tree = insert(tree, value)

# ============== ПОИСК В ГЛУБИНУ (DFS) ==============                print(f"✅ Элемент {value} добавлен!")

                display_tree_compact(tree)

def dfs_inorder_recursive(node, result=None):            

    """Симметричный обход (In-order): ЛЕВЫЙ → КОРЕНЬ → ПРАВЫЙ"""            elif choice == '2':

    if result is None:                # Удаление

        result = []                if tree is None:

                        print("❌ Дерево пустое! Сначала добавьте элементы.")

    if node is not None:                    continue

        dfs_inorder_recursive(node['left'], result)                

        result.append(node['value'])                value = int(input("Введите число для удаления: "))

        dfs_inorder_recursive(node['right'], result)                tree = delete(tree, value)

                    display_tree_compact(tree)

    return result            

            elif choice == '3':

                # Показать дерево

def dfs_preorder_recursive(node, result=None):                if tree is None:

    """Прямой обход (Pre-order): КОРЕНЬ → ЛЕВЫЙ → ПРАВЫЙ"""                    print("❌ Дерево пустое!")

    if result is None:                else:

        result = []                    display_tree_compact(tree)

                

    if node is not None:            elif choice == '4':

        result.append(node['value'])                # Симметричный обход

        dfs_preorder_recursive(node['left'], result)                if tree is None:

        dfs_preorder_recursive(node['right'], result)                    print("❌ Дерево пустое!")

                    else:

    return result                    print("\n🔄 Симметричный обход (In-order):")

                    print("Рекурсивный:  ", dfs_inorder_recursive(tree))

                    print("Итеративный:  ", dfs_inorder_iterative(tree))

def dfs_postorder_recursive(node, result=None):            

    """Обратный обход (Post-order): ЛЕВЫЙ → ПРАВЫЙ → КОРЕНЬ"""            elif choice == '5':

    if result is None:                # Прямой обход

        result = []                if tree is None:

                        print("❌ Дерево пустое!")

    if node is not None:                else:

        dfs_postorder_recursive(node['left'], result)                    print("\n🔄 Прямой обход (Pre-order):")

        dfs_postorder_recursive(node['right'], result)                    print("Рекурсивный:  ", dfs_preorder_recursive(tree))

        result.append(node['value'])                    print("Итеративный:  ", dfs_preorder_iterative(tree))

                

    return result            elif choice == '6':

                # Обратный обход

                if tree is None:

def dfs_inorder_iterative(root):                    print("❌ Дерево пустое!")

    """Симметричный обход (итеративный) - используем СТЕК"""                else:

    result = []                    print("\n🔄 Обратный обход (Post-order):")

    stack = []                    print("Рекурсивный:  ", dfs_postorder_recursive(tree))

    current = root                    print("Итеративный:  ", dfs_postorder_iterative(tree))

                

    while current is not None or stack:            elif choice == '7':

        # Идём максимально влево                # Поиск в ширину

        while current is not None:                if tree is None:

            stack.append(current)                    print("❌ Дерево пустое!")

            current = current['left']                else:

                            print("\n🌊 Поиск в ширину (BFS):")

        # Берём узел из стека                    print("Итеративный:  ", bfs_iterative(tree))

        current = stack.pop()                    print("Рекурсивный:  ", bfs_recursive(tree))

        result.append(current['value'])            

                    elif choice == '8':

        # Переходим вправо                # Все обходы

        current = current['right']                show_all_traversals(tree)

                

    return result            elif choice == '9':

                # Создать дерево из списка

                print("\nВведите числа через пробел (например: 50 30 70 20 40 60 80)")

def dfs_preorder_iterative(root):                numbers = input("👉 Числа: ").strip().split()

    """Прямой обход (итеративный) - используем СТЕК"""                

    if root is None:                tree = None  # Очищаем дерево

        return []                for num in numbers:

                        tree = insert(tree, int(num))

    result = []                

    stack = [root]                print(f"\n✅ Создано дерево из {len(numbers)} элементов!")

                    display_tree_compact(tree)

    while stack:            

        node = stack.pop()            else:

        result.append(node['value'])                print("❌ Неверный выбор! Попробуйте ещё раз.")

                

        # Сначала правый (чтобы левый обработался первым)        except ValueError:

        if node['right']:            print("❌ Ошибка! Введите корректное число.")

            stack.append(node['right'])        except KeyboardInterrupt:

        if node['left']:            print("\n\n👋 Программа прервана. До свидания!")

            stack.append(node['left'])            break

            except Exception as e:

    return result            print(f"❌ Произошла ошибка: {e}")





def dfs_postorder_iterative(root):if __name__ == "__main__":

    """Обратный обход (итеративный) - используем два СТЕКА"""    main()

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


# ============== ПОИСК В ШИРИНУ (BFS) ==============

def bfs_iterative(root):
    """Поиск в ширину (итеративный) - используем ОЧЕРЕДЬ"""
    if root is None:
        return []
    
    result = []
    queue = [root]
    
    while queue:
        node = queue.pop(0)  # Берём первый элемент (FIFO)
        result.append(node['value'])
        
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

def display_tree(root, space=0, level=0, side='C'):
    """
    Красивая визуализация дерева как на скриншоте
    """
    if root is None:
        return
    
    # Увеличиваем расстояние для следующего уровня
    space += 5
    
    # Сначала обрабатываем правое поддерево (сверху)
    if root['right']:
        display_tree(root['right'], space, level + 1, 'R')
    
    # Выводим текущий узел
    indent = ' ' * (space - 5)
    if level == 0:
        print(f"\n{indent}   {root['value']}")
    else:
        connector = '/' if side == 'L' else '\\'
        print(f"{indent} {connector}")
        print(f"{indent}{root['value']}")
    
    # Затем обрабатываем левое поддерево (снизу)
    if root['left']:
        display_tree(root['left'], space, level + 1, 'L')


def display_tree_compact(root):
    """Компактное отображение с рамкой"""
    if root is None:
        print("\n" + "="*50)
        print("Дерево пустое")
        print("="*50 + "\n")
        return
    
    print("\n" + "="*50)
    print("ТЕКУЩЕЕ ДЕРЕВО:")
    print("="*50)
    display_tree(root)
    print("\n" + "="*50 + "\n")


def get_tree_info(root):
    """Получить информацию о дереве"""
    if root is None:
        return 0, 0
    
    def count_nodes(node):
        if node is None:
            return 0
        return 1 + count_nodes(node['left']) + count_nodes(node['right'])
    
    def get_height(node):
        if node is None:
            return 0
        return 1 + max(get_height(node['left']), get_height(node['right']))
    
    return count_nodes(root), get_height(root)


# ============== МЕНЮ ==============

def print_menu():
    """Вывод главного меню"""
    print("\n" + "╔" + "="*58 + "╗")
    print("║" + " "*15 + "🌳 ДВОИЧНОЕ ДЕРЕВО ПОИСКА 🌳" + " "*15 + "║")
    print("╚" + "="*58 + "╝")
    print("\n┌─────────────────────────────────────────────────────────┐")
    print("│  ОСНОВНЫЕ ОПЕРАЦИИ:                                     │")
    print("│  1.  Вставить элемент                                   │")
    print("│  2.  Удалить элемент                                    │")
    print("│  3.  Показать дерево                                    │")
    print("├─────────────────────────────────────────────────────────┤")
    print("│  ПОИСК В ГЛУБИНУ (DFS) - РЕКУРСИВНЫЙ:                   │")
    print("│  4.  Симметричный обход (In-order)                      │")
    print("│  5.  Прямой обход (Pre-order)                           │")
    print("│  6.  Обратный обход (Post-order)                        │")
    print("├─────────────────────────────────────────────────────────┤")
    print("│  ПОИСК В ГЛУБИНУ (DFS) - ИТЕРАТИВНЫЙ:                   │")
    print("│  7.  Симметричный обход (In-order)                      │")
    print("│  8.  Прямой обход (Pre-order)                           │")
    print("│  9.  Обратный обход (Post-order)                        │")
    print("├─────────────────────────────────────────────────────────┤")
    print("│  ПОИСК В ШИРИНУ (BFS):                                  │")
    print("│  10. Итеративный (с очередью)                           │")
    print("│  11. Рекурсивный (по уровням)                           │")
    print("├─────────────────────────────────────────────────────────┤")
    print("│  ДОПОЛНИТЕЛЬНО:                                         │")
    print("│  12. Показать все обходы                                │")
    print("│  13. Информация о дереве                                │")
    print("│  14. Очистить дерево                                    │")
    print("│  0.  Выход                                              │")
    print("└─────────────────────────────────────────────────────────┘")


def show_all_traversals(root):
    """Показать все виды обхода"""
    if root is None:
        print("\n⚠️  Дерево пустое!")
        return
    
    print("\n" + "╔" + "="*58 + "╗")
    print("║" + " "*18 + "ВСЕ ВИДЫ ОБХОДА ДЕРЕВА" + " "*18 + "║")
    print("╚" + "="*58 + "╝\n")
    
    print("┌─ ПОИСК В ГЛУБИНУ (DFS) - Рекурсивный ──────────────────┐")
    print("│ Симметричный (In-order):  ", dfs_inorder_recursive(root))
    print("│ Прямой (Pre-order):       ", dfs_preorder_recursive(root))
    print("│ Обратный (Post-order):    ", dfs_postorder_recursive(root))
    print("└─────────────────────────────────────────────────────────┘\n")
    
    print("┌─ ПОИСК В ГЛУБИНУ (DFS) - Итеративный ──────────────────┐")
    print("│ Симметричный (In-order):  ", dfs_inorder_iterative(root))
    print("│ Прямой (Pre-order):       ", dfs_preorder_iterative(root))
    print("│ Обратный (Post-order):    ", dfs_postorder_iterative(root))
    print("└─────────────────────────────────────────────────────────┘\n")
    
    print("┌─ ПОИСК В ШИРИНУ (BFS) ──────────────────────────────────┐")
    print("│ Итеративный (очередь):    ", bfs_iterative(root))
    print("│ Рекурсивный (уровни):     ", bfs_recursive(root))
    print("└─────────────────────────────────────────────────────────┘")


def show_tree_info(root):
    """Показать информацию о дереве"""
    if root is None:
        print("\n⚠️  Дерево пустое!")
        return
    
    nodes, height = get_tree_info(root)
    
    print("\n" + "╔" + "="*58 + "╗")
    print("║" + " "*19 + "ИНФОРМАЦИЯ О ДЕРЕВЕ" + " "*20 + "║")
    print("╚" + "="*58 + "╝\n")
    
    print(f"📊 Количество узлов:  {nodes}")
    print(f"📏 Высота дерева:     {height}")
    print(f"🌲 Корень дерева:     {root['value']}")
    
    # Минимум и максимум
    min_node = find_min(root)
    
    def find_max(node):
        current = node
        while current['right'] is not None:
            current = current['right']
        return current
    
    max_node = find_max(root)
    
    print(f"⬇️  Минимальный элемент: {min_node['value']}")
    print(f"⬆️  Максимальный элемент: {max_node['value']}")
    print(f"\n💡 Отсортированный вид: {dfs_inorder_recursive(root)}")


# ============== ГЛАВНАЯ ПРОГРАММА ==============

def main():
    """Главная функция с интерактивным меню"""
    tree = None
    
    print("\n" + "🌟"*30)
    print("  Добро пожаловать в интерактивное двоичное дерево поиска!")
    print("🌟"*30)
    
    # Предлагаем создать начальное дерево
    print("\n💡 Хотите создать дерево с начальными значениями?")
    choice = input("Введите 'да' для создания примера или Enter для пустого дерева: ").strip().lower()
    
    if choice in ['да', 'yes', 'y', 'д']:
        initial_values = [50, 30, 70, 20, 40, 60, 80]
        for val in initial_values:
            tree = insert(tree, val)
        print(f"\n✅ Создано дерево со значениями: {initial_values}")
        display_tree_compact(tree)
    
    while True:
        print_menu()
        
        try:
            choice = input("\n➤ Выберите действие (0-14): ").strip()
            
            if choice == '1':
                # Вставка
                display_tree_compact(tree)
                value = input("Введите значение для вставки: ").strip()
                try:
                    value = int(value)
                    tree = insert(tree, value)
                    print(f"\n✅ Элемент {value} добавлен!")
                    display_tree_compact(tree)
                except ValueError:
                    print("❌ Ошибка: введите целое число!")
            
            elif choice == '2':
                # Удаление
                display_tree_compact(tree)
                if tree is None:
                    print("\n⚠️  Дерево пустое!")
                    continue
                    
                value = input("Введите значение для удаления: ").strip()
                try:
                    value = int(value)
                    tree, deleted = delete(tree, value)
                    if deleted:
                        print(f"\n✅ Элемент {value} удалён!")
                        display_tree_compact(tree)
                    else:
                        print(f"\n❌ Элемент {value} не найден в дереве!")
                except ValueError:
                    print("❌ Ошибка: введите целое число!")
            
            elif choice == '3':
                # Показать дерево
                display_tree_compact(tree)
            
            elif choice == '4':
                # DFS In-order (рекурсивный)
                result = dfs_inorder_recursive(tree)
                print(f"\n🔍 Симметричный обход (рекурсивный): {result}")
                print("   Порядок: ЛЕВЫЙ → КОРЕНЬ → ПРАВЫЙ")
                print("   Результат отсортирован ✓")
            
            elif choice == '5':
                # DFS Pre-order (рекурсивный)
                result = dfs_preorder_recursive(tree)
                print(f"\n🔍 Прямой обход (рекурсивный): {result}")
                print("   Порядок: КОРЕНЬ → ЛЕВЫЙ → ПРАВЫЙ")
            
            elif choice == '6':
                # DFS Post-order (рекурсивный)
                result = dfs_postorder_recursive(tree)
                print(f"\n🔍 Обратный обход (рекурсивный): {result}")
                print("   Порядок: ЛЕВЫЙ → ПРАВЫЙ → КОРЕНЬ")
            
            elif choice == '7':
                # DFS In-order (итеративный)
                result = dfs_inorder_iterative(tree)
                print(f"\n🔍 Симметричный обход (итеративный - СТЕК): {result}")
                print("   Порядок: ЛЕВЫЙ → КОРЕНЬ → ПРАВЫЙ")
            
            elif choice == '8':
                # DFS Pre-order (итеративный)
                result = dfs_preorder_iterative(tree)
                print(f"\n🔍 Прямой обход (итеративный - СТЕК): {result}")
                print("   Порядок: КОРЕНЬ → ЛЕВЫЙ → ПРАВЫЙ")
            
            elif choice == '9':
                # DFS Post-order (итеративный)
                result = dfs_postorder_iterative(tree)
                print(f"\n🔍 Обратный обход (итеративный - 2 СТЕКА): {result}")
                print("   Порядок: ЛЕВЫЙ → ПРАВЫЙ → КОРЕНЬ")
            
            elif choice == '10':
                # BFS (итеративный)
                result = bfs_iterative(tree)
                print(f"\n🔍 Поиск в ширину (итеративный - ОЧЕРЕДЬ): {result}")
                print("   Обход по уровням (level-order)")
            
            elif choice == '11':
                # BFS (рекурсивный)
                result = bfs_recursive(tree)
                print(f"\n🔍 Поиск в ширину (рекурсивный): {result}")
                print("   Обход по уровням (level-order)")
            
            elif choice == '12':
                # Показать все обходы
                show_all_traversals(tree)
            
            elif choice == '13':
                # Информация о дереве
                show_tree_info(tree)
            
            elif choice == '14':
                # Очистить дерево
                confirm = input("\n⚠️  Вы уверены? (да/нет): ").strip().lower()
                if confirm in ['да', 'yes', 'y', 'д']:
                    tree = None
                    print("\n✅ Дерево очищено!")
                    display_tree_compact(tree)
            
            elif choice == '0':
                # Выход
                print("\n" + "🌟"*30)
                print("  Спасибо за использование программы! До свидания! 👋")
                print("🌟"*30 + "\n")
                break
            
            else:
                print("\n❌ Неверный выбор! Попробуйте снова.")
        
        except KeyboardInterrupt:
            print("\n\n⚠️  Программа прервана пользователем.")
            print("До свидания! 👋\n")
            break
        except Exception as e:
            print(f"\n❌ Произошла ошибка: {e}")


if __name__ == "__main__":
    main()
