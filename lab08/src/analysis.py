import itertools
import time
import matplotlib.pyplot as plt
from greedy_algorithms import *
import random
from typing import List, Tuple, Dict

def brute_force_knapsack_01(capacity: float, items: List[Item]) -> float:
    """
    Полный перебор для задачи 0-1 рюкзака.
    Экспоненциальная сложность: O(2^n)
    """
    n = len(items)
    max_value = 0
    
    # Перебираем все возможные комбинации
    for i in range(1 << n):
        total_weight = 0
        total_value = 0
        
        for j in range(n):
            if i & (1 << j):
                total_weight += items[j].weight
                total_value += items[j].value
        
        if total_weight <= capacity and total_value > max_value:
            max_value = total_value
    
    return max_value

def compare_knapsack_algorithms():
    """
    Сравнение жадного алгоритма и полного перебора.
    """
    # Тестовые данные
    test_cases = [
        {
            "capacity": 50,
            "items": [
                Item(value=60, weight=10),
                Item(value=100, weight=20),
                Item(value=120, weight=30),
            ]
        },
        {
            "capacity": 10,
            "items": [
                Item(value=5, weight=1),
                Item(value=6, weight=2),
                Item(value=7, weight=3),
                Item(value=8, weight=4),
                Item(value=9, weight=5),
            ]
        },
        {
            "capacity": 50,
            "items": [
                Item(value=30, weight=5),
                Item(value=20, weight=10),
                Item(value=100, weight=20),
                Item(value=90, weight=30),
                Item(value=160, weight=40),
            ]
        }
    ]
    
    print("=" * 60)
    print("Сравнение алгоритмов для задачи о рюкзаке")
    print("=" * 60)
    
    for i, test in enumerate(test_cases, 1):
        print(f"\nТест {i}:")
        print(f"Вместимость рюкзака: {test['capacity']}")
        print("Предметы:")
        for idx, item in enumerate(test["items"], 1):
            print(f"  {idx}. стоимость={item.value}, вес={item.weight}, цена/вес={item.ratio:.2f}")
        
        # Жадный алгоритм для непрерывного рюкзака
        greedy_value, taken = fractional_knapsack(test["capacity"], test["items"])
        print(f"\nЖадный алгоритм (непрерывный): {greedy_value:.2f}")
        print("Взятые предметы:")
        for item, fraction in taken.items():
            print(f"  Предмет(ст={item.value}, в={item.weight}): {fraction:.1%}")
        
        # Полный перебор для 0-1 рюкзака
        if len(test["items"]) <= 15:  # Ограничиваем размер для перебора
            start_time = time.time()
            optimal_value = brute_force_knapsack_01(test["capacity"], test["items"])
            elapsed = time.time() - start_time
            print(f"\nПолный перебор (0-1): {optimal_value:.2f}")
            print(f"Время выполнения перебора: {elapsed:.6f} сек")
            
            # Сравнение
            if optimal_value > 0:
                ratio = greedy_value / optimal_value
                print(f"Отношение жадный/оптимальный: {ratio:.2%}")
                if ratio < 1.0:
                    print("⚠️  Жадный алгоритм дает неоптимальный результат для 0-1 рюкзака!")
            else:
                print("Оптимальное значение равно 0")
        else:
            print("\nСлишком много предметов для полного перебора")

