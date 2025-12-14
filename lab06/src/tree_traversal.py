from binary_search_tree import BinarySearchTree


def inorder_recursive(node, result=None):
    """Рекурсивный in-order обход.
    Сложность: O(n)
    """
    if result is None:
        result = []
    
    if node:
        inorder_recursive(node.left, result)
        result.append(node.value)
        inorder_recursive(node.right, result)
    
    return result


def preorder_recursive(node, result=None):
    """Рекурсивный pre-order обход.
    Сложность: O(n)
    """
    if result is None:
        result = []
    
    if node:
        result.append(node.value)
        preorder_recursive(node.left, result)
        preorder_recursive(node.right, result)
    
    return result


def postorder_recursive(node, result=None):
    """Рекурсивный post-order обход.
    Сложность: O(n)
    """
    if result is None:
        result = []
    
    if node:
        postorder_recursive(node.left, result)
        postorder_recursive(node.right, result)
        result.append(node.value)
    
    return result


def inorder_iterative(root):
    """Итеративный in-order обход с использованием стека.
    Сложность: O(n)
    """
    result = []
    stack = []
    current = root
    
    while current is not None or stack:
        # Достигаем самого левого узла
        while current is not None:
            stack.append(current)
            current = current.left
        
        current = stack.pop()
        result.append(current.value)
        
        # Переходим к правому поддереву
        current = current.right
    
    return result


def level_order_traversal(root):
    """Обход дерева по уровням (BFS).
    Сложность: O(n)
    """
    if not root:
        return []
    
    result = []
    queue = [root]
    
    while queue:
        current = queue.pop(0)
        result.append(current.value)
        
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    
    return result


# Пример использования функций обхода
if __name__ == "__main__":
    bst = BinarySearchTree()
    values = [50, 30, 70, 20, 40, 60, 80]
    
    for value in values:
        bst.insert(value)
    
    print("In-order (рекурсивный):", inorder_recursive(bst.root))
    print("Pre-order (рекурсивный):", preorder_recursive(bst.root))
    print("Post-order (рекурсивный):", postorder_recursive(bst.root))
    print("In-order (итеративный):", inorder_iterative(bst.root))
    print("Level-order (BFS):", level_order_traversal(bst.root))