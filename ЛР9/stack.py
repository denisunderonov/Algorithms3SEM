def check_brackets_stack(s):
    stack = []
    
    for char in s:
        if char in '({[':
            stack.append(char)  # Кладем открывающую скобку в стек
        elif char in ')}]':
            if not stack:  # Если стек пуст - ошибка
                return False
            last = stack.pop()  # Берем последнюю открывающую скобку
            
            # Проверяем соответствие
            if (last == '(' and char != ')') or \
               (last == '{' and char != '}') or \
               (last == '[' and char != ']'):
                return False
    
    return len(stack) == 0  # Стек должен быть пустым

tests = [
    "(a + b)",        
    "(a + b))",      
    "((a + b)",       
    "({[]})",         
    "({[)}]"         
]

for test in tests:
    result = check_brackets_stack(test)
    print(f"'{test}' -> {'✓ Правильно' if result else '✗ Ошибка'}")