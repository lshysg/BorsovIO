def factorial(n):
    """
    Рекурсивное вычисление факториала n!
    """
    if n == 0 or n == 1:   # O(1)
        return 1           # O(1)

    return n * factorial(n - 1)  # O(1) операция умножения + O(n-1) рекурсивный вызов

    # Итоговая сложность: O(n)
    # Глубина рекурсии: O(n)


def fibonacci(n):
    """
    Наивная рекурсивная функция Фибоначчи.
    """
    if n <= 1:     # O(1)
        return n   # O(1)

    # Два рекурсивных вызова:
    # fibonacci(n - 1) — O(2^(n-1))
    # fibonacci(n - 2) — O(2^(n-2))
    return fibonacci(n - 1) + fibonacci(n - 2)  # O(1) операция сложения

    # Итоговая сложность: O(2^n)
    # Глубина рекурсии: O(n)


def fast_power(a, n):
    """
    Быстрое возведение числа a в степень n.
    """
    if n == 0:     # O(1)
        return 1   # O(1)

    if n % 2 == 0:            # O(1)
        half = fast_power(a, n // 2)  # O(log n)
        return half * half    # O(1)
    else:
        return a * fast_power(a, n - 1)  # O(1) + O(log n)

    # Итоговая сложность: O(log n)
    # Глубина рекурсии: O(log n)



if __name__ == "__main__":
    # Факториал
    print("factorial(5) =", factorial(5))          # 120
    print("factorial(1) =", factorial(1))          # 1
    print("factorial(0) =", factorial(0))          # 1

    # Фибоначчи (наивная версия — медленная!)
    print("fibonacci(10) =", fibonacci(10))        # 55
    print("fibonacci(5) =", fibonacci(5))          # 5

    # Быстрое возведение в степень
    print("fast_power(2, 10) =", fast_power(2, 10))  # 1024
    print("fast_power(3, 5) =", fast_power(3, 5))    # 243
    print("fast_power(10, 0) =", fast_power(10, 0))  # 1