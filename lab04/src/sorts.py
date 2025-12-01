"""
Алгоритмы сортировки: Bubble, Selection, Insertion, Merge, Quick.
"""

def bubble_sort(arr):
    """
    Сортировка пузырьком
    Лучший случай:    O(n)        — массив уже отсортирован
    Худший случай:    O(n^2)
    Память: O(1)
    """
    a = arr[:]       # O(n) — копирование массива
    n = len(a)       # O(1)

    for i in range(n):                 # O(n)
        swapped = False                # O(1)
        for j in range(0, n - i - 1):  # O(n)
            if a[j] > a[j + 1]:        # O(1)
                a[j], a[j + 1] = a[j + 1], a[j]  # O(1)
                swapped = True
        if not swapped:                # O(1)
            break
    return a
    # Итоговая сложность: O(n^2)


def selection_sort(arr):
    """
    Сортировка выбором
    Лучший случай:    O(n^2)
    Худший случай:    O(n^2)
    Память: O(1)
    """
    a = arr[:]       # O(n)
    n = len(a)       # O(1)

    for i in range(n):                 # O(n)
        min_index = i                  # O(1)
        for j in range(i + 1, n):      # O(n)
            if a[j] < a[min_index]:    # O(1)
                min_index = j          # O(1)
        a[i], a[min_index] = a[min_index], a[i]  # O(1)
    return a
    # Итоговая сложность: O(n^2)



def insertion_sort(arr):
    """
    Сортировка вставками
    Лучший случай:    O(n)      — массив уже отсортирован
    Худший случай:    O(n^2)
    Память: O(1)
    """
    a = arr[:]          # O(n)

    for i in range(1, len(a)):     # O(n)
        key = a[i]                 # O(1)
        j = i - 1                  # O(1)

        while j >= 0 and a[j] > key:  # O(n)
            a[j + 1] = a[j]        # O(1)
            j -= 1                 # O(1)

        a[j + 1] = key             # O(1)

    return a
    # Итоговая сложность: O(n^2)


def merge_sort(arr):
    """
    Сортировка слиянием
    Лучший случай:    O(n log n)
    Худший случай:    O(n log n)
    Память: O(n)
    """
    if len(arr) <= 1:  # O(1)
        return arr

    mid = len(arr) // 2               # O(1)
    left = merge_sort(arr[:mid])      # O(n/2 log n)
    right = merge_sort(arr[mid:])     # O(n/2 log n)

    return merge(left, right)         # O(n)
    # Итоговая сложность: O(n log n)


def merge(left, right):
    result = []                       # O(1)
    i = j = 0                         # O(1)

    while i < len(left) and j < len(right):   # O(n)
        if left[i] < right[j]:                # O(1)
            result.append(left[i])            # O(1)
            i += 1                            # O(1)
        else:
            result.append(right[j])           # O(1)
            j += 1                            # O(1)

    result.extend(left[i:])          # O(k)
    result.extend(right[j:])         # O(m)

    return result
    # Итоговая сложность: O(n)


def quick_sort(arr):
    """
    Быстрая сортировка (Quick Sort)
    Лучший случай:    O(n log n)
    Худший случай:    O(n^2) — массив отсортирован
    Память: O(log n) — стек рекурсии
    """
    if len(arr) <= 1:      # O(1)
        return arr

    pivot = arr[len(arr) // 2]    # O(1)

    left = [x for x in arr if x < pivot]      # O(n)
    middle = [x for x in arr if x == pivot]   # O(n)
    right = [x for x in arr if x > pivot]     # O(n)

    return quick_sort(left) + middle + quick_sort(right)  # рекурсивные вызовы
    # Итоговая сложность: O(n log n) в среднем