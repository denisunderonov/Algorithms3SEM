# -*- coding: utf-8 -*-
"""
ИНТЕРАКТИВНОЕ ДВОИЧНОЕ ДЕРЕВО ПОИСКА
Программа позволяет работать с деревом через удобное меню
Все функции импортируются из binary_tree.py
"""
from binary_tree import *

def print_main_menu():
    """
    Просто выводим красивое меню с рамочкой
    Перечисляем все доступные операции
    """
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
    print("│  0.  Выход                                              │")
    print("└─────────────────────────────────────────────────────────┘")

def show_all_methods(tree):
    """
    Показываем все возможные способы обхода дерева сразу
    Удобно для сравнения результатов разных методов
    """
    if tree is None:
        print("\n⚠️  Дерево пустое!")
        return
    
    print("\n" + "="*60)
    print("ВСЕ ВИДЫ ОБХОДА:")
    print("="*60)
    
    # Показываем DFS рекурсивные методы
    print("\nDFS РЕКУРСИВНЫЙ:")
    print("  In-order (симметричный):  ", dfs_inorder_recursive(tree))
    print("  Pre-order (прямой):       ", dfs_preorder_recursive(tree))
    print("  Post-order (обратный):    ", dfs_postorder_recursive(tree))
    
    # Показываем DFS итеративные методы (без рекурсии)
    print("\nDFS ИТЕРАТИВНЫЙ:")
    print("  In-order (симметричный):  ", dfs_inorder_iterative(tree))
    print("  Pre-order (прямой):       ", dfs_preorder_iterative(tree))
    print("  Post-order (обратный):    ", dfs_postorder_iterative(tree))
    
    # Показываем BFS методы (обход по уровням)
    print("\nBFS:")
    print("  Итеративный:              ", bfs_iterative(tree))
    print("  Рекурсивный:              ", bfs_recursive(tree))
    print("="*60)

def main():
    """
    Главная функция программы - тут весь основной цикл
    """
    tree = None  # Начинаем с пустого дерева
    
    # Приветствие
    print("\n" + "🌟"*30)
    print("  Интерактивное двоичное дерево поиска")
    print("🌟"*30)
    
    # Предлагаем создать дерево с готовыми значениями для примера
    choice = input("\nСоздать дерево с начальными значениями [50,30,70,20,40,60,80]? (да/нет): ").lower()
    if choice in ['да', 'yes', 'y', 'д']:
        # Вставляем готовые значения
        for val in [50, 30, 70, 20, 40, 60, 80]:
            tree = insert(tree, val)
        print("\n✅ Дерево создано!")
        display_tree_compact(tree)
    
    # Основной цикл программы
    while True:
        print_main_menu()
        choice = input("\n➤ Выберите действие: ").strip()
        
        try:
            # ВСТАВКА ЭЛЕМЕНТА
            if choice == '1':
                display_tree_compact(tree)  # Показываем текущее состояние
                val = int(input("Введите значение: "))
                tree = insert(tree, val)    # Вставляем новый элемент
                print(f"\n✅ Добавлено: {val}")
                display_tree_compact(tree)  # Показываем как изменилось дерево
            
            # УДАЛЕНИЕ ЭЛЕМЕНТА
            elif choice == '2':
                if tree is None:
                    print("\n⚠️  Дерево пустое!")
                    continue
                display_tree_compact(tree)
                val = int(input("Введите значение для удаления: "))
                tree = delete(tree, val)    # Удаляем элемент
                print(f"\n✅ Удалено: {val}")
                display_tree_compact(tree)  # Показываем результат
            
            # ПРОСТО ПОКАЗАТЬ ДЕРЕВО
            elif choice == '3':
                display_tree_compact(tree)
            
            # DFS - РЕКУРСИВНЫЕ ОБХОДЫ
            elif choice == '4':
                # Симметричный - даёт отсортированный список!
                print(f"\n🔍 In-order (рекурсивный): {dfs_inorder_recursive(tree)}")
                print("   Порядок: ЛЕВЫЙ → КОРЕНЬ → ПРАВЫЙ (отсортирован!)")
            
            elif choice == '5':
                # Прямой - сначала корень, потом дети
                print(f"\n🔍 Pre-order (рекурсивный): {dfs_preorder_recursive(tree)}")
                print("   Порядок: КОРЕНЬ → ЛЕВЫЙ → ПРАВЫЙ")
            
            elif choice == '6':
                # Обратный - сначала дети, потом корень
                print(f"\n🔍 Post-order (рекурсивный): {dfs_postorder_recursive(tree)}")
                print("   Порядок: ЛЕВЫЙ → ПРАВЫЙ → КОРЕНЬ")
            
            # DFS - ИТЕРАТИВНЫЕ ОБХОДЫ (без рекурсии, используем стек)
            elif choice == '7':
                # Симметричный через стек
                print(f"\n🔍 In-order (итеративный, СТЕК): {dfs_inorder_iterative(tree)}")
            
            elif choice == '8':
                # Прямой через стек
                print(f"\n🔍 Pre-order (итеративный, СТЕК): {dfs_preorder_iterative(tree)}")
            
            elif choice == '9':
                # Обратный через два стека
                print(f"\n🔍 Post-order (итеративный, 2 СТЕКА): {dfs_postorder_iterative(tree)}")
            
            # BFS - ОБХОДЫ В ШИРИНУ (по уровням)
            elif choice == '10':
                # Итеративный BFS - используем очередь
                print(f"\n🔍 BFS (итеративный, ОЧЕРЕДЬ): {bfs_iterative(tree)}")
                print("   Обход по уровням")
            
            elif choice == '11':
                # Рекурсивный BFS - обрабатываем целый уровень за раз
                print(f"\n🔍 BFS (рекурсивный): {bfs_recursive(tree)}")
                print("   Обход по уровням")
            
            # ПОКАЗАТЬ ВСЕ ОБХОДЫ СРАЗУ
            elif choice == '12':
                show_all_methods(tree)
            
            # ВЫХОД ИЗ ПРОГРАММЫ
            elif choice == '0':
                print("\n👋 До свидания!\n")
                break
            
            # ЕСЛИ ВВЕЛИ ЧТО-ТО НЕПРАВИЛЬНОЕ
            else:
                print("\n❌ Неверный выбор!")
        
        # ОБРАБОТКА ОШИБОК
        except ValueError:
            # Если ввели не число
            print("\n❌ Ошибка: введите число!")
        except KeyboardInterrupt:
            # Если нажали Ctrl+C
            print("\n\n👋 Программа прервана. До свидания!\n")
            break

# Запускаем программу, если файл запущен напрямую (не импортирован)
if __name__ == "__main__":
    main()
