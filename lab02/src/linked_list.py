class Node:
    """Класс узла связного списка"""
    def __init__(self, data):
        self.data = data
        self.next = None
        #  O(1) - создание узла занимает постоянное время


class LinkedList:
    """Односвязный список с поддержкой хвоста для O(1) вставки в конец"""
    def __init__(self):
        self.head = None
        self.tail = None
        #  O(1) - инициализация пустого списка

    def insert_at_start(self, data):
        """
        Вставка в начало списка        
        """
        new_node = Node(data)  # O(1)
        new_node.next = self.head  # O(1)
        self.head = new_node  # O(1)
        if self.tail is None:  # O(1)
            self.tail = new_node  # O(1)
        #  O(1) - вставка всегда занимает постоянное время

    def insert_at_end(self, data):
        """
        Вставка в конец списка        
        """
        new_node = Node(data)  # O(1)
        if self.tail:  # O(1)
            self.tail.next = new_node  # O(1)
            self.tail = new_node  # O(1)
        else:  # список пустой
            self.head = self.tail = new_node  # O(1)
        #  O(1) - благодаря хранению tail указателя вставка в конец постоянна

    def delete_from_start(self):
        """
        Удаление из начала списка        
        """
        if self.head is None:  # O(1)
            return None
        removed_data = self.head.data  # O(1)
        self.head = self.head.next  # O(1)
        if self.head is None:  # O(1)
            self.tail = None  # O(1)
        return removed_data  # O(1)
        #  O(1) - всегда удаляем первый элемент, не нужно проходить список

    def traversal(self):
        """
        Обход списка   
        """
        elements = []  # O(1)
        current = self.head  # O(1)
        while current:  # O(n) - проход по всем элементам
            elements.append(current.data)  # O(1) на каждый элемент
            current = current.next  # O(1) на каждый элемент
        return elements  # O(1)
        #  O(n) - нужно пройти весь список из n элементов


if __name__ == "__main__":
    # Простой тест
    ll = LinkedList()
    ll.insert_at_start(1)
    ll.insert_at_start(2)
    ll.insert_at_end(3)
    print("Содержимое списка:", ll.traversal())
    ll.delete_from_start()
    print("После удаления с начала:", ll.traversal())