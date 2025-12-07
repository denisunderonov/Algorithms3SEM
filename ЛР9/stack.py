
def check_brackets_stack(string):
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}
    
    for char in string:
        if char in '([{':
            stack.append(char)
        elif char in ')]}':
            if not stack:
                return False
            last = stack.pop()
            if last != pairs[char]:
                return False
    return len(stack) == 0


def check_brackets_queue(string):
    queue = [] 
    pairs = {'(': ')', '[': ']', '{': '}'}
    
    for char in string:
        if char in '([{':
            queue.append(char)
        elif char in ')]}':
            if not queue:
                return False
            first = queue.pop(0)
            if pairs[first] != char:
                return False
    return len(queue) == 0

if __name__ == "__main__":
    test_cases = [
        "()",           # Простая пара
        "()[]{}",       # Несколько пар подряд
        "([{}])",       # Вложенные скобки
        "({[]})",       # Сложная вложенность
        "((()))",       # Много одинаковых
        "(()",          # НЕ хватает закрывающей
        "())",          # Лишняя закрывающая
        "([)]",         # Неправильный порядок (важный тест!)
        "{[}]",
        "((([[{{}}]])))[]"# Неправильная вложенность
    ]
    
    print("=" * 60)
    print("СРАВНЕНИЕ: СТЕК vs ОЧЕРЕДЬ для проверки скобок")
    print("=" * 60)
    print(f"{'Строка':<15} {'Стек (LIFO)':<15} {'Очередь (FIFO)':<15}")
    print("-" * 60)
    
    for test in test_cases:
        stack_result = check_brackets_stack(test)
        queue_result = check_brackets_queue(test)
        
        stack_str = "✓ Верно" if stack_result else "✗ Неверно"
        queue_str = "✓ Верно" if queue_result else "✗ Неверно"
        
        print(f"{test:<15} {stack_str:<15} {queue_str:<15}")