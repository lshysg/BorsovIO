import heapq
from dataclasses import dataclass, field
from typing import List, Tuple, Dict, Any, Optional
import matplotlib.pyplot as plt
import networkx as nx
import time
import random
import numpy as np
from collections import Counter

# ==================== Задача о выборе заявок ====================
@dataclass
class Interval:
    start: float
    end: float
    
    def __repr__(self):
        return f"({self.start:.1f}, {self.end:.1f})"

def interval_scheduling(intervals: List[Interval]) -> List[Interval]:
    """
    Жадный алгоритм для задачи о выборе максимального количества
    непересекающихся интервалов.
    Сложность: O(n log n) из-за сортировки
    """
    if not intervals:
        return []
    
    # Сортируем интервалы по времени окончания
    sorted_intervals = sorted(intervals, key=lambda x: x.end)
    
    selected = [sorted_intervals[0]]
    last_end = sorted_intervals[0].end
    
    for interval in sorted_intervals[1:]:
        if interval.start >= last_end:
            selected.append(interval)
            last_end = interval.end
    
    return selected

# ==================== Непрерывный рюкзак ====================
@dataclass(frozen=True)  # Делаем класс неизменяемым для хэширования
class Item:
    value: float
    weight: float
    id: int = field(default_factory=lambda: random.randint(1, 10000))  # Уникальный ID
    
    @property
    def ratio(self):
        return self.value / self.weight if self.weight > 0 else 0
    
    def __hash__(self):
        return hash(self.id)
    
    def __eq__(self, other):
        if not isinstance(other, Item):
            return False
        return self.id == other.id

def fractional_knapsack(capacity: float, items: List[Item]) -> Tuple[float, Dict[Item, float]]:
    """
    Жадный алгоритм для непрерывного рюкзака.
    Сложность: O(n log n) из-за сортировки
    """
    # Сортируем предметы по удельной стоимости (по убыванию)
    sorted_items = sorted(items, key=lambda x: x.ratio, reverse=True)
    
    total_value = 0.0
    remaining_capacity = capacity
    taken = {}
    
    for item in sorted_items:
        if remaining_capacity <= 0:
            break
        
        # Берем сколько можем от текущего предмета
        take_weight = min(item.weight, remaining_capacity)
        fraction = take_weight / item.weight
        
        taken[item] = fraction
        total_value += item.value * fraction
        remaining_capacity -= take_weight
    
    return total_value, taken

# ==================== Алгоритм Хаффмана ====================
@dataclass(order=True)
class HuffmanNode:
    freq: int
    char: Any = field(compare=False)
    left: Any = field(default=None, compare=False)
    right: Any = field(default=None, compare=False)
    
    def is_leaf(self):
        return self.left is None and self.right is None

def build_huffman_tree(frequencies: Dict[str, int]) -> Optional[HuffmanNode]:
    """
    Построение дерева Хаффмана.
    Сложность: O(n log n)
    """
    if not frequencies:
        return None
    
    # Создаем приоритетную очередь из узлов
    heap = [HuffmanNode(freq, char) for char, freq in frequencies.items()]
    heapq.heapify(heap)
    
    # Пока в очереди больше одного узла
    while len(heap) > 1:
        # Извлекаем два узла с наименьшей частотой
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        
        # Создаем новый узел
        merged = HuffmanNode(
            freq=left.freq + right.freq,
            char=None,
            left=left,
            right=right
        )
        
        heapq.heappush(heap, merged)
    
    return heap[0] if heap else None

def generate_huffman_codes(node: Optional[HuffmanNode], code="", codes=None) -> Dict[str, str]:
    """
    Генерация кодов Хаффмана из дерева.
    """
    if codes is None:
        codes = {}
    
    if node is None:
        return codes
    
    if node.is_leaf():
        codes[node.char] = code if code else "0"
    else:
        generate_huffman_codes(node.left, code + "0", codes)
        generate_huffman_codes(node.right, code + "1", codes)
    
    return codes

def huffman_coding(data: str) -> Tuple[Optional[HuffmanNode], Dict[str, str]]:
    """
    Полный алгоритм Хаффмана.
    """
    if not data:
        return None, {}
    
    # Подсчет частот
    freq = {}
    for char in data:
        freq[char] = freq.get(char, 0) + 1
    
    # Построение дерева
    tree = build_huffman_tree(freq)
    
    # Генерация кодов
    codes = generate_huffman_codes(tree)
    
    return tree, codes

