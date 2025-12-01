import os

def binary_search(arr, target, left=0, right=None):
    """
    Рекурсивный бинарный поиск.
    """
    if right is None:          # O(1)
        right = len(arr) - 1   # O(1)

    if left > right:  # O(1)
        return -1     # O(1)

    mid = (left + right) // 2  # O(1)

    if arr[mid] == target:  # O(1)
        return mid          # O(1)
    elif arr[mid] > target:  # O(1)
        return binary_search(arr, target, left, mid - 1)  # O(log n)
    else:
        return binary_search(arr, target, mid + 1, right)  # O(log n)

    # Итоговая сложность: O(log n)
    # Глубина рекурсии: O(log n)

def walk_directory(path, indent=0):
    """
    Рекурсивный вывод дерева каталогов.
    """
    for item in os.listdir(path):  # O(k), k — количество элементов в папке
        full = os.path.join(path, item)  # O(1)
        print(" " * indent + item)       # O(1)

        if os.path.isdir(full):          # O(1)
            walk_directory(full, indent + 4)  # O(h)

    # Итоговая сложность: O(N), где N — все файлы и папки
    # Глубина рекурсии: O(h), h — максимальная вложенность

def hanoi(n, start, end, aux):
    """
    Решение задачи Ханойских башен.
    """
    if n == 1:  # O(1)
        print(f"Перенести диск 1 со стержня {start} на стержень {end}")  # O(1)
        return  # O(1)

    hanoi(n - 1, start, aux, end)  # O(2^(n-1))

    print(f"Перенести диск {n} со стержня {start} на стержень {end}")  # O(1)

    hanoi(n - 1, aux, end, start)  # O(2^(n-1))

    # Итоговая сложность: O(2^n)
    # Глубина рекурсии: O(n)

if __name__ == "__main__":
   
    # 1. Бинарный поиск    
    arr = [1, 3, 5, 7, 9, 11, 15]
    print("binary_search(arr, 7) =", binary_search(arr, 7))   # 3
    print("binary_search(arr, 1) =", binary_search(arr, 1))   # 0
    print("binary_search(arr, 15) =", binary_search(arr, 15)) # 6
    print("binary_search(arr, 100) =", binary_search(arr, 100)) # -1

   
    # 2. Обход файловой системы
    
    print("\nДемонстрация walk_directory (текущая папка):")
    # WARNING: может вывести много текста!
    walk_directory(".")

    
    # 3. Ханойские башни
    
    print("\nХанойские башни для n=3:")
    hanoi(3, 'A', 'C', 'B')