"""
Сравнительный анализ алгоритмов динамического программирования.
"""

import time
import sys
import matplotlib.pyplot as plt
import numpy as np
from typing import Dict, List, Tuple
from dynamic_programming import Fibonacci, Knapsack


class Comparison:
    """Класс для сравнения различных подходов ДП."""
    
    @staticmethod
    def compare_fibonacci(n_values: List[int] = [5, 10, 20, 30, 40]) -> Dict[str, List[float]]:
        """
        Сравнение времени работы разных методов вычисления чисел Фибоначчи.
        """
        results = {
            'naive': [],
            'memoization': [],
            'iterative': [],
            'optimized': []
        }
        
        for n in n_values:
            print(f"\nВычисление F({n}):")
            
            # Наивная рекурсия (только для небольших n)
            if n <= 30:
                start = time.perf_counter()
                result = Fibonacci.naive_recursive(n)
                elapsed = time.perf_counter() - start
                results['naive'].append(elapsed)
                print(f"  Наивная рекурсия: {result} за {elapsed:.6f} сек")
            
            # Рекурсия с мемоизацией
            start = time.perf_counter()
            result = Fibonacci.memoization_recursive(n)
            elapsed = time.perf_counter() - start
            results['memoization'].append(elapsed)
            print(f"  С мемоизацией: {result} за {elapsed:.6f} сек")
            
            # Итеративный подход
            start = time.perf_counter()
            result = Fibonacci.iterative(n)
            elapsed = time.perf_counter() - start
            results['iterative'].append(elapsed)
            print(f"  Итеративный: {result} за {elapsed:.6f} сек")
            
            # Оптимизированный итеративный
            start = time.perf_counter()
            result = Fibonacci.optimized_iterative(n)
            elapsed = time.perf_counter() - start
            results['optimized'].append(elapsed)
            print(f"  Оптимизированный: {result} за {elapsed:.6f} сек")
        
        return results
    
    @staticmethod
    def compare_knapsack_algorithms() -> None:
        """
        Сравнение жадного алгоритма и ДП для задачи о рюкзаке.
        """
        print("\n" + "="*60)
        print("Сравнение алгоритмов для задачи о рюкзаке")
        print("="*60)
        
        # Тестовые данные
        weights = [10, 20, 30, 40, 50]
        values = [60, 100, 120, 140, 160]
        capacities = [50, 100, 150]
        
        for capacity in capacities:
            print(f"\nВместимость рюкзака: {capacity}")
            print(f"Предметы: веса={weights}, стоимости={values}")
            
            # Жадный алгоритм (непрерывный рюкзак)
            greedy_result = Knapsack.greedy_fractional(weights, values, capacity)
            print(f"Жадный алгоритм (непрерывный): {greedy_result:.2f}")
            
            # ДП (0-1 рюкзак)
            dp_result, selected = Knapsack.bottom_up(weights, values, capacity)
            print(f"ДП (0-1 рюкзак): {dp_result}")
            print(f"  Выбранные предметы: {selected}")
            
            print(f"Разница: {dp_result - greedy_result:.2f}")
    
    @staticmethod
    def analyze_complexity() -> None:
        """
        Анализ временной и пространственной сложности алгоритмов.
        """
        print("\n" + "="*60)
        print("Анализ сложности алгоритмов ДП")
        print("="*60)
        
        complexities = {
            "Числа Фибоначчи (наивная рекурсия)": {
                "Время": "O(2^n)",
                "Память": "O(n)"
            },
            "Числа Фибоначчи (мемоизация)": {
                "Время": "O(n)",
                "Память": "O(n)"
            },
            "Числа Фибоначчи (итеративный)": {
                "Время": "O(n)",
                "Память": "O(n)"
            },
            "Числа Фибоначчи (оптимизированный)": {
                "Время": "O(n)",
                "Память": "O(1)"
            },
            "Задача о рюкзаке 0-1": {
                "Время": "O(n*W)",
                "Память": "O(n*W)"
            },
            "LCS": {
                "Время": "O(m*n)",
                "Память": "O(m*n)"
            },
            "Расстояние Левенштейна": {
                "Время": "O(m*n)",
                "Память": "O(m*n)"
            },
            "Размен монет (минимальное количество)": {
                "Время": "O(n*amount)",
                "Память": "O(amount)"
            },
            "LIS (наивный)": {
                "Время": "O(n^2)",
                "Память": "O(n)"
            }
        }
        
        for algorithm, comp in complexities.items():
            print(f"\n{algorithm}:")
            print(f"  Временная сложность: {comp['Время']}")
            print(f"  Пространственная сложность: {comp['Память']}")
    
    @staticmethod
    def plot_fibonacci_comparison(n_values: List[int], results: Dict[str, List[float]]) -> None:
        """
        Построение графика сравнения методов вычисления чисел Фибоначчи.
        """
        plt.figure(figsize=(10, 6))
        
        for method, times in results.items():
            if len(times) == len(n_values):  # Проверяем, что данные совпадают
                plt.plot(n_values, times, marker='o', label=method)
        
        plt.xlabel('n (номер числа Фибоначчи)')
        plt.ylabel('Время выполнения (сек)')
        plt.title('Сравнение методов вычисления чисел Фибоначчи')
        plt.legend()
        plt.grid(True)
        plt.yscale('log')  # Логарифмическая шкала для наглядности
        plt.savefig('fibonacci_comparison.png', dpi=300, bbox_inches='tight')
        plt.show()
        
        print("\nГрафик сохранен как 'fibonacci_comparison.png'")


def main():
    """Основная функция для запуска сравнений."""
    
    # Сравнение методов вычисления чисел Фибоначчи
    print("Сравнение методов вычисления чисел Фибоначчи")
    print("="*60)
    
    n_values = [5, 10, 20, 30, 40, 50]
    results = Comparison.compare_fibonacci(n_values)
    
    # Построение графика
    Comparison.plot_fibonacci_comparison(n_values[:len(results['memoization'])], results)
    
    # Сравнение алгоритмов для рюкзака
    Comparison.compare_knapsack_algorithms()
    
    # Анализ сложности
    Comparison.analyze_complexity()


if __name__ == "__main__":
    main()