# ==================== Задача о сдаче ====================
def coin_change_greedy(amount: int, coins: List[int]) -> Dict[int, int]:
    """
    Жадный алгоритм для задачи о сдаче.
    Работает оптимально для канонических систем монет.
    """
    # Сортируем монеты по убыванию
    coins_sorted = sorted(coins, reverse=True)
    result = {}
    
    remaining = amount
    
    for coin in coins_sorted:
        if remaining >= coin:
            count = remaining // coin
            result[coin] = count
            remaining -= coin * count
    
    if remaining > 0:
        raise ValueError(f"Невозможно выдать сдачу для суммы {amount}")
    
    return result

# ==================== Визуализация дерева Хаффмана ====================
def visualize_huffman_tree(node: Optional[HuffmanNode], filename="huffman_tree.png"):
    """
    Визуализация дерева Хаффмана.
    """
    if node is None:
        print("Дерево пустое, визуализация невозможна")
        return
    
    G = nx.Graph()
    pos = {}
    
    def add_edges(current_node, parent=None, depth=0, x=0, width=2):
        if current_node is None:
            return
        
        node_id = id(current_node)
        label = f"{current_node.char}:{current_node.freq}" if current_node.char else f"{current_node.freq}"
        
        # Позиционирование
        pos[node_id] = (x, -depth)
        G.add_node(node_id, label=label)
        
        if parent is not None:
            G.add_edge(parent, node_id)
        
        if not current_node.is_leaf():
            # Рекурсивно добавляем детей
            add_edges(current_node.left, node_id, depth+1, x-width/2, width/2)
            add_edges(current_node.right, node_id, depth+1, x+width/2, width/2)
    
    add_edges(node)
    
    plt.figure(figsize=(12, 8))
    labels = nx.get_node_attributes(G, 'label')
    nx.draw(G, pos, with_labels=True, labels=labels, 
            node_size=2000, node_color='lightblue',
            font_size=10, font_weight='bold')
    plt.title("Дерево Хаффмана")
    plt.savefig(filename, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Дерево сохранено в {filename}")

# ==================== Визуализация производительности алгоритмов ====================
def visualize_performance_comparison(filename="performance_comparison.png"):
    """
    График зависимости времени работы алгоритмов от размера входных данных.
    """
    # Тестируемые размеры данных
    sizes = [100, 500, 1000, 2000, 5000, 10000]
    
    # Результаты измерений
    huffman_times = []
    scheduling_times = []
    knapsack_times = []
    
    print("=" * 60)
    print("Измерение производительности алгоритмов")
    print("=" * 60)
    
    for size in sizes:
        print(f"\nТестирование для размера данных: {size}")
        
        # Генерация тестовых данных
        # 1. Для Хаффмана
        huffman_data = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=size))
        
        # 2. Для задачи о выборе заявок
        intervals = []
        for i in range(size // 10):  # Меньше интервалов для наглядности
            start = random.uniform(0, 100)
            end = start + random.uniform(1, 10)
            intervals.append(Interval(start, end))
        
        # 3. Для задачи о рюкзаке
        items = []
        for i in range(size // 20):  # Еще меньше предметов
            value = random.uniform(10, 100)
            weight = random.uniform(1, 20)
            items.append(Item(value, weight))
        capacity = random.uniform(50, 200)
        
        # Измерение времени для алгоритма Хаффмана
        start_time = time.time()
        tree, codes = huffman_coding(huffman_data)
        huffman_time = time.time() - start_time
        huffman_times.append(huffman_time)
        print(f"  Алгоритм Хаффмана: {huffman_time:.6f} сек")
        
        # Измерение времени для задачи о выборе заявок
        if intervals:
            start_time = time.time()
            selected = interval_scheduling(intervals)
            scheduling_time = time.time() - start_time
            scheduling_times.append(scheduling_time)
            print(f"  Задача о выборе заявок: {scheduling_time:.6f} сек")
        else:
            scheduling_times.append(0)
        
        # Измерение времени для задачи о рюкзаке
        if items:
            start_time = time.time()
            total_value, _ = fractional_knapsack(capacity, items)
            knapsack_time = time.time() - start_time
            knapsack_times.append(knapsack_time)
            print(f"  Непрерывный рюкзак: {knapsack_time:.6f} сек")
        else:
            knapsack_times.append(0)
    
    # Построение графика
    plt.figure(figsize=(14, 8))
    
    # Основной график
    plt.subplot(2, 2, 1)
    plt.plot(sizes, huffman_times, 'bo-', linewidth=2, markersize=6, label='Алгоритм Хаффмана')
    plt.plot(sizes, scheduling_times, 'rs-', linewidth=2, markersize=6, label='Выбор заявок')
    plt.plot(sizes, knapsack_times, 'g^-', linewidth=2, markersize=6, label='Непрерывный рюкзак')
    
    plt.xlabel('Размер входных данных')
    plt.ylabel('Время выполнения (сек)')
    plt.title('Сравнение производительности жадных алгоритмов')
    plt.grid(True, alpha=0.3)
    plt.legend()
    
    # График в логарифмическом масштабе (время)
    plt.subplot(2, 2, 2)
    plt.semilogy(sizes, huffman_times, 'bo-', linewidth=2, markersize=6, label='Алгоритм Хаффмана')
    plt.semilogy(sizes, scheduling_times, 'rs-', linewidth=2, markersize=6, label='Выбор заявок')
    plt.semilogy(sizes, knapsack_times, 'g^-', linewidth=2, markersize=6, label='Непрерывный рюкзак')
    
    plt.xlabel('Размер входных данных')
    plt.ylabel('Время выполнения (сек, log scale)')
    plt.title('Производительность в логарифмическом масштабе')
    plt.grid(True, alpha=0.3)
    plt.legend()
    
    # График зависимости O(n log n)
    plt.subplot(2, 2, 3)
    # Нормализуем первую точку для каждой кривой
    if huffman_times and sizes:
        norm_factor_h = huffman_times[0] / (sizes[0] * np.log(sizes[0]))
        y_fit_h = [norm_factor_h * (x * np.log(x)) for x in sizes]
        plt.plot(sizes, y_fit_h, 'b--', alpha=0.7, label='O(n log n)')
    
    if scheduling_times and sizes:
        norm_factor_s = scheduling_times[0] / (sizes[0] * np.log(sizes[0]))
        y_fit_s = [norm_factor_s * (x * np.log(x)) for x in sizes]
        plt.plot(sizes, y_fit_s, 'r--', alpha=0.7)
    
    if knapsack_times and sizes:
        norm_factor_k = knapsack_times[0] / (sizes[0] * np.log(sizes[0]))
        y_fit_k = [norm_factor_k * (x * np.log(x)) for x in sizes]
        plt.plot(sizes, y_fit_k, 'g--', alpha=0.7)
    
    plt.plot(sizes, huffman_times, 'bo-', linewidth=2, markersize=6, label='Алгоритм Хаффмана (факт)')
    plt.plot(sizes, scheduling_times, 'rs-', linewidth=2, markersize=6, label='Выбор заявок (факт)')
    plt.plot(sizes, knapsack_times, 'g^-', linewidth=2, markersize=6, label='Непрерывный рюкзак (факт)')
    
    plt.xlabel('Размер входных данных')
    plt.ylabel('Время выполнения (сек)')
    plt.title('Сравнение с теоретической сложностью O(n log n)')
    plt.grid(True, alpha=0.3)
    plt.legend()
    
    # Таблица результатов
    plt.subplot(2, 2, 4)
    plt.axis('off')
    
    # Создаем текстовую таблицу
    table_data = []
    table_data.append(['Размер', 'Хаффман', 'Заявки', 'Рюкзак'])
    
    for i, size in enumerate(sizes):
        table_data.append([
            str(size),
            f"{huffman_times[i]:.6f}",
            f"{scheduling_times[i]:.6f}",
            f"{knapsack_times[i]:.6f}"
        ])
    
    # Добавляем итоговую строку
    table_data.append([
        'Отношение',
        f"{huffman_times[-1]/huffman_times[0]:.2f}x",
        f"{scheduling_times[-1]/scheduling_times[0]:.2f}x",
        f"{knapsack_times[-1]/knapsack_times[0]:.2f}x"
    ])
    
    # Рисуем таблицу
    table = plt.table(cellText=table_data,
                      cellLoc='center',
                      loc='center',
                      colWidths=[0.2, 0.25, 0.25, 0.25])
    
    table.auto_set_font_size(False)
    table.set_fontsize(9)
    table.scale(1, 1.5)
    
    plt.title('Время выполнения (секунды)')
    
    plt.tight_layout()
    plt.savefig(filename, dpi=300, bbox_inches='tight')
    plt.close()
    
    print(f"\nГрафик производительности сохранен в {filename}")
    
    # Анализ сложности
    print("\n" + "=" * 60)
    print("Анализ асимптотической сложности:")
    print("=" * 60)
    
    if len(sizes) > 1:
        # Оцениваем рост времени для каждого алгоритма
        for i in range(len(sizes)-1):
            size_ratio = sizes[i+1] / sizes[i]
            
            if huffman_times[i] > 0 and huffman_times[i+1] > 0:
                time_ratio_h = huffman_times[i+1] / huffman_times[i]
                expected_ratio = size_ratio * np.log(size_ratio) / np.log(sizes[i]) if sizes[i] > 1 else size_ratio
                print(f"\nОт {sizes[i]} до {sizes[i+1]} (в {size_ratio:.1f} раз больше):")
                print(f"  Алгоритм Хаффмана: время увеличилось в {time_ratio_h:.2f} раз")
                print(f"  Ожидаемо для O(n log n): примерно в {expected_ratio:.2f} раз")
            
            if scheduling_times[i] > 0 and scheduling_times[i+1] > 0:
                time_ratio_s = scheduling_times[i+1] / scheduling_times[i]
                print(f"  Задача о выборе заявок: время увеличилось в {time_ratio_s:.2f} раз")
            
            if knapsack_times[i] > 0 and knapsack_times[i+1] > 0:
                time_ratio_k = knapsack_times[i+1] / knapsack_times[i]
                print(f"  Непрерывный рюкзак: время увеличилось в {time_ratio_k:.2f} раз")

# ==================== Демонстрационная функция ====================
def demo_algorithms():
    """
    Демонстрация работы всех алгоритмов с визуализацией.
    """
    print("=" * 60)
    print("ДЕМОНСТРАЦИЯ ЖАДНЫХ АЛГОРИТМОВ")
    print("=" * 60)
    
    # 1. Алгоритм Хаффмана
    print("\n1. АЛГОРИТМ ХАФФМАНА")
    print("-" * 40)
    
    text = "abracadabra"
    print(f"Исходный текст: '{text}'")
    
    # Подсчет частот
    freq = Counter(text)
    print("Частоты символов:")
    for char, count in sorted(freq.items()):
        print(f"  '{char}': {count}")
    
    # Кодирование
    tree, codes = huffman_coding(text)
    print("\nКоды Хаффмана:")
    for char, code in sorted(codes.items()):
        print(f"  '{char}': {code}")
    
    # Визуализация дерева
    visualize_huffman_tree(tree, "demo_huffman_tree.png")
    
    # 2. Задача о выборе заявок
    print("\n\n2. ЗАДАЧА О ВЫБОРЕ ЗАЯВОК")
    print("-" * 40)
    
    intervals = [
        Interval(1, 3), Interval(2, 5), Interval(4, 7),
        Interval(6, 9), Interval(8, 10), Interval(9, 11)
    ]
    
    print("Все интервалы:")
    for i, interval in enumerate(intervals, 1):
        print(f"  {i}. {interval}")
    
    selected = interval_scheduling(intervals)
    print(f"\nВыбранные интервалы ({len(selected)} из {len(intervals)}):")
    for i, interval in enumerate(selected, 1):
        print(f"  {i}. {interval}")
    
    # 3. Непрерывный рюкзак
    print("\n\n3. НЕПРЕРЫВНЫЙ РЮКЗАК")
    print("-" * 40)
    
    items = [
        Item(value=60, weight=10),
        Item(value=100, weight=20),
        Item(value=120, weight=30),
        Item(value=80, weight=15)
    ]
    
    capacity = 50
    print(f"Вместимость рюкзака: {capacity}")
    print("Предметы:")
    for i, item in enumerate(items, 1):
        print(f"  {i}. стоимость={item.value}, вес={item.weight}, цена/вес={item.ratio:.2f}")
    
    total_value, taken = fractional_knapsack(capacity, items)
    print(f"\nОбщая стоимость: {total_value:.2f}")
    print("Взятые предметы:")
    for item, fraction in taken.items():
        print(f"  Предмет(ст={item.value}, в={item.weight}): {fraction:.1%}")
    
    # 4. Визуализация производительности
    print("\n\n4. ВИЗУАЛИЗАЦИЯ ПРОИЗВОДИТЕЛЬНОСТИ")
    print("-" * 40)
    visualize_performance_comparison("performance_comparison.png")
    
    print("\n" + "=" * 60)
    print("ДЕМОНСТРАЦИЯ ЗАВЕРШЕНА")
    print("=" * 60)


if __name__ == "__main__":
    # Запуск демонстрации
    demo_algorithms()