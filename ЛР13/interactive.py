# ИНТЕРАКТИВНАЯ ПРОГРАММА ДЛЯ РАБОТЫ С ДВОИЧНЫМ ДЕРЕВОМ
# Здесь вы можете сами вставлять/удалять элементы

from binary_tree import *

def print_menu():
    """Показать меню"""
    print("\n" + "="*50)
    print("🌳 МЕНЮ ДВОИЧНОГО ДЕРЕВА")
    print("="*50)
    print("1. Вставить элемент")
    print("2. Удалить элемент")
    print("3. Показать дерево")
    print("4. DFS - Симметричный обход (in-order)")
    print("5. DFS - Прямой обход (pre-order)")
    print("6. DFS - Обратный обход (post-order)")
    print("7. BFS - Поиск в ширину")
    print("8. Показать все обходы")
    print("9. Создать дерево из списка")
    print("0. Выход")
    print("="*50)


def show_all_traversals(tree):
    """Показать все виды обходов"""
    if tree is None:
        print("❌ Дерево пустое!")
        return
    
    print("\n" + "="*50)
    print("📊 ВСЕ ВИДЫ ОБХОДОВ")
    print("="*50)
    
    print("\n🔄 ПОИСК В ГЛУБИНУ (DFS) - Рекурсивный:")
    print("├─ Симметричный (In-order):  ", dfs_inorder_recursive(tree))
    print("├─ Прямой (Pre-order):       ", dfs_preorder_recursive(tree))
    print("└─ Обратный (Post-order):    ", dfs_postorder_recursive(tree))
    
    print("\n🔄 ПОИСК В ГЛУБИНУ (DFS) - Итеративный:")
    print("├─ Симметричный (In-order):  ", dfs_inorder_iterative(tree))
    print("├─ Прямой (Pre-order):       ", dfs_preorder_iterative(tree))
    print("└─ Обратный (Post-order):    ", dfs_postorder_iterative(tree))
    
    print("\n🌊 ПОИСК В ШИРИНУ (BFS):")
    print("├─ Итеративный:              ", bfs_iterative(tree))
    print("└─ Рекурсивный:              ", bfs_recursive(tree))
    print("="*50)


def main():
    """Главная функция"""
    tree = None
    
    print("\n🌳 ИНТЕРАКТИВНАЯ ПРОГРАММА - ДВОИЧНОЕ ДЕРЕВО 🌳")
    print("\nДобро пожаловать! Сейчас дерево пустое.")
    print("Начните с добавления элементов (пункт 1) или создайте дерево из списка (пункт 9)")
    
    while True:
        print_menu()
        
        try:
            choice = input("\n👉 Выберите действие (0-9): ").strip()
            
            if choice == '0':
                print("\n👋 До свидания!")
                break
            
            elif choice == '1':
                # Вставка
                value = int(input("Введите число для вставки: "))
                tree = insert(tree, value)
                print(f"✅ Элемент {value} добавлен!")
                display_tree_compact(tree)
            
            elif choice == '2':
                # Удаление
                if tree is None:
                    print("❌ Дерево пустое! Сначала добавьте элементы.")
                    continue
                
                value = int(input("Введите число для удаления: "))
                tree = delete(tree, value)
                display_tree_compact(tree)
            
            elif choice == '3':
                # Показать дерево
                if tree is None:
                    print("❌ Дерево пустое!")
                else:
                    display_tree_compact(tree)
            
            elif choice == '4':
                # Симметричный обход
                if tree is None:
                    print("❌ Дерево пустое!")
                else:
                    print("\n🔄 Симметричный обход (In-order):")
                    print("Рекурсивный:  ", dfs_inorder_recursive(tree))
                    print("Итеративный:  ", dfs_inorder_iterative(tree))
            
            elif choice == '5':
                # Прямой обход
                if tree is None:
                    print("❌ Дерево пустое!")
                else:
                    print("\n🔄 Прямой обход (Pre-order):")
                    print("Рекурсивный:  ", dfs_preorder_recursive(tree))
                    print("Итеративный:  ", dfs_preorder_iterative(tree))
            
            elif choice == '6':
                # Обратный обход
                if tree is None:
                    print("❌ Дерево пустое!")
                else:
                    print("\n🔄 Обратный обход (Post-order):")
                    print("Рекурсивный:  ", dfs_postorder_recursive(tree))
                    print("Итеративный:  ", dfs_postorder_iterative(tree))
            
            elif choice == '7':
                # Поиск в ширину
                if tree is None:
                    print("❌ Дерево пустое!")
                else:
                    print("\n🌊 Поиск в ширину (BFS):")
                    print("Итеративный:  ", bfs_iterative(tree))
                    print("Рекурсивный:  ", bfs_recursive(tree))
            
            elif choice == '8':
                # Все обходы
                show_all_traversals(tree)
            
            elif choice == '9':
                # Создать дерево из списка
                print("\nВведите числа через пробел (например: 50 30 70 20 40 60 80)")
                numbers = input("👉 Числа: ").strip().split()
                
                tree = None  # Очищаем дерево
                for num in numbers:
                    tree = insert(tree, int(num))
                
                print(f"\n✅ Создано дерево из {len(numbers)} элементов!")
                display_tree_compact(tree)
            
            else:
                print("❌ Неверный выбор! Попробуйте ещё раз.")
        
        except ValueError:
            print("❌ Ошибка! Введите корректное число.")
        except KeyboardInterrupt:
            print("\n\n👋 Программа прервана. До свидания!")
            break
        except Exception as e:
            print(f"❌ Произошла ошибка: {e}")


if __name__ == "__main__":
    main()
