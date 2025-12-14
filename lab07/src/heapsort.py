from heap import MinHeap, MaxHeap
"""
Реализация алгоритма сортировки кучей (Heapsort)
"""

def heap_sort(array, ascending=True):
    """
    Сортировка кучей с использованием дополнительной памяти
    
    Args:
        array: список для сортировки
        ascending: True для сортировки по возрастанию, False для убывания
    
    Returns:
        Отсортированный список
    
    Сложность: O(n log n)
    """
    if ascending:
        heap = MinHeap(array)
    else:
        heap = MaxHeap(array)
    
    sorted_array = []
    while heap.size() > 0:
        sorted_array.append(heap.extract())
    
    return sorted_array


def heap_sort_inplace(array, ascending=True):
    """
    In-place сортировка кучей (без дополнительной памяти)
    
    Args:
        array: список для сортировки (изменяется на месте)
        ascending: True для сортировки по возрастанию, False для убывания
    
    Returns:
        Отсортированный список (исходный массив изменен)
    
    Сложность: O(n log n)
    Память: O(1)
    """
    n = len(array)
    
    def _sift_down(arr, start, end, is_max_heap=False):
        """
        Вспомогательная функция для погружения элемента
        """
        root = start
        
        while True:
            child = 2 * root + 1  # Левый потомок
            
            if child > end:
                break
            
            # Выбираем наибольшего/наименьшего потомка
            if child + 1 <= end:
                if is_max_heap:
                    if arr[child] < arr[child + 1]:
                        child += 1
                else:
                    if arr[child] > arr[child + 1]:
                        child += 1
            
            # Проверяем, нужно ли менять местами
            swap_needed = False
            if is_max_heap:
                swap_needed = arr[root] < arr[child]
            else:
                swap_needed = arr[root] > arr[child]
            
            if swap_needed:
                arr[root], arr[child] = arr[child], arr[root]
                root = child
            else:
                break
    
    # 1. Построение кучи из массива
    # Для сортировки по возрастанию строим max-heap
    # Для сортировки по убыванию строим min-heap
    is_max_heap = ascending
    
    # Начинаем с последнего нелистового узла
    start = n // 2 - 1
    
    for i in range(start, -1, -1):
        _sift_down(array, i, n - 1, is_max_heap)
    
    # 2. Сортировка
    for end in range(n - 1, 0, -1):
        # Меняем корень (макс/мин элемент) с последним элементом
        array[0], array[end] = array[end], array[0]
        # Восстанавливаем свойство кучи для уменьшенной кучи
        _sift_down(array, 0, end - 1, is_max_heap)
    
    return array


def heap_sort_simple(array):
    """
    Простая реализация heapsort для сортировки по возрастанию
    """
    return heap_sort_inplace(array, ascending=True)