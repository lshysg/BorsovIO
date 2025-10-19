# search_comparison.py
import timeit
import random
import matplotlib.pyplot as plt
import bisect

# ----------------------------------------------------------
# 1. Реализация линейного поиска
# ----------------------------------------------------------

def linear_search(arr, target):
    """
    Линейный поиск элемента в массиве.
    Возвращает индекс элемента, если найден, иначе -1.
    Сложность: O(n)
    """
    for i in range(len(arr)):  # O(n) — цикл по всем элементам массива
        if arr[i] == target:   # O(1) — сравнение
            return i           # O(1) — возврат результата
    return -1                  # O(1)
    # Общая сложность: O(n)


# ----------------------------------------------------------
# 2. Реализация бинарного поиска
# ----------------------------------------------------------

def binary_search(arr, target):
    """
    Бинарный поиск элемента в отсортированном массиве.
    Возвращает индекс элемента, если найден, иначе -1.
    Сложность: O(log n)
    """
    left = 0           # O(1)
    right = len(arr) - 1  # O(1)
    while left <= right:  # O(log n) — деление диапазона пополам
        mid = (left + right) // 2  # O(1)
        if arr[mid] == target:     # O(1)
            return mid             # O(1)
        elif arr[mid] < target:    # O(1)
            left = mid + 1         # O(1)
        else:
            right = mid - 1        # O(1)
    return -1                      # O(1)
    # Общая сложность: O(log n)


# ----------------------------------------------------------
# 3. Функция для измерения времени
# ----------------------------------------------------------

def measure_time(func, arr, target, repeats=10):
    """
    Измеряет среднее время выполнения функции поиска.
    Возвращает время в миллисекундах.
    """
    total_time = timeit.timeit(lambda: func(arr, target), number=repeats)
    avg_time_ms = (total_time / repeats) * 1000
    return avg_time_ms


# ----------------------------------------------------------
# 4. Подготовка данных и эксперимент
# ----------------------------------------------------------

def run_experiment():
    sizes = [1000, 5000, 10000, 50000, 100000, 500000, 1000000]
    linear_times = []
    binary_times = []

    print("Характеристики ПК для тестирования:")
    print("- Процессор: Intel Core i5-4460 @ 3.20GHz")
    print("- ОЗУ: 8 GB DDR3")
    print("- ОС: Windows 10")
    print("- Python: 3.13.5\n")

    print("{:>10} {:>15} {:>15}".format("Размер", "Линейный поиск (мс)", "Бинарный поиск (мс)"))
    print("-" * 45)

    for n in sizes:
        arr = sorted(random.sample(range(n * 2), n))  # создаём отсортированный массив
        target = random.choice(arr)  # выбираем существующий элемент

        # Замер линейного поиска
        lin_time = measure_time(linear_search, arr, target)
        # Замер бинарного поиска
        bin_time = measure_time(binary_search, arr, target)

        linear_times.append(lin_time)
        binary_times.append(bin_time)

        print(f"{n:>10} {lin_time:>15.4f} {bin_time:>15.4f}")

    # ------------------------------------------------------
    # 5. Визуализация результатов
    # ------------------------------------------------------
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, linear_times, 'o-', label='Линейный поиск O(n)')
    plt.plot(sizes, binary_times, 's-', label='Бинарный поиск O(log n)')
    plt.xlabel("Размер массива (n)")
    plt.ylabel("Среднее время (мс)")
    plt.title("Сравнение времени выполнения линейного и бинарного поиска")
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend()
    plt.savefig('search_time_linear_scale.png', dpi=300, bbox_inches='tight')
    plt.show()

    # Логарифмический масштаб
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, linear_times, 'o-', label='O(n)')
    plt.plot(sizes, binary_times, 's-', label='O(log n)')
    plt.xscale('log')
    plt.yscale('log')
    plt.xlabel("Размер массива (log n)")
    plt.ylabel("Время выполнения (log мс)")
    plt.title("Сравнение в логарифмическом масштабе")
    plt.grid(True, which='both', linestyle='--', alpha=0.6)
    plt.legend()
    plt.savefig('search_time_log_scale.png', dpi=300, bbox_inches='tight')
    plt.show()

    # ------------------------------------------------------
    # 6. Анализ результатов
    # ------------------------------------------------------
    print("\nАнализ результатов:")
    print("1. Линейный поиск демонстрирует рост времени ~O(n) — при увеличении размера массива в 10 раз,")
    print("   время выполнения увеличивается примерно во столько же раз.")
    print("2. Бинарный поиск показывает логарифмический рост — увеличение размера массива почти не влияет на время.")
    print("3. Небольшие отклонения возможны из-за системных факторов и случайного выбора целевого элемента.")
    print("4. Эксперимент подтверждает теоретические оценки O(n) и O(log n).")


# ----------------------------------------------------------
# Запуск эксперимента
# ----------------------------------------------------------

if __name__ == "__main__":
    run_experiment()
