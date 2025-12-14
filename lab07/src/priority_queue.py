"""
Реализация приоритетной очереди на основе кучи
"""

class PriorityItem:
    """
    Элемент приоритетной очереди
    """
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority
    
    def __lt__(self, other):
        # Для min-heap: меньший приоритет = более высокий приоритет
        return self.priority < other.priority
    
    def __gt__(self, other):
        return self.priority > other.priority
    
    def __eq__(self, other):
        return self.priority == other.priority
    
    def __repr__(self):
        return f"({self.value}, приоритет: {self.priority})"


class PriorityQueue:
    """
    Приоритетная очередь на основе min-heap
    Элементы с меньшим приоритетом имеют более высокий приоритет
    """
    
    def __init__(self):
        self.heap = []
    
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
        """Всплытие элемента"""
        while (self._has_parent(index) and 
               self.heap[index] < self.heap[self._parent_index(index)]):
            parent_idx = self._parent_index(index)
            self._swap(index, parent_idx)
            index = parent_idx
    
    def _sift_down(self, index):
        """Погружение элемента"""
        while self._has_left_child(index):
            min_child_idx = self._left_child_index(index)
            if (self._has_right_child(index) and 
                self.heap[self._right_child_index(index)] < self.heap[min_child_idx]):
                min_child_idx = self._right_child_index(index)
            
            if self.heap[index] < self.heap[min_child_idx]:
                break
            
            self._swap(index, min_child_idx)
            index = min_child_idx
    
    def enqueue(self, value, priority):
        """
        Добавление элемента в очередь с заданным приоритетом
        
        Args:
            value: значение элемента
            priority: приоритет (меньше = выше приоритет)
        
        Сложность: O(log n)
        """
        item = PriorityItem(value, priority)
        self.heap.append(item)
        self._sift_up(len(self.heap) - 1)
    
    def dequeue(self):
        """
        Извлечение элемента с наивысшим приоритетом (наименьшим значением приоритета)
        
        Returns:
            Значение элемента с наивысшим приоритетом
        
        Сложность: O(log n)
        """
        if not self.heap:
            raise IndexError("Очередь пуста")
        
        if len(self.heap) == 1:
            return self.heap.pop().value
        
        item = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._sift_down(0)
        
        return item.value
    
    def peek(self):
        """
        Просмотр элемента с наивысшим приоритетом без извлечения
        
        Returns:
            Кортеж (значение, приоритет) элемента с наивысшим приоритетом
        
        Сложность: O(1)
        """
        if not self.heap:
            raise IndexError("Очередь пуста")
        
        item = self.heap[0]
        return item.value, item.priority
    
    def is_empty(self):
        """Проверяет, пуста ли очередь"""
        return len(self.heap) == 0
    
    def size(self):
        """Возвращает размер очереди"""
        return len(self.heap)
    
    def clear(self):
        """Очищает очередь"""
        self.heap = []
    
    def __str__(self):
        """Строковое представление очереди"""
        items = [str(item) for item in self.heap]
        return "Приоритетная очередь: " + " -> ".join(items)
    
    def print_queue(self):
        """Вывод очереди в удобном формате"""
        if self.is_empty():
            print("Очередь пуста")
            return
        
        print("Элементы приоритетной очереди (значение, приоритет):")
        # Создаем копию и извлекаем элементы в порядке приоритета
        temp_heap = self.heap[:]
        while temp_heap:
            # Находим элемент с наивысшим приоритетом
            min_idx = 0
            for i in range(1, len(temp_heap)):
                if temp_heap[i] < temp_heap[min_idx]:
                    min_idx = i
            
            item = temp_heap.pop(min_idx)
            print(f"  {item.value} (приоритет: {item.priority})")