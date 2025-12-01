import matplotlib.pyplot as plt
from performance_test import run_tests, DATA_SIZES

def plot_results():
    results = run_tests()

    # --- график зависимости времени от размера массива (случайные данные) ---
    data = results["random"]

    plt.figure(figsize=(10, 6))
    for sort_name in data[100].keys():
        times = [data[n][sort_name] for n in DATA_SIZES]
        plt.plot(DATA_SIZES, times, marker='o', label=sort_name)

    plt.title("Производительность сортировок (random data)")
    plt.xlabel("Размер массива")
    plt.ylabel("Время (сек)")
    plt.legend()
    plt.grid(True)
    plt.show()

    # --- график времени от типа данных для n=5000 ---
    n = 5000
    plt.figure(figsize=(10, 6))
    for sort_name in results["random"][n]:
        values = [
            results[tp][n][sort_name]
            for tp in ["random", "sorted", "reversed", "almost_sorted"]
        ]
        plt.plot(["random", "sorted", "reversed", "almost_sorted"],
                 values, marker='o', label=sort_name)

    plt.title(f"Зависимость времени от типа данных (n={n})")
    plt.xlabel("Тип данных")
    plt.ylabel("Время (сек)")
    plt.legend()
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    plot_results()
