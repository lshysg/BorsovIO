"""
Тестирование и анализ производительности реализации кучи
"""

import time
import random
import numpy as np
import matplotlib.pyplot as plt
import sys
import heapq  # Для сравнения с встроенной реализацией
from heap import MinHeap, MaxHeap
from heapsort import heap_sort, heap_sort_inplace, heap_sort_simple
from priority_queue import PriorityQueue


def test_min_heap_basic():
    """Базовое тестирование MinHeap"""
    print("=" * 60)
    print("ТЕСТИРОВАНИЕ MIN-HEAP")
    print("=" * 60)
    
    heap = MinHeap()
    
    # Тест 1: Вставка элементов
    test_data = [4, 2, 8, 1, 5, 7, 3]
    print(f"Вставляем элементы: {test_data}")
    
    for value in test_data:
        heap.insert(value)
        print(f"После вставки {value}: {heap}")
        assert heap.validate(), "Нарушено свойство min-heap!"
    
    # Тест 2: Извлечение элементов
    print("\nИзвлекаем элементы в порядке возрастания:")
    extracted = []
    while not heap.is_empty():
        value = heap.extract()
        extracted.append(value)
        print(f"Извлечено: {value}, Оставшаяся куча: {heap}")
        if heap.size() > 0:
            assert heap.validate(), "Нарушено свойство min-heap после извлечения!"
    
    print(f"Извлеченные элементы: {extracted}")
    assert extracted == sorted(test_data), "Элементы извлечены не в отсортированном порядке!"
    
    # Тест 3: Построение кучи из массива
    print("\nТест build_heap:")
    array = [9, 3, 7, 1, 4, 6, 8, 2, 5]
    heap.build_heap(array)
    print(f"Массив: {array}")
    print(f"Построенная куча: {heap}")
    assert heap.validate(), "build_heap нарушило свойство кучи!"
    
    # Визуализация дерева
    print("\nВизуализация кучи в виде дерева:")
    heap.print_tree()
    
    print("\n✓ Все тесты MinHeap пройдены успешно!")


def test_max_heap_basic():
    """Базовое тестирование MaxHeap"""
    print("\n" + "=" * 60)
    print("ТЕСТИРОВАНИЕ MAX-HEAP")
    print("=" * 60)
    
    heap = MaxHeap()
    
    # Тест 1: Вставка элементов
    test_data = [4, 2, 8, 1, 5, 7, 3]
    print(f"Вставляем элементы: {test_data}")
    
    for value in test_data:
        heap.insert(value)
        print(f"После вставки {value}: {heap}")
    
    # Тест 2: Извлечение элементов
    print("\nИзвлекаем элементы в порядке убывания:")
    extracted = []
    while not heap.is_empty():
        value = heap.extract()
        extracted.append(value)
        print(f"Извлечено: {value}, Оставшаяся куча: {heap}")
    
    print(f"Извлеченные элементы: {extracted}")
    assert extracted == sorted(test_data, reverse=True), "Элементы извлечены не в правильном порядке!"
    
    print("\n✓ Все тесты MaxHeap пройдены успешно!")


