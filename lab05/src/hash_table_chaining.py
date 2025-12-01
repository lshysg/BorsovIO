"""
Хеш-таблица с методом цепочек.
"""

from hash_functions import hash_djb2

class HashTableChaining:
    def __init__(self, capacity=8):
        self.capacity = capacity             # O(1)
        self.table = [[] for _ in range(capacity)]  # O(n)
        self.size = 0                        # O(1)

    def _hash(self, key: str) -> int:
        """
        Вычисление индекса.
        O(1) амортизированно
        """
        return hash_djb2(key) % self.capacity  # O(1)

    def insert(self, key, value):
        """
        Вставка в цепочку.
        Среднее: O(1)
        Худшее: O(n) — если все ключи в одной корзине
        """
        idx = self._hash(key)     # O(1)
        bucket = self.table[idx]  # O(1)

        for i, (k, v) in enumerate(bucket):  # O(chain_length)
            if k == key:                     # O(1)
                bucket[i] = (key, value)     # O(1)
                return

        bucket.append((key, value))  # O(1)
        self.size += 1               # O(1)

        if self.size / self.capacity > 0.75:  # O(1)
            self._resize()                    # O(n)

    def get(self, key):
        """
        Поиск.
        Среднее: O(1)
        Худшее: O(n)
        """
        idx = self._hash(key)      # O(1)
        for k, v in self.table[idx]:  # O(chain_length)
            if k == key:              # O(1)
                return v
        return None

    def delete(self, key):
        """
        Удаление.
        Среднее: O(1)
        Худшее: O(n)
        """
        idx = self._hash(key)      # O(1)
        bucket = self.table[idx]

        for i, (k, v) in enumerate(bucket):  # O(chain_length)
            if k == key:                     # O(1)
                bucket.pop(i)                # O(1)
                self.size -= 1
                return True
        return False

    def _resize(self):
        """
        Увеличение размера таблицы в 2 раза.
        Амортизированная сложность: O(1)
        Фактический вызов: O(n)
        """
        old_table = self.table
        self.capacity *= 2               # O(1)
        self.table = [[] for _ in range(self.capacity)]  # O(n)

        for bucket in old_table:         # O(n)
            for k, v in bucket:          # O(chain_length)
                self.insert(k, v)        # O(1) амортиз.
