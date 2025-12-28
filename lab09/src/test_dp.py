"""
Тестирование и демонстрация работы алгоритмов ДП.
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from dynamic_programming import (
    Fibonacci, Knapsack, LCS, Levenshtein, CoinChange, LIS
)
from comparison import Comparison
from visualization import DPVisualizer


def test_fibonacci():
    """Тестирование вычисления чисел Фибоначчи."""
    print("Тестирование вычисления чисел Фибоначчи")
    print("="*60)
    
    test_cases = [0, 1, 5, 10, 20]
    
    for n in test_cases:
        print(f"\nF({n}):")
        
        # Рекурсия с мемоизацией
        result_memo = Fibonacci.memoization_recursive(n)
        print(f"  Мемоизация: {result_memo}")
        
        # Итеративный
        result_iter = Fibonacci.iterative(n)
        print(f"  Итеративный: {result_iter}")
        
        # Оптимизированный
        result_opt = Fibonacci.optimized_iterative(n)
        print(f"  Оптимизированный: {result_opt}")
        
        # Проверка корректности
        assert result_memo == result_iter == result_opt, f"Ошибка для n={n}"
    
    print("\n✓ Все вычисления корректны!")


def test_knapsack():
    """Тестирование задачи о рюкзаке."""
    print("\n\nТестирование задачи о рюкзаке")
    print("="*60)
    
    # Тестовый случай 1
    weights = [2, 3, 4, 5]
    values = [3, 4, 5, 6]
    capacity = 5
    
    print(f"\nТест 1:")
    print(f"  Веса: {weights}")
    print(f"  Стоимости: {values}")
    print(f"  Вместимость: {capacity}")
    
    max_value, selected = Knapsack.bottom_up(weights, values, capacity)
    print(f"  Максимальная стоимость: {max_value}")
    print(f"  Выбранные предметы: {selected}")
    
    # Проверка
    total_weight = sum(weights[i] for i in selected)
    total_value = sum(values[i] for i in selected)
    assert total_weight <= capacity
    assert total_value == max_value
    
    # Тестовый случай 2
    weights = [10, 20, 30]
    values = [60, 100, 120]
    capacity = 50
    
    print(f"\nТест 2:")
    print(f"  Веса: {weights}")
    print(f"  Стоимости: {values}")
    print(f"  Вместимость: {capacity}")
    
    max_value, selected = Knapsack.bottom_up(weights, values, capacity)
    print(f"  Максимальная стоимость: {max_value}")
    print(f"  Выбранные предметы: {selected}")
    
    print("\n✓ Задача о рюкзаке решена корректно!")


def test_lcs():
    """Тестирование поиска наибольшей общей подпоследовательности."""
    print("\n\nТестирование LCS")
    print("="*60)
    
    test_cases = [
        ("ABCDGH", "AEDFHR", "ADH"),
        ("AGGTAB", "GXTXAYB", "GTAB"),
        ("ABCBDAB", "BDCAB", "BCAB"),
    ]
    
    for str1, str2, expected in test_cases:
        length, lcs = LCS.bottom_up(str1, str2)
        
        print(f"\nСтрока 1: '{str1}'")
        print(f"Строка 2: '{str2}'")
        print(f"  Ожидаемая LCS: '{expected}'")
        print(f"  Найденная LCS: '{lcs}' (длина: {length})")
        
        assert lcs == expected, f"Ошибка для '{str1}' и '{str2}'"
        assert len(lcs) == length
    
    print("\n✓ LCS найден корректно!")


def test_levenshtein():
    """Тестирование расстояния Левенштейна."""
    print("\n\nТестирование расстояния Левенштейна")
    print("="*60)
    
    test_cases = [
        ("kitten", "sitting", 3),
        ("saturday", "sunday", 3),
        ("", "abc", 3),
        ("abc", "", 3),
        ("same", "same", 0),
    ]
    
    for str1, str2, expected in test_cases:
        distance = Levenshtein.bottom_up(str1, str2)
        
        print(f"\n'{str1}' -> '{str2}'")
        print(f"  Ожидаемое расстояние: {expected}")
        print(f"  Вычисленное расстояние: {distance}")
        
        assert distance == expected, f"Ошибка для '{str1}' -> '{str2}'"
    
    print("\n✓ Расстояние Левенштейна вычислено корректно!")


def test_coin_change():
    """Тестирование задачи размена монет."""
    print("\n\nТестирование задачи размена монет")
    print("="*60)
    
    # Минимальное количество монет
    coins = [1, 2, 5]
    amount = 11
    min_coins = CoinChange.min_coins(coins, amount)
    print(f"\nМинимальное количество монет для суммы {amount}:")
    print(f"  Монеты: {coins}")
    print(f"  Минимальное количество: {min_coins}")
    assert min_coins == 3  # 5 + 5 + 1
    
    # Количество способов
    amount = 5
    num_ways = CoinChange.num_ways(coins, amount)
    print(f"\nКоличество способов разменять сумму {amount}:")
    print(f"  Монеты: {coins}")
    print(f"  Количество способов: {num_ways}")
    assert num_ways == 4  # [5], [2+2+1], [2+1+1+1], [1+1+1+1+1]
    
    # Случай, когда размен невозможен
    coins = [2]
    amount = 3
    min_coins = CoinChange.min_coins(coins, amount)
    print(f"\nРазмен невозможен:")
    print(f"  Монеты: {coins}")
    print(f"  Сумма: {amount}")
    print(f"  Результат: {min_coins}")
    assert min_coins == -1
    
    print("\n✓ Задача размена монет решена корректно!")


def test_lis():
    """Тестирование поиска наибольшей возрастающей подпоследовательности."""
    print("\n\nТестирование LIS")
    print("="*60)
    
    test_cases = [
        ([10, 9, 2, 5, 3, 7, 101, 18], [2, 3, 7, 18]),
        ([0, 1, 0, 3, 2, 3], [0, 1, 2, 3]),
        ([7, 7, 7, 7, 7, 7, 7], [7]),
        ([], []),
    ]
    
    for nums, expected in test_cases:
        length, lis = LIS.length(nums)
        
        print(f"\nПоследовательность: {nums}")
        print(f"  Ожидаемая LIS: {expected}")
        print(f"  Найденная LIS: {lis} (длина: {length})")
        
        assert lis == expected, f"Ошибка для {nums}"
        assert len(lis) == length
    
    print("\n✓ LIS найден корректно!")


def run_experiments():
    """Экспериментальное исследование масштабируемости."""
    print("\n\nЭкспериментальное исследование масштабируемости")
    print("="*60)
    
    # Исследование задачи о рюкзаке
    print("\n1. Масштабируемость задачи о рюкзаке:")
    
    import time
    
    capacities = [10, 20, 30, 40, 50]
    times = []
    
    for capacity in capacities:
        # Генерируем тестовые данные
        n_items = capacity
        weights = [i+1 for i in range(n_items)]
        values = [(i+1) * 10 for i in range(n_items)]
        
        start = time.perf_counter()
        Knapsack.bottom_up(weights, values, capacity)
        elapsed = time.perf_counter() - start
        
        times.append(elapsed)
        print(f"  Вместимость: {capacity}, предметов: {n_items}, время: {elapsed:.6f} сек")
    
    # Исследование LCS
    print("\n2. Масштабируемость LCS:")
    
    lengths = [10, 20, 30, 40, 50]
    for length in lengths:
        # Генерируем случайные строки
        import random
        import string
        
        str1 = ''.join(random.choices(string.ascii_uppercase, k=length))
        str2 = ''.join(random.choices(string.ascii_uppercase, k=length))
        
        start = time.perf_counter()
        LCS.bottom_up(str1, str2)
        elapsed = time.perf_counter() - start
        
        print(f"  Длина строк: {length}, время: {elapsed:.6f} сек")


def main():
    """Основная функция тестирования."""
    print("Тестирование алгоритмов динамического программирования")
    print("="*60)
    
    # Запуск тестов
    test_fibonacci()
    test_knapsack()
    test_lcs()
    test_levenshtein()
    test_coin_change()
    test_lis()
    
    # Эксперименты
    run_experiments()
    
    print("\n" + "="*60)
    print("Все тесты пройдены успешно!")
    print("="*60)
    
    # Дополнительно: демонстрация визуализации
    print("\n\nДемонстрация визуализации таблиц ДП")
    print("="*60)
    
    answer = input("Хотите увидеть визуализацию таблиц? (y/n): ")
    if answer.lower() == 'y':
        # Простая демонстрация
        str1 = "ABC"
        str2 = "ACB"
        print(f"\nВизуализация таблицы LCS для '{str1}' и '{str2}':")
        
        # Создаем простую таблицу
        from dynamic_programming import LCS
        length, lcs = LCS.bottom_up(str1, str2)
        print(f"LCS: '{lcs}' (длина: {length})")
        
        # Простая текстовая визуализация
        m, n = len(str1), len(str2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if str1[i-1] == str2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        print("\nТаблица DP:")
        print("   ", "  ".join([' '] + list(str2)))
        for i in range(m + 1):
            row_char = ' ' if i == 0 else str1[i-1]
            row_vals = [f"{dp[i][j]:2}" for j in range(n + 1)]
            print(f"{row_char}: {' '.join(row_vals)}")


if __name__ == "__main__":
    main()