def test_heap_sort():
    """Тестирование сортировки кучей"""
    print("\n" + "=" * 60)
    print("ТЕСТИРОВАНИЕ HEAPSORT")
    print("=" * 60)
    
    # Тестовые данные
    test_arrays = [
        [5, 3, 8, 1, 2],
        [1],
        [],
        [9, 8, 7, 6, 5, 4, 3, 2, 1],
        [1, 2, 3, 4, 5],
        [5, 5, 5, 5, 5],
        random.sample(range(100), 20)
    ]
    
    for i, arr in enumerate(test_arrays, 1):
        print(f"\nТест {i}: Исходный массив: {arr[:10]}..." if len(arr) > 10 else f"\nТест {i}: Исходный массив: {arr}")
        
        # Тестируем все версии heapsort
        arr_copy = arr[:]
        sorted_heap = heap_sort(arr_copy)
        print(f"  heap_sort (asc): {sorted_heap[:10]}..." if len(sorted_heap) > 10 else f"  heap_sort (asc): {sorted_heap}")
        
        arr_copy = arr[:]
        sorted_heap_desc = heap_sort(arr_copy, ascending=False)
        print(f"  heap_sort (desc): {sorted_heap_desc[:10]}..." if len(sorted_heap_desc) > 10 else f"  heap_sort (desc): {sorted_heap_desc}")
        
        arr_copy = arr[:]
        sorted_inplace = heap_sort_inplace(arr_copy[:], ascending=True)
        print(f"  heap_sort_inplace (asc): {sorted_inplace[:10]}..." if len(sorted_inplace) > 10 else f"  heap_sort_inplace (asc): {sorted_inplace}")
        
        # Проверка корректности
        assert sorted_heap == sorted(arr), f"Ошибка в heap_sort! Ожидалось: {sorted(arr)}, получено: {sorted_heap}"
        assert sorted_heap_desc == sorted(arr, reverse=True), f"Ошибка в heap_sort (desc)!"
        assert sorted_inplace == sorted(arr), f"Ошибка в heap_sort_inplace!"
    
    print("\n✓ Все тесты Heapsort пройдены успешно!")


def test_priority_queue():
    """Тестирование приоритетной очереди"""
    print("\n" + "=" * 60)
    print("ТЕСТИРОВАНИЕ ПРИОРИТЕТНОЙ ОЧЕРЕДИ")
    print("=" * 60)
    
    pq = PriorityQueue()
    
    # Добавляем элементы с разными приоритетами
    tasks = [
        ("Почистить зубы", 3),
        ("Позавтракать", 2),
        ("Проверить почту", 4),
        ("Сделать зарядку", 1),
        ("Принять душ", 2),
        ("Собраться на работу", 3)
    ]
    
    print("Добавляем задачи в очередь:")
    for task, priority in tasks:
        pq.enqueue(task, priority)
        print(f"  Добавлено: '{task}' с приоритетом {priority}")
    
    print(f"\nРазмер очереди: {pq.size()}")
    print(f"Первый элемент: {pq.peek()}")
    
    print("\nИзвлекаем задачи в порядке приоритета:")
    while not pq.is_empty():
        task = pq.dequeue()
        print(f"  Выполняем: '{task}'")
    
    print("\n✓ Все тесты PriorityQueue пройдены успешно!")


def performance_comparison():
    """Сравнение производительности разных методов"""
    print("\n" + "=" * 60)
    print("СРАВНЕНИЕ ПРОИЗВОДИТЕЛЬНОСТИ")
    print("=" * 60)
    
    sizes = [100, 500, 1000, 5000, 10000, 20000]
    results_insert = []
    results_build = []
    results_sort = []
    results_sort_inplace = []
    results_sort_builtin = []
    
    for size in sizes:
        print(f"\nРазмер данных: {size}")
        
        # Генерация случайных данных
        data = random.sample(range(size * 10), size)
        
        # 1. Построение кучи последовательной вставкой
        start = time.time()
        heap = MinHeap()
        for value in data:
            heap.insert(value)
        end = time.time()
        time_insert = end - start
        results_insert.append((size, time_insert))
        print(f"  Последовательная вставка: {time_insert:.6f} сек")
        
        # 2. Построение кучи с помощью build_heap
        start = time.time()
        heap2 = MinHeap(data)
        end = time.time()
        time_build = end - start
        results_build.append((size, time_build))
        print(f"  build_heap: {time_build:.6f} сек")
        
        # 3. Сортировка кучей (с дополнительной памятью)
        start = time.time()
        sorted1 = heap_sort(data[:])
        end = time.time()
        time_sort = end - start
        results_sort.append((size, time_sort))
        print(f"  heap_sort: {time_sort:.6f} сек")
        
        # 4. In-place сортировка кучей
        start = time.time()
        sorted2 = heap_sort_inplace(data[:])
        end = time.time()
        time_sort_inplace = end - start
        results_sort_inplace.append((size, time_sort_inplace))
        print(f"  heap_sort_inplace: {time_sort_inplace:.6f} сек")
        
        # 5. Встроенная сортировка Python для сравнения
        start = time.time()
        sorted3 = sorted(data)
        end = time.time()
        time_sort_builtin = end - start
        results_sort_builtin.append((size, time_sort_builtin))
        print(f"  sorted() Python: {time_sort_builtin:.6f} сек")
        
        # Проверка корректности
        assert sorted1 == sorted2 == sorted3, "Ошибка сортировки!"
    
    return {
        'sizes': sizes,
        'insert': results_insert,
        'build': results_build,
        'sort': results_sort,
        'sort_inplace': results_sort_inplace,
        'sort_builtin': results_sort_builtin
    }


