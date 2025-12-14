"""
Реализация структуры данных "Куча" (Heap)
"""

class MinHeap:
    """
    Min-Heap реализация на основе массива
    """
    
    def __init__(self, array=None):
        """
        Инициализация кучи
        Сложность: O(n) если передан массив, O(1) иначе
        """
        self.heap = []
        if array:
            self.build_heap(array)
    
    def _parent_index(self, index):
        """Возвращает индекс родителя"""
        return (index - 1) // 2
    
    def _left_child_index(self, index):
        """Возвращает индекс левого потомка"""
        return 2 * index + 1
    
    def _right_child_index(self, index):
        """Возвращает индекс правого потомка"""
        return 2 * index + 2
    
    def _has_parent(self, index):
        """Проверяет, есть ли родитель у узла"""
        return self._parent_index(index) >= 0
    
    def _has_left_child(self, index):
        """Проверяет, есть ли левый потомок"""
        return self._left_child_index(index) < len(self.heap)
    
    def _has_right_child(self, index):
        """Проверяет, есть ли правый потомок"""
        return self._right_child_index(index) < len(self.heap)
    
    def _swap(self, i, j):
        """Меняет местами элементы с индексами i и j"""
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
    
    def _sift_up(self, index):
        """
        Всплытие элемента (проталкивание вверх)
        Сложность: O(log n)
        """
        while self._has_parent(index) and self.heap[index] < self.heap[self._parent_index(index)]:
            parent_idx = self._parent_index(index)
            self._swap(index, parent_idx)
            index = parent_idx
    
    def _sift_down(self, index):
        """
        Погружение элемента (проталкивание вниз)
        Сложность: O(log n)
        """
        while self._has_left_child(index):
            # Находим индекс минимального потомка
            min_child_idx = self._left_child_index(index)
            if (self._has_right_child(index) and 
                self.heap[self._right_child_index(index)] < self.heap[min_child_idx]):
                min_child_idx = self._right_child_index(index)
            
            # Если текущий элемент меньше минимального потомка, свойство кучи восстановлено
            if self.heap[index] < self.heap[min_child_idx]:
                break
            
            # Меняем местами с минимальным потомком
            self._swap(index, min_child_idx)
            index = min_child_idx
    
    def insert(self, value):
        """
        Вставка элемента в кучу
        Сложность: O(log n)
        """
        self.heap.append(value)  # Добавляем в конец
        self._sift_up(len(self.heap) - 1)  # Восстанавливаем свойство кучи
    
    def extract(self):
        """
        Извлечение минимального элемента (корня)
        Сложность: O(log n)
        """
        if not self.heap:
            raise IndexError("Куча пуста")
        
        if len(self.heap) == 1:
            return self.heap.pop()
        
        root = self.heap[0]
        # Перемещаем последний элемент в корень
        self.heap[0] = self.heap.pop()
        # Восстанавливаем свойство кучи
        self._sift_down(0)
        
        return root
    
    def peek(self):
        """
        Просмотр минимального элемента без извлечения
        Сложность: O(1)
        """
        if not self.heap:
            raise IndexError("Куча пуста")
        return self.heap[0]
    
    def build_heap(self, array):
        """
        Построение кучи из произвольного массива
        Сложность: O(n)
        """
        self.heap = array[:]
        # Начинаем с последнего нелистового узла и идем к корню
        start_idx = len(self.heap) // 2 - 1
        
        for i in range(start_idx, -1, -1):
            self._sift_down(i)
    
    def heapify(self):
        """Альтернативное название для build_heap"""
        self.build_heap(self.heap)
    
    def size(self):
        """Возвращает размер кучи"""
        return len(self.heap)
    
    def is_empty(self):
        """Проверяет, пуста ли куча"""
        return len(self.heap) == 0
    
    def __str__(self):
        """Строковое представление кучи"""
        return str(self.heap)
    
    def print_tree(self):
        """
        Визуализация кучи в виде дерева
        """
        if not self.heap:
            print("Куча пуста")
            return
        
        height = self._calculate_height()
        max_width = 2 ** height
        lines = []
        
        for level in range(height):
            start = 2 ** level - 1
            end = min(start * 2 + 1, len(self.heap))
            nodes = self.heap[start:end]
            
            # Вычисляем отступы для красивого отображения
            spacing = max_width // (2 ** level)
            line = " " * (spacing // 2)
            
            for node in nodes:
                line += f"{node:^{spacing}}"
                line += " " * (spacing // 2)
            
            lines.append(line)
        
        for line in lines:
            print(line)
    
    def _calculate_height(self):
        """Вычисляет высоту дерева"""
        n = len(self.heap)
        height = 0
        while 2 ** height - 1 < n:
            height += 1
        return height
    
    def validate(self):
        """
        Проверяет свойство min-heap
        Возвращает True если свойство выполняется
        """
        for i in range(len(self.heap)):
            left = self._left_child_index(i)
            right = self._right_child_index(i)
            
            if left < len(self.heap) and self.heap[i] > self.heap[left]:
                return False
            if right < len(self.heap) and self.heap[i] > self.heap[right]:
                return False
        
        return True


class MaxHeap:
    """
    Max-Heap реализация на основе массива
    """
    
    def __init__(self, array=None):
        self.heap = []
        if array:
            self.build_heap(array)
    
    def _parent_index(self, index):
        return (index - 1) // 2
    
    def _left_child_index(self, index):
        return 2 * index + 1
    
    def _right_child_index(self, index):
        return 2 * index + 2
    
    def _has_parent(self, index):
        return self._parent_index(index) >= 0
    
    def _has_left_child(self, index):
        return self._left_child_index(index) < len(self.heap)
    
    def _has_right_child(self, index):
        return self._right_child_index(index) < len(self.heap)
    
    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
    
    def _sift_up(self, index):
        """Всплытие для max-heap"""
        while self._has_parent(index) and self.heap[index] > self.heap[self._parent_index(index)]:
            parent_idx = self._parent_index(index)
            self._swap(index, parent_idx)
            index = parent_idx
    
    def _sift_down(self, index):
        """Погружение для max-heap"""
        while self._has_left_child(index):
            max_child_idx = self._left_child_index(index)
            if (self._has_right_child(index) and 
                self.heap[self._right_child_index(index)] > self.heap[max_child_idx]):
                max_child_idx = self._right_child_index(index)
            
            if self.heap[index] > self.heap[max_child_idx]:
                break
            
            self._swap(index, max_child_idx)
            index = max_child_idx
    
    def insert(self, value):
        self.heap.append(value)
        self._sift_up(len(self.heap) - 1)
    
    def extract(self):
        if not self.heap:
            raise IndexError("Куча пуста")
        
        if len(self.heap) == 1:
            return self.heap.pop()
        
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._sift_down(0)
        
        return root
    
    def peek(self):
        if not self.heap:
            raise IndexError("Куча пуста")
        return self.heap[0]
    
    def build_heap(self, array):
        self.heap = array[:]
        start_idx = len(self.heap) // 2 - 1
        
        for i in range(start_idx, -1, -1):
            self._sift_down(i)
    
    def size(self):
        return len(self.heap)
    
    def is_empty(self):
        return len(self.heap) == 0
    
    def __str__(self):
        return str(self.heap)