def create_node(data):
    """Создать узел (элемент списка)"""
    return {'data': data, 'next': None}


def create_list():
    """Создать пустой список - просто None (нет головы)"""
    return None


def insert_at_end(head, value):
    """Вставка элемента в конец"""
    new_node = create_node(value)
    
    if head is None:
        return new_node
    
    current = head
    while current['next'] is not None:
        current = current['next']
    
    current['next'] = new_node
    return head


def insert_at_beginning(head, value):
    """Вставка элемента в начало"""
    new_node = create_node(value)
    new_node['next'] = head
    return new_node


def insert_at_index(head, index, value):
    """Вставка элемента по индексу"""
    new_node = create_node(value)
    
    if index == 0:
        new_node['next'] = head
        return new_node
    
    current = head
    position = 0
    
    while current is not None and position < index - 1:
        current = current['next']
        position += 1
    
    if current is None:
        print("Индекс вне диапазона!")
        return head
    
    new_node['next'] = current['next']
    current['next'] = new_node
    return head


def delete_by_value(head, value):
    """Удаление элемента по значению"""
    if head is None:
        print("Список пуст!")
        return head
    
    if head['data'] == value:
        print(f"Элемент {value} удален")
        return head['next']
    
    current = head
    while current['next'] is not None:
        if current['next']['data'] == value:
            current['next'] = current['next']['next']
            print(f"Элемент {value} удален")
            return head
        current = current['next']
    
    print(f"Элемент {value} не найден")
    return head


def delete_by_index(head, index):
    """Удаление элемента по индексу"""
    if head is None:
        print("Список пуст!")
        return head
    
    if index == 0:
        print(f"Элемент с индексом {index} удален")
        return head['next']
    
    current = head
    position = 0
    
    while current['next'] is not None and position < index - 1:
        current = current['next']
        position += 1
    
    if current['next'] is None:
        print("Индекс вне диапазона!")
        return head
    
    current['next'] = current['next']['next']
    print(f"Элемент с индексом {index} удален")
    return head


def search_by_value(head, value):
    """Поиск элемента по значению"""
    current = head
    index = 0
    
    while current is not None:
        if current['data'] == value:
            print(f"Элемент {value} найден на индексе {index}")
            return index
        current = current['next']
        index += 1
    
    print(f"Элемент {value} не найден")
    return -1


def search_by_index(head, index):
    """Поиск элемента по индексу"""
    current = head
    position = 0
    
    while current is not None:
        if position == index:
            print(f"Элемент на индексе {index}: {current['data']}")
            return current['data']
        current = current['next']
        position += 1
    
    print("Индекс вне диапазона!")
    return None


def display(head):
    """Вывод всех элементов списка"""
    if head is None:
        print("Список пуст")
        return
    
    current = head
    result = []
    
    while current is not None:
        result.append(current['data'])
        current = current['next']
    
    print("Список:", " -> ".join(map(str, result)))


def get_list_length(head):
    """Получить длину списка"""
    count = 0
    current = head
    while current is not None:
        count += 1
        current = current['next']
    return count


def print_menu():
    """Вывод меню"""
    print("\n" + "="*50)
    print("ОДНОСВЯЗНЫЙ СПИСОК")
    print("="*50)
    print("1.  Показать список")
    print("2.  Добавить элемент в конец")
    print("3.  Добавить элемент в начало")
    print("4.  Вставить элемент по индексу")
    print("5.  Удалить элемент по значению")
    print("6.  Удалить элемент по индексу")
    print("7.  Найти элемент по значению")
    print("8.  Найти элемент по индексу")
    print("9.  Показать длину списка")
    print("10. Очистить список")
    print("0.  Выход")
    print("="*50)


def main():
    """Главная функция программы"""
    my_list = create_list()
    
    print("\nПрограмма управления односвязным списком")
    
    while True:
        print_menu()
        
        try:
            choice = input("\nВыберите действие: ").strip()
            
            if choice == '1':
                # Показать список
                display(my_list)
            
            elif choice == '2':
                # Добавить в конец
                value = input("Введите значение для добавления: ").strip()
                my_list = insert_at_end(my_list, value)
                print(f"✅ Элемент '{value}' добавлен в конец")
                display(my_list)
            
            elif choice == '3':
                # Добавить в начало
                value = input("Введите значение для добавления: ").strip()
                my_list = insert_at_beginning(my_list, value)
                print(f"Элемент '{value}' добавлен в начало")
                display(my_list)
            
            elif choice == '4':
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
            
            elif choice == '5':
                # Удалить по значению
                display(my_list)
                value = input("Введите значение для удаления: ").strip()
                my_list = delete_by_value(my_list, value)
                display(my_list)
            
            elif choice == '6':
                # Удалить по индексу
                display(my_list)
                try:
                    index = int(input("Введите индекс для удаления: "))
                    my_list = delete_by_index(my_list, index)
                    display(my_list)
                except ValueError:
                    print("Индекс должен быть числом!")
            
            elif choice == '7':
                # Найти по значению
                value = input("Введите значение для поиска: ").strip()
                search_by_value(my_list, value)
            
            elif choice == '8':
                # Найти по индексу
                try:
                    index = int(input("Введите индекс для поиска: "))
                    search_by_index(my_list, index)
                except ValueError:
                    print("Индекс должен быть числом!")
            
            elif choice == '9':
                # Показать длину
                length = get_list_length(my_list)
                print(f"Длина списка: {length}")
            
            elif choice == '10':
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
