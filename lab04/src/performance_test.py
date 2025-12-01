import timeit
from sorts import *
from generate_data import *

DATA_SIZES = [100, 1000, 5000, 10000]

SORT_FUNCTIONS = {
    "Bubble": bubble_sort,
    "Selection": selection_sort,
    "Insertion": insertion_sort,
    "Merge": merge_sort,
    "Quick": quick_sort
}

DATA_TYPES = {
    "random": generate_random,
    "sorted": generate_sorted,
    "reversed": generate_reversed,
    "almost_sorted": generate_almost_sorted
}

def run_tests():
    results = {}

    for data_type_name, generator in DATA_TYPES.items():
        print(f"\n=== Тип данных: {data_type_name} ===")
        results[data_type_name] = {}

        for n in DATA_SIZES:
            print(f"\nРазмер: {n}")
            base_data = generator(n)

            results[data_type_name][n] = {}

            for sort_name, sort_func in SORT_FUNCTIONS.items():
                data_copy = base_data[:]  # копия

                t = timeit.timeit(
                    stmt=lambda: sort_func(data_copy),
                    number=1
                )

                results[data_type_name][n][sort_name] = t
                print(f"{sort_name:10s} -> {t:.4f} сек")

    return results


if __name__ == "__main__":
    run_tests()
