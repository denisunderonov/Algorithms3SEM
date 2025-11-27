def create_node(data):
    """Создать узел (элемент списка)"""
    return {'data': data, 'next': None, 'prev': None}


def create_list():
    return {'head': None, 'last': None}


def insert_at_end(dll, value):
    new_node = create_node(value)

    if dll['head'] is None:
        dll['head'] = new_node
        dll['last'] = new_node
    else:
        # Добавляем в конец через указатель last
        dll['last']['next'] = new_node
        new_node['prev'] = dll['last']
        dll['last'] = new_node  # Обновляем хвост!
    
    return dll


def insert_at_beginning(dll, value):
    """Вставка элемента в начало"""
    new_node = create_node(value)
    
    # Если список пустой
    if dll['head'] is None:
        dll['head'] = new_node
        dll['last'] = new_node
    else:
        new_node['next'] = dll['head']
        dll['head']['prev'] = new_node
        dll['head'] = new_node  # Обновляем голову!
    
    return dll


def insert_at_index(dll, index, value):
    """Вставка элемента по индексу"""
    new_node = create_node(value)
    
    if index == 0:
        return insert_at_beginning(dll, value)
    
    current = dll['head']
    position = 0
    
    while current is not None and position < index - 1:
        current = current['next']
        position += 1
    
    if current is None:
        print("Индекс вне диапазона!")
        return dll
    
    new_node['next'] = current['next']
    new_node['prev'] = current
    
    if current['next'] is not None:
        current['next']['prev'] = new_node
    else:
        # Если вставляем в конец, обновляем last
        dll['last'] = new_node
    
    current['next'] = new_node
    return dll


def delete_by_value(dll, value):
    """Удаление ВСЕХ элементов по значению"""
    if dll['head'] is None:
        print("Список пуст!")
        return dll
    
    current = dll['head']
    deleted_count = 0
    
    while current is not None:
        next_node = current['next']  # Сохраняем следующий узел
        
        if current['data'] == value:
            # Если это голова списка
            if current['prev'] is None:
                dll['head'] = current['next']
                if dll['head'] is not None:
                    dll['head']['prev'] = None
                else:
                    # Список стал пустым
                    dll['last'] = None
            # Если это хвост списка
            elif current['next'] is None:
                dll['last'] = current['prev']
                dll['last']['next'] = None
            # Элемент в середине
            else:
                current['prev']['next'] = current['next']
                current['next']['prev'] = current['prev']
            
            deleted_count += 1
        
        current = next_node
    
    if deleted_count > 0:
        print(f"Удалено {deleted_count} элемент(ов) со значением '{value}'")
    else:
        print(f"Элемент '{value}' не найден")
    
    return dll


def delete_by_index(dll, index):
    """Удаление элемента по индексу"""
    if dll['head'] is None:
        print("Список пуст!")
        return dll
    
    current = dll['head']
    position = 0
    
    while current is not None and position < index:
        current = current['next']
        position += 1
    
    if current is None:
        print("Индекс вне диапазона!")
        return dll
    
    # Удаляем голову
    if current['prev'] is None:
        dll['head'] = current['next']
        if dll['head'] is not None:
            dll['head']['prev'] = None
        else:
            dll['last'] = None
    # Удаляем хвост
    elif current['next'] is None:
        dll['last'] = current['prev']
        dll['last']['next'] = None
    # Удаляем из середины
    else:
        current['prev']['next'] = current['next']
        current['next']['prev'] = current['prev']
    
    print(f"Элемент с индексом {index} удален")
    return dll


def search_by_value(dll, value):
    """Поиск ВСЕХ элементов по значению"""
    current = dll['head']
    index = 0
    found_indices = []
    
    while current is not None:
        if current['data'] == value:
            found_indices.append(index)
        current = current['next']
        index += 1
    
    if found_indices:
        if len(found_indices) == 1:
            print(f"Элемент '{value}' найден на индексе: {found_indices[0]}")
        else:
            print(f"Элемент '{value}' найден на индексах: {', '.join(map(str, found_indices))}")
        return found_indices
    else:
        print(f"Элемент '{value}' не найден")
        return []


def search_by_index(dll, index):
    """Поиск элемента по индексу"""
    current = dll['head']
    position = 0
    
    while current is not None:
        if position == index:
            print(f"Элемент на индексе {index}: {current['data']}")
            return current['data']
        current = current['next']
        position += 1
    
    print("Индекс вне диапазона!")
    return None


def display(dll):
    """Вывод всех элементов списка (вперед) через указатель head"""
    if dll['head'] is None:
        print("Список пуст")
        return
    
    current = dll['head']
    result = []
    
    while current is not None:
        result.append(current['data'])
        current = current['next']
    
    print("Список (вперед от head):", " <-> ".join(map(str, result)))
    print(f"[Голова (head): {dll['head']['data']}, Хвост (last): {dll['last']['data']}]")


