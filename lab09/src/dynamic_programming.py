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
        """
        Наивная рекурсивная реализация.
        
        Временная сложность: O(2^n) - экспоненциальная
        Пространственная сложность: O(n) - глубина стека рекурсии
        """
        if n <= 1:
            return n
        return Fibonacci.naive_recursive(n-1) + Fibonacci.naive_recursive(n-2)
    
    @staticmethod
    def memoization_recursive(n: int, memo: Dict[int, int] = None) -> int:
        """
        Рекурсивная реализация с мемоизацией (нисходящий подход).
        
        Временная сложность: O(n) - линейная
        Пространственная сложность: O(n) - для хранения memo и стека рекурсии
        """
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
        """
        Итеративная реализация (восходящий подход).
        
        Временная сложность: O(n) - линейная
        Пространственная сложность: O(n) - массив размера n+1
        """
        if n <= 1:
            return n
        
        fib = [0] * (n + 1)
        fib[1] = 1
        
        for i in range(2, n + 1):
            fib[i] = fib[i-1] + fib[i-2]
        
        return fib[n]
    
    @staticmethod
    def optimized_iterative(n: int) -> int:
        """
        Оптимизированная итеративная реализация O(1) по памяти.
        
        Временная сложность: O(n) - линейная
        Пространственная сложность: O(1) - константная, используем только 2 переменные
        """
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
        
        Временная сложность: O(n * capacity), где n - количество предметов
        Пространственная сложность: O(n * capacity) - двумерная таблица
        Можно оптимизировать до O(capacity) используя только один массив
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
        
        Временная сложность: O(n log n) - сортировка по удельной стоимости
        Пространственная сложность: O(n) - хранение отсортированного списка
        
        Примечание: Для задачи 0-1 рюкзака жадный алгоритм не всегда дает оптимальное решение
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
        
        Временная сложность: O(m * n), где m = len(str1), n = len(str2)
        Пространственная сложность: O(m * n) - двумерная таблица
        Можно оптимизировать до O(min(m, n)) используя только две строки
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
        
        Временная сложность: O(m * n), где m = len(str1), n = len(str2)
        Пространственная сложность: O(m * n) - двумерная таблица
        Можно оптимизировать до O(min(m, n)) используя два массива
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
        
        Временная сложность: O(amount * n), где n - количество номиналов
        Пространственная сложность: O(amount) - массив размера amount+1
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
        
        Временная сложность: O(amount * n), где n - количество номиналов
        Пространственная сложность: O(amount) - массив размера amount+1
        
        Важно: Вариант с подсчетом количества способов отличается от варианта
        с минимальным количеством монет. Здесь мы используем += вместо min()
        """
        dp = [0] * (amount + 1)
        dp[0] = 1
        
        # Внешний цикл по монетам, а не по сумме, чтобы избежать дублирования
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
        
        Временная сложность: O(n^2) - два вложенных цикла
        Пространственная сложность: O(n) - два массива размера n
        
        Оптимизация: можно использовать бинарный поиск для достижения O(n log n)
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
    
    @staticmethod
    def length_optimized(nums: List[int]) -> Tuple[int, List[int]]:
        """
        Оптимизированная версия LIS с использованием бинарного поиска.
        
        Временная сложность: O(n log n) - основной цикл + бинарный поиск
        Пространственная сложность: O(n) - дополнительные массивы
        """
        if not nums:
            return 0, []
        
        n = len(nums)
        # tails[i] - минимальный возможный последний элемент LIS длины i+1
        tails = []
        # indices[i] - индекс элемента в nums, который является последним в LIS длины i+1
        indices = []
        # prev[i] - индекс предыдущего элемента в LIS для элемента nums[i]
        prev = [-1] * n
        
        for i, num in enumerate(nums):
            # Бинарный поиск позиции для вставки
            left, right = 0, len(tails)
            while left < right:
                mid = (left + right) // 2
                if tails[mid] < num:
                    left = mid + 1
                else:
                    right = mid
            
            if left == len(tails):
                tails.append(num)
                indices.append(i)
            else:
                tails[left] = num
                indices[left] = i
            
            if left > 0:
                prev[i] = indices[left - 1]
        
        # Восстанавливаем LIS
        length = len(tails)
        lis = []
        idx = indices[-1]
        for _ in range(length):
            lis.append(nums[idx])
            idx = prev[idx]
        
        lis.reverse()
        
        return length, lis