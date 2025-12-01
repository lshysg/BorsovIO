"""
Файл: hash_functions.py
Содержит несколько хеш-функций для строковых ключей.
"""

def hash_sum(s: str) -> int:
    """
    Простая хеш-функция: сумма кодов символов
    Среднее качество распределения
    Сложность: O(n)
    """
    h = 0              # O(1)
    for ch in s:       # O(n)
        h += ord(ch)   # O(1)
    return h           # O(1)


def hash_poly(s: str, p: int = 53, mod: int = 2**64) -> int:
    """
    Полиномиальный хеш
    Хорошее распределение
    Сложность: O(n)
    """
    h = 0                 # O(1)
    power = 1             # O(1)
    for ch in s:          # O(n)
        h = (h + ord(ch) * power) % mod   # O(1)
        power = (power * p) % mod         # O(1)
    return h               # O(1)


def hash_djb2(s: str) -> int:
    """
    Классическая хеш-функция DJB2
    Хорошее распределение, часто используется
    Сложность: O(n)
    """
    h = 5381            # O(1)
    for ch in s:        # O(n)
        h = ((h << 5) + h) + ord(ch)   # h * 33 + ord — O(1)
    return h            # O(1)
