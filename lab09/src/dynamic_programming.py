"""
Реализация алгоритмов динамического программирования.
"""

import functools
import time
from typing import List, Tuple, Dict, Any


class Fibonacci:
    """Класс для вычисления чисел Фибоначчи различными методами."""
    
    @staticmethod
    def naive_recursive(n: int) -> int:
        """Наивная рекурсивная реализация."""
        if n <= 1:
            return n
        return Fibonacci.naive_recursive(n-1) + Fibonacci.naive_recursive(n-2)
    
    @staticmethod
    def memoization_recursive(n: int, memo: Dict[int, int] = None) -> int:
        """Рекурсивная реализация с мемоизацией (нисходящий подход)."""
        if memo is None:
            memo = {}
        
        if n <= 1:
            return n
        
        if n not in memo:
            memo[n] = Fibonacci.memoization_recursive(n-1, memo) + \
                      Fibonacci.memoization_recursive(n-2, memo)
        
        return memo[n]
    
    @staticmethod
    def iterative(n: int) -> int:
        """Итеративная реализация (восходящий подход)."""
        if n <= 1:
            return n
        
        fib = [0] * (n + 1)
        fib[1] = 1
        
        for i in range(2, n + 1):
            fib[i] = fib[i-1] + fib[i-2]
        
        return fib[n]
    
    @staticmethod
    def optimized_iterative(n: int) -> int:
        """Оптимизированная итеративная реализация O(1) по памяти."""
        if n <= 1:
            return n
        
        prev, curr = 0, 1
        for _ in range(2, n + 1):
            prev, curr = curr, prev + curr
        
        return curr


class Knapsack:
    """Класс для решения задачи о рюкзаке 0-1."""
    
    @staticmethod
    def bottom_up(weights: List[int], values: List[int], capacity: int) -> Tuple[int, List[int]]:
        """
        Решение задачи о рюкзаке 0-1 восходящим подходом.
        
        Args:
            weights: веса предметов
            values: стоимости предметов
            capacity: вместимость рюкзака
            
        Returns:
            Tuple[максимальная стоимость, список выбранных предметов]
        """
        n = len(weights)
        
        # Создаем таблицу DP
        dp = [[0] * (capacity + 1) for _ in range(n + 1)]
        
        # Заполняем таблицу
        for i in range(1, n + 1):
            for w in range(1, capacity + 1):
                if weights[i-1] <= w:
                    dp[i][w] = max(dp[i-1][w], 
                                  dp[i-1][w - weights[i-1]] + values[i-1])
                else:
                    dp[i][w] = dp[i-1][w]
        
        # Восстанавливаем решение
        selected_items = []
        w = capacity
        for i in range(n, 0, -1):
            if dp[i][w] != dp[i-1][w]:
                selected_items.append(i-1)
                w -= weights[i-1]
        
        selected_items.reverse()
        
        return dp[n][capacity], selected_items
    
    @staticmethod
    def greedy_fractional(weights: List[int], values: List[int], capacity: int) -> float:
        """
        Жадный алгоритм для непрерывного рюкзака.
        Возвращает максимальную стоимость (можно брать части предметов).
        """
        # Создаем список предметов с их удельной стоимостью
        items = [(values[i] / weights[i], weights[i], values[i]) 
                for i in range(len(weights))]
        
        # Сортируем по удельной стоимости по убыванию
        items.sort(reverse=True, key=lambda x: x[0])
        
        total_value = 0.0
        remaining_capacity = capacity
        
        for density, weight, value in items:
            if remaining_capacity >= weight:
                total_value += value
                remaining_capacity -= weight
            else:
                total_value += density * remaining_capacity
                break
        
        return total_value


class LCS:
    """Класс для поиска наибольшей общей подпоследовательности."""
    
    @staticmethod
    def bottom_up(str1: str, str2: str) -> Tuple[int, str]:
        """
        Поиск LCS восходящим подходом.
        
        Args:
            str1, str2: входные строки
            
        Returns:
            Tuple[длина LCS, сама LCS]
        """
        m, n = len(str1), len(str2)
        
        # Создаем таблицу DP
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # Заполняем таблицу
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if str1[i-1] == str2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        # Восстанавливаем LCS
        lcs_chars = []
        i, j = m, n
        
        while i > 0 and j > 0:
            if str1[i-1] == str2[j-1]:
                lcs_chars.append(str1[i-1])
                i -= 1
                j -= 1
            elif dp[i-1][j] > dp[i][j-1]:
                i -= 1
            else:
                j -= 1
        
        lcs_str = ''.join(reversed(lcs_chars))
        
        return dp[m][n], lcs_str


class Levenshtein:
    """Класс для вычисления расстояния Левенштейна."""
    
    @staticmethod
    def bottom_up(str1: str, str2: str) -> int:
        """
        Вычисление расстояния Левенштейна.
        
        Args:
            str1, str2: входные строки
            
        Returns:
            Минимальное количество операций для преобразования str1 в str2
        """
        m, n = len(str1), len(str2)
        
        # Создаем таблицу DP
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # Инициализируем первую строку и столбец
        for i in range(m + 1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j
        
        # Заполняем таблицу
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if str1[i-1] == str2[j-1]:
                    cost = 0
                else:
                    cost = 1
                
                dp[i][j] = min(
                    dp[i-1][j] + 1,      # удаление
                    dp[i][j-1] + 1,      # вставка
                    dp[i-1][j-1] + cost  # замена
                )
        
        return dp[m][n]


class CoinChange:
    """Класс для решения задачи размена монет."""
    
    @staticmethod
    def min_coins(coins: List[int], amount: int) -> int:
        """
        Минимальное количество монет для заданной суммы.
        
        Args:
            coins: номиналы монет
            amount: целевая сумма
            
        Returns:
            Минимальное количество монет или -1, если невозможно
        """
        # Инициализируем массив большими значениями
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        
        # Заполняем массив DP
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], dp[i - coin] + 1)
        
        return dp[amount] if dp[amount] != float('inf') else -1
    
    @staticmethod
    def num_ways(coins: List[int], amount: int) -> int:
        """
        Количество способов разменять сумму.
        
        Args:
            coins: номиналы монет
            amount: целевая сумма
            
        Returns:
            Количество способов размена
        """
        dp = [0] * (amount + 1)
        dp[0] = 1
        
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] += dp[i - coin]
        
        return dp[amount]


class LIS:
    """Класс для поиска наибольшей возрастающей подпоследовательности."""
    
    @staticmethod
    def length(nums: List[int]) -> Tuple[int, List[int]]:
        """
        Поиск длины LIS и восстановление последовательности.
        
        Args:
            nums: входная последовательность
            
        Returns:
            Tuple[длина LIS, сама LIS]
        """
        if not nums:
            return 0, []
        
        n = len(nums)
        
        # dp[i] - длина LIS, заканчивающейся в позиции i
        dp = [1] * n
        # prev[i] - индекс предыдущего элемента в LIS
        prev = [-1] * n
        
        # Заполняем массивы DP
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i] and dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    prev[i] = j
        
        # Находим максимальную длину и её индекс
        max_len = max(dp)
        max_idx = dp.index(max_len)
        
        # Восстанавливаем LIS
        lis = []
        idx = max_idx
        while idx != -1:
            lis.append(nums[idx])
            idx = prev[idx]
        
        lis.reverse()
        
        return max_len, lis