def plot_performance(results):
    """Построение графиков производительности"""
    sizes = results['sizes']
    
    # Извлекаем данные для графиков
    insert_times = [t for _, t in results['insert']]
    build_times = [t for _, t in results['build']]
    sort_times = [t for _, t in results['sort']]
    sort_inplace_times = [t for _, t in results['sort_inplace']]
    sort_builtin_times = [t for _, t in results['sort_builtin']]
    
    # График 1: Построение кучи разными методами
    plt.figure(figsize=(12, 10))
    
    plt.subplot(2, 2, 1)
    plt.plot(sizes, insert_times, 'o-', label='Последовательная вставка', linewidth=2)
    plt.plot(sizes, build_times, 's-', label='build_heap', linewidth=2)
    plt.xlabel('Размер данных')
    plt.ylabel('Время (сек)')
    plt.title('Сравнение методов построения кучи')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    # График 2: Сравнение сортировок
    plt.subplot(2, 2, 2)
    plt.plot(sizes, sort_times, 'o-', label='heap_sort', linewidth=2)
    plt.plot(sizes, sort_inplace_times, 's-', label='heap_sort_inplace', linewidth=2)
    plt.plot(sizes, sort_builtin_times, '^-', label='sorted() Python', linewidth=2)
    plt.xlabel('Размер данных')
    plt.ylabel('Время (сек)')
    plt.title('Сравнение алгоритмов сортировки')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    # График 3: Отношение времени build_heap к n log n
    plt.subplot(2, 2, 3)
    # Теоретическая сложность O(n)
    theoretical = [n * 1e-6 for n in sizes]  # Масштабируем для визуализации
    plt.plot(sizes, build_times, 'o-', label='build_heap (эксперимент)', linewidth=2)
    plt.plot(sizes, theoretical, '--', label='O(n) (теория)', linewidth=2)
    plt.xlabel('Размер данных')
    plt.ylabel('Время (сек)')
    plt.title('Проверка сложности build_heap: O(n)')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    # График 4: Отношение времени heapsort к n log n
    plt.subplot(2, 2, 4)
    # Теоретическая сложность O(n log n)
    theoretical_sort = [n * np.log2(n) * 1e-6 for n in sizes if n > 0]  # Масштабируем
    plt.plot(sizes, sort_inplace_times, 'o-', label='heapsort (эксперимент)', linewidth=2)
    plt.plot(sizes, theoretical_sort, '--', label='O(n log n) (теория)', linewidth=2)
    plt.xlabel('Размер данных')
    plt.ylabel('Время (сек)')
    plt.title('Проверка сложности heapsort: O(n log n)')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()
    

def main():
    """Главная функция тестирования"""    
    
    # Запуск всех тестов
    test_min_heap_basic()
    test_max_heap_basic()
    test_heap_sort()
    test_priority_queue()
    
    # Запуск сравнения производительности
    results = performance_comparison()  
        
    # Построение графиков (требует matplotlib)
    try:
        plot_performance(results)
    except ImportError:
        print("\nMatplotlib не установлен. Графики не будут построены.")
        print("Установите: pip install matplotlib") 

if __name__ == "__main__":
    main()