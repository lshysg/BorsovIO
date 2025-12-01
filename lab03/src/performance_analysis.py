import time
import matplotlib.pyplot as plt
from memoization import fibonacci_naive, fibonacci_memo, memo, calls_memo, calls_naive

def measure_times(max_n=35):
    naive_times = []
    memo_times = []
    sizes = list(range(5, max_n + 1))

    for n in sizes:
        global calls_naive, calls_memo, memo
        calls_naive = 0
        t1 = time.time()
        fibonacci_naive(n)
        t2 = time.time()
        naive_times.append(t2 - t1)

        calls_memo = 0
        memo = {}
        t3 = time.time()
        fibonacci_memo(n)
        t4 = time.time()
        memo_times.append(t4 - t3)

    plt.figure(figsize=(8,5))
    plt.plot(sizes, naive_times, marker='o', label='Наивная рекурсия')
    plt.plot(sizes, memo_times, marker='o', label='Мемоизация')
    plt.xlabel('n')
    plt.ylabel('Время (сек)')
    plt.title('Время вычисления Фибоначчи: рекурсия vs мемоизация')
    plt.legend()
    plt.grid(True)
    plt.show()


# Пример использования Ханойских башен
# hanoi(3, 'A', 'C', 'B')


if __name__ == "__main__":
    measure_times(35)