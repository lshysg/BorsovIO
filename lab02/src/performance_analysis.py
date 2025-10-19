import timeit
from collections import deque
import matplotlib.pyplot as plt
from linked_list import LinkedList

REPEAT = 10  # количество повторов для timeit
sizes = [100, 500, 1000, 2000, 5000]  # размеры теста

# ------------------ Функции для замеров ------------------
def test_insert_start_list(n):
    """
    Вставка n элементов в начало списка (list)
    """
    lst = []
    for i in range(n):
        lst.insert(0, i)
    # Сложность: O(n^2) - каждая вставка в начало списка list требует сдвига всех элементов

def test_insert_start_linkedlist(n):
    """
    Вставка n элементов в начало связного списка (LinkedList)
    """
    ll = LinkedList()
    for i in range(n):
        ll.insert_at_start(i)
    # Сложность: O(n) - каждая вставка O(1), всего n вставок

def test_queue_list(n):
    """
    Удаление n элементов с начала списка (list)
    """
    lst = list(range(n))
    for _ in range(n):
        lst.pop(0)
    # Сложность: O(n^2) - pop(0) сдвигает все оставшиеся элементы на каждом шаге

def test_queue_deque(n):
    """
    Удаление n элементов с начала двусторонней очереди (deque)
    """
    q = deque(range(n))
    for _ in range(n):
        q.popleft()
    # Сложность: O(n) - popleft() выполняется за O(1) для каждого элемента

# ------------------ Замеры вставки в начало ------------------
list_start_times = []
ll_start_times = []

for n in sizes:
    t_list = timeit.timeit(lambda: test_insert_start_list(n), number=REPEAT)
    t_ll = timeit.timeit(lambda: test_insert_start_linkedlist(n), number=REPEAT)
    list_start_times.append(t_list)
    ll_start_times.append(t_ll)

print("Вставка в начало:")
for i, n in enumerate(sizes):
    print(f"{n} элементов -> list: {list_start_times[i]:.6f}, LinkedList: {ll_start_times[i]:.6f}")

# ------------------ Замеры очереди (удаление из начала) ------------------
list_queue_times = []
deque_times = []

for n in sizes:
    t_list = timeit.timeit(lambda: test_queue_list(n), number=REPEAT)
    t_deque = timeit.timeit(lambda: test_queue_deque(n), number=REPEAT)
    list_queue_times.append(t_list)
    deque_times.append(t_deque)

print("\nОчередь (удаление из начала):")
for i, n in enumerate(sizes):
    print(f"{n} элементов -> list pop(0): {list_queue_times[i]:.6f}, deque popleft(): {deque_times[i]:.6f}")

# ------------------ Визуализация ------------------
# Вставка в начало
plt.figure(figsize=(8,5))
plt.plot(sizes, list_start_times, marker='o', label='list insert(0, item)')
plt.plot(sizes, ll_start_times, marker='o', label='LinkedList insert_at_start')
plt.xlabel('Количество элементов')
plt.ylabel('Время (сек)')
plt.title('Вставка в начало: list vs LinkedList')
plt.legend()
plt.grid(True)
plt.show()

# Очередь
plt.figure(figsize=(8,5))
plt.plot(sizes, list_queue_times, marker='o', label='list pop(0)')
plt.plot(sizes, deque_times, marker='o', label='deque popleft()')
plt.xlabel('Количество элементов')
plt.ylabel('Время (сек)')
plt.title('Очередь: list vs deque')
plt.legend()
plt.grid(True)
plt.show()
