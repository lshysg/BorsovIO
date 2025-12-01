from time import time

calls_naive = 0

def fibonacci_naive(n):
    """
    Наивная рекурсивная функция Фибоначчи.
    """
    global calls_naive
    calls_naive += 1  # O(1)

    if n <= 1:     # O(1)
        return n   # O(1)

    # Рекурсивные вызовы — экспоненциальные:
    return fibonacci_naive(n - 1) + fibonacci_naive(n - 2)  # O(1)

    # Итоговая сложность: O(2^n)
    # Глубина рекурсии: O(n)


calls_memo = 0
memo = {}

def fibonacci_memo(n):
    """
    Мемоизированная функция Фибоначчи.
    """
    global calls_memo, memo
    calls_memo += 1  # O(1)

    if n in memo:    # O(1)
        return memo[n]  # O(1)

    if n <= 1:       # O(1)
        memo[n] = n  # O(1)
    else:
        memo[n] = fibonacci_memo(n - 1) + fibonacci_memo(n - 2)  # O(1)

    return memo[n]  # O(1)

    # Итоговая сложность: O(n)
    # Глубина рекурсии: O(n)
