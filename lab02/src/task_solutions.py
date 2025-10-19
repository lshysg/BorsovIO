from collections import deque


def is_balanced(expr):
    """
    Задача 1: Сбалансированные скобки
    """
    stack = []
    pairs = {'(': ')', '[': ']', '{': '}'}
    for char in expr:
        if char in pairs:
            stack.append(char)
        elif char in pairs.values():
            if not stack or pairs[stack.pop()] != char:
                return False
    return not stack


def print_queue(tasks):
    """
    Задача 2: Очередь печати
    """
    q = deque(tasks)
    while q:
        task = q.popleft()
        print(f"Processing task: {task}")   


def is_palindrome(seq):
    """
    Задача 3: Палиндром
    """
    d = deque(seq)
    while len(d) > 1:
        if d.popleft() != d.pop():
            return False
    return True


if __name__ == "__main__":
    # Тесты
    print("Сбалансированность скобок:")
    print(is_balanced("{[()]}"))  # True
    print(is_balanced("{[(])}"))  # False

    print("\nОчередь печати:")
    print_queue(["task1", "task2", "task3"])

    print("\nПроверка палиндрома:")
    print(is_palindrome("radar"))  # True
    print(is_palindrome("hello"))  # False
