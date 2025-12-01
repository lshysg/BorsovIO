"""
Открытая адресация (линейное пробирование и двойное хеширование).
"""

from hash_functions import hash_sum, hash_poly


class HashTableOpenAddressing:
    EMPTY = object()
    DELETED = object()

    def __init__(self, capacity=8, method='linear'):
        self.capacity = capacity                 # O(1)
        self.table = [self.EMPTY] * capacity     # O(n)
        self.size = 0                            # O(1)
        self.method = method                     # 'linear' | 'double'

    def _hash1(self, key: str) -> int:
        return hash_sum(key) % self.capacity     # O(1)

    def _hash2(self, key: str) -> int:
        """Для double hashing"""
        return hash_poly(key) % (self.capacity - 1) + 1  # O(1)

    def _probe(self, key, i):
        """
        Функция пробирования.
        Линейное: (h + i) % m
        Двойное: (h1 + i * h2) % m
        O(1)
        """
        if self.method == 'linear':
            return (self._hash1(key) + i) % self.capacity  # O(1)
        else:
            return (self._hash1(key) + i * self._hash2(key)) % self.capacity  # O(1)

    def insert(self, key, value):
        """
        Вставка.
        Среднее: O(1)
        Худшее: O(n) — при длинных последовательностях пробирования
        """
        if self.size / self.capacity > 0.7:  # O(1)
            self._resize()                   # O(n)

        for i in range(self.capacity):    # O(n) worst
            idx = self._probe(key, i)     # O(1)
            slot = self.table[idx]        # O(1)

            if slot is self.EMPTY or slot is self.DELETED:  # O(1)
                self.table[idx] = (key, value)  # O(1)
                self.size += 1                  # O(1)
                return

            if slot[0] == key:       # O(1)
                self.table[idx] = (key, value)  # обновление
                return

        raise RuntimeError("HashTable is full")

    def get(self, key):
        """
        Поиск.
        Среднее: O(1)
        Худшее: O(n)
        """
        for i in range(self.capacity):   # O(n) worst
            idx = self._probe(key, i)    # O(1)
            slot = self.table[idx]       # O(1)

            if slot is self.EMPTY:       # O(1)
                return None

            if slot is not self.DELETED and slot[0] == key:  # O(1)
                return slot[1]

        return None

    def delete(self, key):
        """
        Удаление.
        Среднее: O(1)
        Худшее: O(n)
        """
        for i in range(self.capacity):  # O(n)
            idx = self._probe(key, i)
            slot = self.table[idx]

            if slot is self.EMPTY:
                return False

            if slot is not self.DELETED and slot[0] == key:
                self.table[idx] = self.DELETED
                self.size -= 1
                return True
        return False

    def _resize(self):
        """
        Увеличение массива.
        Амортизированно: O(1)
        Факт вызова: O(n)
        """
        old_table = self.table
        self.capacity *= 2                 # O(1)
        self.table = [self.EMPTY] * self.capacity  # O(n)
        self.size = 0                      # O(1)

        for slot in old_table:             # O(n)
            if slot not in (self.EMPTY, self.DELETED):
                self.insert(*slot)         # O(1) амортиз.
