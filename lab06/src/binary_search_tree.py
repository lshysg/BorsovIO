import sys
sys.setrecursionlimit(10000)  # Увеличиваем лимит рекурсии

class TreeNode:
    """Узел бинарного дерева поиска"""
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.value)


class BinarySearchTree:
    """Бинарное дерево поиска"""
    
    def __init__(self):
        self.root = None
        self._size = 0
    
    def insert(self, value):
        """Вставка значения в дерево (итеративная версия).
        Сложность: O(log n) в среднем, O(n) в худшем (вырожденное дерево)
        """
        new_node = TreeNode(value)
        
        if self.root is None:
            self.root = new_node
            self._size = 1
            return
        
        current = self.root
        parent = None
        
        while current is not None:
            parent = current
            if value < current.value:
                current = current.left
            elif value > current.value:
                current = current.right
            else:
                # Значение уже существует
                return
        
        if value < parent.value:
            parent.left = new_node
        else:
            parent.right = new_node
        
        self._size += 1
    
    def insert_recursive(self, value):
        """Вставка значения в дерево (рекурсивная версия).
        Используется для демонстрации, но для больших деревьев лучше итеративная.
        """
        if self.root is None:
            self.root = TreeNode(value)
            self._size = 1
        else:
            self._insert_recursive(self.root, value)
    
    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = TreeNode(value)
                self._size += 1
            else:
                self._insert_recursive(node.left, value)
        elif value > node.value:
            if node.right is None:
                node.right = TreeNode(value)
                self._size += 1
            else:
                self._insert_recursive(node.right, value)
        # Если значение уже существует, ничего не делаем
    
    def search(self, value):
        """Поиск значения в дереве (итеративная версия).
        Сложность: O(log n) в среднем, O(n) в худшем (вырожденное дерево)
        """
        current = self.root
        
        while current is not None:
            if value == current.value:
                return True
            elif value < current.value:
                current = current.left
            else:
                current = current.right
        
        return False
    
    def search_recursive(self, value):
        """Поиск значения в дереве (рекурсивная версия)."""
        return self._search_recursive(self.root, value)
    
    def _search_recursive(self, node, value):
        if node is None:
            return False
        if value == node.value:
            return True
        elif value < node.value:
            return self._search_recursive(node.left, value)
        else:
            return self._search_recursive(node.right, value)
    
    def delete(self, value):
        """Удаление значения из дерева.
        Сложность: O(log n) в среднем, O(n) в худшем (вырожденное дерево)
        """
        self.root = self._delete_recursive(self.root, value)
        if self.root is not None:
            # Обновляем размер
            self._size = self._size_recursive(self.root)
    
    def _delete_recursive(self, node, value):
        if node is None:
            return node
        
        # Поиск узла для удаления
        if value < node.value:
            node.left = self._delete_recursive(node.left, value)
        elif value > node.value:
            node.right = self._delete_recursive(node.right, value)
        else:
            # Узел найден
            # Случай 1: узел без потомков или с одним потомком
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            
            # Случай 3: узел с двумя потомками
            # Находим минимальное значение в правом поддереве
            min_node = self._find_min_node(node.right)
            node.value = min_node.value
            node.right = self._delete_recursive(node.right, min_node.value)
        
        return node
    
    def _find_min_node(self, node):
        """Вспомогательный метод для поиска минимального узла"""
        current = node
        while current.left is not None:
            current = current.left
        return current
    
    def find_min(self, node=None):
        """Поиск минимального значения в поддереве.
        Сложность: O(log n) в среднем, O(n) в худшем
        """
        if node is None:
            node = self.root
        if node is None:
            return None
        
        current = node
        while current.left is not None:
            current = current.left
        return current
    
    def find_max(self, node=None):
        """Поиск максимального значения в поддереве.
        Сложность: O(log n) в среднем, O(n) в худшем
        """
        if node is None:
            node = self.root
        if node is None:
            return None
        
        current = node
        while current.right is not None:
            current = current.right
        return current
    
    def is_valid_bst(self):
        """Проверка, является ли дерево корректным BST.
        Сложность: O(n)
        """
        return self._is_valid_recursive(self.root, float('-inf'), float('inf'))
    
    def _is_valid_recursive(self, node, min_val, max_val):
        if node is None:
            return True
        
        if node.value <= min_val or node.value >= max_val:
            return False
        
        return (self._is_valid_recursive(node.left, min_val, node.value) and
                self._is_valid_recursive(node.right, node.value, max_val))
    
    def height(self, node=None):
        """Вычисление высоты дерева/поддерева.
        Сложность: O(n)
        """
        if node is None:
            node = self.root
        if node is None:
            return 0
        
        left_height = self.height(node.left) if node.left else 0
        right_height = self.height(node.right) if node.right else 0
        
        return max(left_height, right_height) + 1
    
    def size(self):
        """Возвращает количество узлов в дереве.
        Сложность: O(1) - теперь храним размер отдельно
        """
        return self._size
    
    def _size_recursive(self, node):
        """Рекурсивный подсчет размера (для внутреннего использования)"""
        if node is None:
            return 0
        return 1 + self._size_recursive(node.left) + self._size_recursive(node.right)
    
    def get_inorder_list(self):
        """Возвращает список элементов в порядке in-order"""
        result = []
        self._inorder_recursive(self.root, result)
        return result
    
    def _inorder_recursive(self, node, result):
        if node:
            self._inorder_recursive(node.left, result)
            result.append(node.value)
            self._inorder_recursive(node.right, result)