import unittest
from binary_search_tree import BinarySearchTree, TreeNode
from tree_traversal import *
import random


class TestBinarySearchTree(unittest.TestCase):
    
    def setUp(self):
        """Подготовка тестовых данных"""
        self.bst = BinarySearchTree()
        self.values = [50, 30, 70, 20, 40, 60, 80]
        for value in self.values:
            self.bst.insert(value)
    
    def test_insert_and_search(self):
        """Тестирование вставки и поиска"""
        # Проверка существующих значений
        for value in self.values:
            self.assertTrue(self.bst.search(value), 
                          f"Значение {value} должно быть найдено")
        
        # Проверка несуществующих значений
        self.assertFalse(self.bst.search(100), 
                        "Несуществующее значение не должно быть найдено")
        self.assertFalse(self.bst.search(10), 
                        "Несуществующее значение не должно быть найдено")
    
    def test_is_valid_bst(self):
        """Тестирование проверки валидности BST"""
        self.assertTrue(self.bst.is_valid_bst(),
                       "Дерево должно быть валидным BST")
        
        # Создаем невалидное дерево
        invalid_bst = BinarySearchTree()
        root = TreeNode(50)
        root.left = TreeNode(60)  # Нарушает свойство BST
        root.right = TreeNode(70)
        invalid_bst.root = root
        
        self.assertFalse(invalid_bst.is_valid_bst(),
                        "Дерево не должно быть валидным BST")
    
    def test_find_min_max(self):
        """Тестирование поиска минимума и максимума"""
        self.assertEqual(self.bst.find_min().value, 20,
                        "Минимальное значение должно быть 20")
        self.assertEqual(self.bst.find_max().value, 80,
                        "Максимальное значение должно быть 80")
        
        # Тест с пустым деревом
        empty_bst = BinarySearchTree()
        self.assertIsNone(empty_bst.find_min(),
                         "В пустом дереве минимум должен быть None")
        self.assertIsNone(empty_bst.find_max(),
                         "В пустом дереве максимум должен быть None")
    
    def test_height(self):
        """Тестирование вычисления высоты"""
        # Высота дерева с 7 элементами (сбалансированного) должна быть 3
        self.assertEqual(self.bst.height(), 3,
                        f"Высота дерева должна быть 3, получено {self.bst.height()}")
        
        # Тест с одним элементом
        single_bst = BinarySearchTree()
        single_bst.insert(10)
        self.assertEqual(single_bst.height(), 1,
                        "Высота дерева с одним элементом должна быть 1")
        
        # Тест с пустым деревом
        empty_bst = BinarySearchTree()
        self.assertEqual(empty_bst.height(), 0,
                        "Высота пустого дерева должна быть 0")
    
    def test_delete(self):
        """Тестирование удаления элементов"""
        # Удаление листа
        self.bst.delete(20)
        self.assertFalse(self.bst.search(20),
                        "Удаленное значение 20 не должно быть найдено")
        self.assertTrue(self.bst.is_valid_bst(),
                       "Дерево должно остаться валидным BST")
        
        # Удаление узла с одним потомком
        self.bst.delete(20)  # Уже удален, но вдруг
        self.bst.delete(30)
        self.assertFalse(self.bst.search(30),
                        "Удаленное значение 30 не должно быть найдено")
        self.assertTrue(self.bst.is_valid_bst(),
                       "Дерево должно остаться валидным BST")
        
        # Удаление узла с двумя потомками
        self.bst.delete(50)
        self.assertFalse(self.bst.search(50),
                        "Удаленное значение 50 не должно быть найдено")
        self.assertTrue(self.bst.is_valid_bst(),
                       "Дерево должно остаться валидным BST")
        
        # Проверка всех оставшихся элементов
        remaining = [40, 60, 70, 80]
        for value in remaining:
            self.assertTrue(self.bst.search(value),
                          f"Оставшееся значение {value} должно быть найдено")
    
    def test_traversals(self):
        """Тестирование обходов дерева"""
        # In-order должен возвращать отсортированный список
        expected_inorder = sorted(self.values)
        actual_inorder = inorder_recursive(self.bst.root)
        self.assertEqual(actual_inorder, expected_inorder,
                        f"In-order обход должен возвращать {expected_inorder}")
        
        # Сравнение рекурсивного и итеративного in-order
        iterative_result = inorder_iterative(self.bst.root)
        self.assertEqual(iterative_result, actual_inorder,
                        "Рекурсивный и итеративный in-order должны совпадать")
        
        # Pre-order для конкретного дерева
        expected_preorder = [50, 30, 20, 40, 70, 60, 80]
        actual_preorder = preorder_recursive(self.bst.root)
        self.assertEqual(actual_preorder, expected_preorder,
                        f"Pre-order обход должен возвращать {expected_preorder}")
        
        # Post-order для конкретного дерева
        expected_postorder = [20, 40, 30, 60, 80, 70, 50]
        actual_postorder = postorder_recursive(self.bst.root)
        self.assertEqual(actual_postorder, expected_postorder,
                        f"Post-order обход должен возвращать {expected_postorder}")
    
    def test_size(self):
        """Тестирование подсчета размера дерева"""
        self.assertEqual(self.bst.size(), 7,
                        f"Размер дерева должен быть 7, получено {self.bst.size()}")
        
        # После удаления
        self.bst.delete(50)
        self.assertEqual(self.bst.size(), 6,
                        f"После удаления размер должен быть 6")
        
        # Пустое дерево
        empty_bst = BinarySearchTree()
        self.assertEqual(empty_bst.size(), 0,
                        "Размер пустого дерева должен быть 0")
    
    def test_random_operations(self):
        """Тестирование случайных операций для проверки целостности"""
        random_bst = BinarySearchTree()
        inserted_values = set()
        
        # Случайные вставки
        for _ in range(100):
            value = random.randint(0, 1000)
            random_bst.insert(value)
            inserted_values.add(value)
        
        # Проверка валидности после вставок
        self.assertTrue(random_bst.is_valid_bst(),
                       "Дерево должно остаться валидным BST после вставок")
        
        # Проверка поиска для некоторых значений
        for value in list(inserted_values)[:10]:  # Проверяем 10 случайных
            self.assertTrue(random_bst.search(value),
                          f"Вставленное значение {value} должно быть найдено")
        
        # Случайные удаления
        for value in list(inserted_values)[:20]:  # Удаляем 20 случайных
            random_bst.delete(value)
            inserted_values.remove(value)
        
        # Проверка валидности после удалений
        self.assertTrue(random_bst.is_valid_bst(),
                       "Дерево должно остаться валидным BST после удалений")