def analyze_huffman_performance():
    """
    Анализ производительности алгоритма Хаффмана.
    """
    print("\n" + "=" * 60)
    print("Анализ производительности алгоритма Хаффмана")
    print("=" * 60)
    
    sizes = [100, 500, 1000, 5000, 10000]
    times = []
    
    for size in sizes:
        # Генерируем случайные данные
        data = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', 
                                     k=size))
        
        start_time = time.time()
        tree, codes = huffman_coding(data)
        elapsed = time.time() - start_time
        
        times.append(elapsed)
        
        print(f"\nРазмер данных: {size}")
        print(f"Время выполнения: {elapsed:.6f} сек")
        print(f"Различных символов: {len(codes)}")
        
        # Вычисляем степень сжатия
        original_bits = size * 8
        compressed_bits = sum(len(codes[char]) for char in data)
        if original_bits > 0:
            compression_ratio = compressed_bits / original_bits
            print(f"Коэффициент сжатия: {compression_ratio:.2%}")
        else:
            print("Коэффициент сжатия: N/A (нулевой размер)")
        print("-" * 40)
    
    # Визуализация
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, times, 'bo-', linewidth=2, markersize=8)
    plt.xlabel('Размер входных данных')
    plt.ylabel('Время выполнения (сек)')
    plt.title('Производительность алгоритма Хаффмана')
    plt.grid(True, alpha=0.3)
    
    # Теоретическая сложность O(n log n)
    if len(sizes) > 1 and len(times) > 1:
        x_fit = np.linspace(min(sizes), max(sizes), 100)
        # Нормализуем первую точку
        y_fit = [times[0] * (x * np.log(x)) / (sizes[0] * np.log(sizes[0])) 
                 for x in x_fit]
        plt.plot(x_fit, y_fit, 'r--', label='O(n log n)', alpha=0.7)
        plt.legend()
    
    plt.savefig('huffman_performance.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("\nГрафик производительности сохранен в 'huffman_performance.png'")

def test_coin_change():
    """
    Тестирование жадного алгоритма для задачи о сдаче.
    """
    print("\n" + "=" * 60)
    print("Тестирование задачи о сдаче")
    print("=" * 60)
    
    # Стандартная система монет (жадный алгоритм работает оптимально)
    standard_coins = [1, 2, 5, 10, 20, 50, 100, 200, 500]
    
    # Нестандартная система (жадный может давать неоптимальный результат)
    non_standard_coins = [1, 3, 4]
    
    test_amounts = [6, 7, 27, 123, 456]
    
    for amount in test_amounts:
        print(f"\nСумма: {amount}")
        
        # Стандартная система
        try:
            change_std = coin_change_greedy(amount, standard_coins)
            coins_std = sum(change_std.values())
            print(f"Стандартные монеты: {change_std}")
            print(f"  Всего монет: {coins_std}")
        except ValueError as e:
            print(f"Ошибка для стандартных монет: {e}")
        
        # Нестандартная система
        try:
            change_nonstd = coin_change_greedy(amount, non_standard_coins)
            coins_nonstd = sum(change_nonstd.values())
            
            # Проверяем оптимальность
            optimal = find_optimal_change(amount, non_standard_coins)
            coins_optimal = sum(optimal.values())
            
            print(f"\nНестандартные монеты (жадный): {change_nonstd}")
            print(f"  Монет: {coins_nonstd}")
            print(f"Нестандартные монеты (оптимальный): {optimal}")
            print(f"  Монет: {coins_optimal}")
            
            if coins_nonstd > coins_optimal:
                print("⚠️  Жадный алгоритм не оптимален!")
        except ValueError as e:
            print(f"Ошибка для нестандартных монет: {e}")

def find_optimal_change(amount: int, coins: List[int]) -> Dict[int, int]:
    """
    Динамическое программирование для оптимальной сдачи.
    """
    if amount <= 0:
        return {}
    
    # Сортируем монеты
    coins_sorted = sorted(coins)
    
    # DP массив
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    
    # Для восстановления решения
    prev = [-1] * (amount + 1)
    coin_used = [0] * (amount + 1)
    
    for i in range(1, amount + 1):
        for coin in coins_sorted:
            if i >= coin and dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                prev[i] = i - coin
                coin_used[i] = coin
    
    if dp[amount] == float('inf'):
        raise ValueError(f"Невозможно выдать сдачу для суммы {amount}")
    
    # Восстановление решения
    result = {}
    current = amount
    while current > 0:
        coin = coin_used[current]
        result[coin] = result.get(coin, 0) + 1
        current = prev[current]
    
    return result

def run_experiments():
    """
    Запуск всех экспериментов.
    """
    print("=" * 60)
    print("ЭКСПЕРИМЕНТАЛЬНОЕ ИССЛЕДОВАНИЕ ЖАДНЫХ АЛГОРИТМОВ")
    print("=" * 60)
    
    # Часть 1: Сравнение алгоритмов для рюкзака
    compare_knapsack_algorithms()
    
    # Часть 2: Анализ производительности Хаффмана
    analyze_huffman_performance()
    
    # Часть 3: Тестирование задачи о сдаче
    test_coin_change()
    
    # Часть 4: Визуализация производительности всех алгоритмов
    print("\n" + "=" * 60)
    print("ВИЗУАЛИЗАЦИЯ ЗАВИСИМОСТИ ВРЕМЕНИ ОТ РАЗМЕРА ДАННЫХ")
    print("=" * 60)
    
    # Импортируем и вызываем функцию визуализации
    from greedy_algorithms import visualize_performance_comparison
    visualize_performance_comparison("performance_comparison_full.png")
    
    # Часть 5: Демонстрация работы других алгоритмов
    print("\n" + "=" * 60)
    print("ДЕМОНСТРАЦИЯ ДРУГИХ АЛГОРИТМОВ")
    print("=" * 60)
    
    # Interval Scheduling
    print("\n1. Задача о выборе заявок:")
    intervals = [
        Interval(1, 3), Interval(2, 5), Interval(4, 7),
        Interval(6, 9), Interval(8, 10)
    ]
    selected = interval_scheduling(intervals)
    print(f"Все интервалы: {intervals}")
    print(f"Выбранные интервалы: {selected}")
    print(f"Количество выбранных интервалов: {len(selected)}")
    

    
    print("\n" + "=" * 60)
    print("ВСЕ ЭКСПЕРИМЕНТЫ ЗАВЕРШЕНЫ")
    print("=" * 60)

if __name__ == "__main__":
    run_experiments()