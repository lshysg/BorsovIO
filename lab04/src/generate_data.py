import random

def generate_random(n):
    return [random.randint(0, 1000000) for _ in range(n)]

def generate_sorted(n):
    return list(range(n))

def generate_reversed(n):
    return list(range(n, 0, -1))

def generate_almost_sorted(n, shuffle_percent=5):
    arr = list(range(n))
    k = n * shuffle_percent // 100
    for _ in range(k):
        i = random.randint(0, n - 1)
        j = random.randint(0, n - 1)
        arr[i], arr[j] = arr[j], arr[i]
    return arr
