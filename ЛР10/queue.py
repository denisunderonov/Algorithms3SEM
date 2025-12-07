# -*- coding: utf-8 -*-
"""
ЛР10: ОЧЕРЕДЬ (QUEUE)
Задание 10: Проверка парных скобок в строке с использованием очереди
"""


class Queue:
    """Класс очереди (FIFO)"""
    def __init__(self):
        self.items = []
    
    def enqueue(self, item):
        """Добавить в конец"""
        self.items.append(item)
    
    def dequeue(self):
        """Извлечь из начала"""
        if not self.is_empty():
            return self.items.pop(0)
        return None
    
    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)
    
    def __repr__(self):
        return str(self.items)


class Stack:
    """Класс стека (LIFO)"""
    def __init__(self):
        self.items = []
    
    def push(self, item):
        """Добавить на вершину"""
        self.items.append(item)
    
    def pop(self):
        """Извлечь с вершины"""
        if not self.is_empty():
            return self.items.pop()
        return None
    
    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)
    
    def __repr__(self):
        return str(self.items)


def check_brackets(string):
    """
    Проверка парных скобок:
    - ОЧЕРЕДЬ читает символы строки последовательно (FIFO)
    - СТЕК хранит открывающие скобки для проверки пар (LIFO)
    """
    brackets_map = {')': '(', ']': '[', '}': '{'}
    
    # Создаём очередь и стек
    queue = Queue()  # Для последовательного чтения символов
    stack = Stack()  # Для хранения открывающих скобок
    
    # Загружаем все символы в очередь
    for char in string:
        queue.enqueue(char)
    
    print(f"\nСтрока: {string}")
    print(f"Очередь: {queue}\n")
    
    # Обрабатываем очередь символов
    step = 0
    while not queue.is_empty():
        step += 1
        char = queue.dequeue()  # Извлекаем из начала очереди (FIFO)
        
        print(f"Шаг {step}: извлекли '{char}' из очереди")
        print(f"  Очередь: {queue if not queue.is_empty() else '[]'}")
        
        # Если открывающая скобка - кладём в стек
        if char in '([{':
            stack.push(char)
            print(f"  Открывающая -> в стек: {stack}\n")
        
        # Если закрывающая скобка - проверяем со стеком
        elif char in ')]}':
            if stack.is_empty():
                print(f"  Ошибка: стек пуст, нет пары для '{char}'\n")
                return False
            
            opening = stack.pop()
            expected = brackets_map[char]
            
            print(f"  Закрывающая -> проверяем со стеком")
            print(f"  Извлекли из стека: '{opening}'")
            print(f"  Стек: {stack if not stack.is_empty() else '[]'}")
            
            if opening != expected:
                print(f"  Ошибка: '{opening}' != '{expected}'\n")
                return False
            
            print(f"  Пара найдена: '{opening}' и '{char}'\n")
        
        else:
            print(f"  Не скобка, пропускаем\n")
    
    # Проверяем, остались ли незакрытые скобки
    print(f"Финальный стек: {stack if not stack.is_empty() else '[]'}")
    
    if not stack.is_empty():
        print("Ошибка: остались незакрытые скобки")
        return False
    
    print("Все скобки корректны!")
    return True


def main():
    string = input("Введите строку: ")
    check_brackets(string)


if __name__ == "__main__":
    main()