class TestEdgeCases(unittest.TestCase):
    """Тестирование крайних случаев"""
    
    def test_empty_tree(self):
        """Тестирование операций с пустым деревом"""
        bst = BinarySearchTree()
        
        self.assertFalse(bst.search(10))
        self.assertEqual(bst.height(), 0)
        self.assertEqual(bst.size(), 0)
        self.assertIsNone(bst.find_min())
        self.assertIsNone(bst.find_max())
        self.assertTrue(bst.is_valid_bst())  # Пустое дерево - валидное BST
    
    def test_single_node(self):
        """Тестирование дерева с одним узлом"""
        bst = BinarySearchTree()
        bst.insert(42)
        
        self.assertTrue(bst.search(42))
        self.assertFalse(bst.search(10))
        self.assertEqual(bst.height(), 1)
        self.assertEqual(bst.size(), 1)
        self.assertEqual(bst.find_min().value, 42)
        self.assertEqual(bst.find_max().value, 42)
        self.assertTrue(bst.is_valid_bst())
        
        # Удаление единственного узла
        bst.delete(42)
        self.assertFalse(bst.search(42))
        self.assertEqual(bst.size(), 0)
    
    def test_duplicate_values(self):
        """Тестирование дубликатов значений"""
        bst = BinarySearchTree()
        bst.insert(10)
        bst.insert(10)  # Дубликат
        
        self.assertTrue(bst.search(10))
        self.assertEqual(bst.size(), 1)  # Размер не должен увеличиться
    
    def test_sorted_insertion_degenerate(self):
        """Тестирование вырожденного дерева (отсортированная вставка)"""
        bst = BinarySearchTree()
        
        for i in range(100):
            bst.insert(i)
        
        self.assertTrue(bst.is_valid_bst())
        self.assertEqual(bst.height(), 100)  # Высота = n для вырожденного дерева
        self.assertEqual(bst.find_min().value, 0)
        self.assertEqual(bst.find_max().value, 99)


if __name__ == "__main__":
    unittest.main(verbosity=2)