def display_reverse(dll):
    """
    Вывод всех элементов списка (назад) - начинаем с хвоста (last)!
    ПРЕИМУЩЕСТВО: не нужно искать хвост, сразу начинаем с dll['last']
    """
    if dll['head'] is None:
        print("Список пуст")
        return
    
    # Начинаем сразу с хвоста!
    current = dll['last']
    result = []
    
    while current is not None:
        result.append(current['data'])
        current = current['prev']
    
    print("Список (назад от last):", " <-> ".join(map(str, result)))
    print(f"[Голова (head): {dll['head']['data']}, Хвост (last): {dll['last']['data']}]")


def get_list_length(dll):
    """Получить длину списка"""
    count = 0
    current = dll['head']
    while current is not None:
        count += 1
        current = current['next']
    return count


def print_menu():
    """Вывод меню"""
    print("\n" + "="*50)
    print("ДВУСВЯЗНЫЙ СПИСОК")
    print("="*50)
    print("1.  Показать список (вперед)")
    print("2.  Показать список (назад)")
    print("3.  Добавить элемент в конец")
    print("4.  Добавить элемент в начало")
    print("5.  Вставить элемент по индексу")
    print("6.  Удалить элемент по значению")
    print("7.  Удалить элемент по индексу")
    print("8.  Найти элемент по значению")
    print("9.  Найти элемент по индексу")
    print("10. Показать длину списка")
    print("11. Очистить список")
    print("0.  Выход")
    print("="*50)


def main():
    """Главная функция программы"""
    my_list = create_list()
    
    print("\n" + "="*60)
    print("ДВУСВЯЗНЫЙ СПИСОК с явно определенными HEAD и LAST")
    print("="*60)
    print("ОТЛИЧИЕ от односвязного списка:")
    print("✓ Есть указатель на ГОЛОВУ (head) - первый элемент")
    print("✓ Есть указатель на ХВОСТ (last) - последний элемент")
    print("✓ Каждый узел имеет ссылки на ПРЕДЫДУЩИЙ и СЛЕДУЮЩИЙ")
    print("\nПРЕИМУЩЕСТВА:")
    print("• Быстрая вставка в конец - O(1) вместо O(n)")
    print("• Быстрое обратное отображение - начинаем с last")
    print("• Удаление элементов с обоих концов за O(1)")
    print("="*60)
    
    while True:
        print_menu()
        
        try:
            choice = input("\nВыберите действие: ").strip()
            
            if choice == '1':
                # Показать список (вперед)
                display(my_list)
            
            elif choice == '2':
                # Показать список (назад)
                display_reverse(my_list)
            
            elif choice == '3':
                # Добавить в конец
                value = input("Введите значение для добавления: ").strip()
                my_list = insert_at_end(my_list, value)
                print(f"Элемент '{value}' добавлен в конец")
                display(my_list)
            
            elif choice == '4':
                # Добавить в начало
                value = input("Введите значение для добавления: ").strip()
                my_list = insert_at_beginning(my_list, value)
                print(f"Элемент '{value}' добавлен в начало")
                display(my_list)
            
            elif choice == '5':
                # Вставить по индексу
                display(my_list)
                try:
                    index = int(input("Введите индекс (0 - начало): "))
                    value = input("Введите значение: ").strip()
                    my_list = insert_at_index(my_list, index, value)
                    print(f"Элемент '{value}' вставлен на индекс {index}")
                    display(my_list)
                except ValueError:
                    print("Индекс должен быть числом!")
            
            elif choice == '6':
                # Удалить по значению
                display(my_list)
                value = input("Введите значение для удаления: ").strip()
                my_list = delete_by_value(my_list, value)
                display(my_list)
            
            elif choice == '7':
                # Удалить по индексу
                display(my_list)
                try:
                    index = int(input("Введите индекс для удаления: "))
                    my_list = delete_by_index(my_list, index)
                    display(my_list)
                except ValueError:
                    print("Индекс должен быть числом!")
            
            elif choice == '8':
                # Найти по значению
                value = input("Введите значение для поиска: ").strip()
                search_by_value(my_list, value)
            
            elif choice == '9':
                # Найти по индексу
                try:
                    index = int(input("Введите индекс для поиска: "))
                    search_by_index(my_list, index)
                except ValueError:
                    print("Индекс должен быть числом!")
            
            elif choice == '10':
                # Показать длину
                length = get_list_length(my_list)
                print(f"Длина списка: {length}")
            
            elif choice == '11':
                # Очистить список
                confirm = input("Вы уверены? (да/нет): ").strip().lower()
                if confirm in ['да', 'yes', 'y', 'д']:
                    my_list = create_list()
                    print("Список очищен")
                    display(my_list)
            
            elif choice == '0':
                # Выход
                print("\nДо свидания!")
                break
            
            else:
                print("Неверный выбор! Попробуйте снова.")
        
        except KeyboardInterrupt:
            print("\n\nПрограмма прервана. До свидания!")
            break
        except Exception as e:
            print(f"Произошла ошибка: {e}")


if __name__ == "__main__":
    main()
