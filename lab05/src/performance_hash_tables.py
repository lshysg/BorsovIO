import time
import random
import string

from hash_table_chaining import HashTableChaining
from hash_table_open_addressing import HashTableOpenAddressing
from hash_functions import hash_sum, hash_poly, hash_djb2



def generate_keys(n):
    """
    Генерирует случайные строки длиной 8.
    O(n)
    """
    keys = []
    for _ in range(n):                     # O(n)
        s = ''.join(random.choice(string.ascii_letters) for _ in range(8))  # O(1)
        keys.append(s)
    return keys                             # O(1)



def count_collisions(func, keys, capacity=1024):
    """
    Подсчитать количество коллизий для хеш-функции.
    Сложность: O(n)
    """
    seen = [0] * capacity
    collisions = 0

    for k in keys:                           # O(n)
        h = func(k) % capacity               # O(1)
        if seen[h] > 0:                      # O(1)
            collisions += 1
        seen[h] += 1

    return collisions



def measure_operations(ht_class, size, method=None):
    """
    Выполняет 3 операции: вставка, поиск, удаление.
    Возвращает времена.
    Сложность:
        вставка — O(n)
        поиск —  O(n)
        удаление — O(n)
    (так как по одному полному проходу)
    """
    keys = generate_keys(size)
    ht = ht_class() if method is None else ht_class(method=method)

    # ---- INSERT ----
    start = time.perf_counter()
    for k in keys:         # O(n)
        ht.insert(k, 123)  # O(1) average
    t_insert = time.perf_counter() - start

    # ---- SEARCH ----
    start = time.perf_counter()
    for k in keys:         # O(n)
        ht.get(k)          # O(1) average
    t_search = time.perf_counter() - start

    # ---- DELETE ----
    start = time.perf_counter()
    for k in keys:         # O(n)
        ht.delete(k)       # O(1) average
    t_delete = time.perf_counter() - start

    return t_insert, t_search, t_delete



def run_benchmarks():
    sizes = [1000, 5000, 10000]

    # Хеш-функции
    keys = generate_keys(50000)

    collisions = {
        "sum": count_collisions(hash_sum, keys),
        "poly": count_collisions(hash_poly, keys),
        "djb2": count_collisions(hash_djb2, keys)
    }

    print("\n=== Коллизии хеш-функций (50k ключей) ===")
    for name, col in collisions.items():
        print(f"{name:<5} -> {col}")

    print("\n=== Тестирование структур ===")
    for n in sizes:
        print(f"\nРазмер: {n}")

        # chaining
        t_ins, t_get, t_del = measure_operations(HashTableChaining, n)
        print(f"Chaining            → insert={t_ins:.4f}s  get={t_get:.4f}s  del={t_del:.4f}s")

        # linear probing
        t_ins, t_get, t_del = measure_operations(HashTableOpenAddressing, n, method="linear")
        print(f"OpenAddress (linear)→ insert={t_ins:.4f}s  get={t_get:.4f}s  del={t_del:.4f}s")

        # double hashing
        t_ins, t_get, t_del = measure_operations(HashTableOpenAddressing, n, method="double")
        print(f"OpenAddress (double)→ insert={t_ins:.4f}s  get={t_get:.4f}s  del={t_del:.4f}s")


if __name__ == "__main__":
    run_benchmarks()
