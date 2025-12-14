import time
import random
import matplotlib.pyplot as plt
from binary_search_tree import BinarySearchTree
import numpy as np


def main():
    print("АНАЛИЗ BST")
    print("="*60)
    
    sizes = [10, 50, 100, 200, 300, 400, 500, 800, 1000]
    
    balanced_times = []
    degenerate_times = []
    balanced_heights = []
    degenerate_heights = []
    
    for n in sizes:
        print(f"\nАнализ для n = {n}")
        
        # Сбалансированное дерево
        print("  Построение сбалансированного дерева...")
        balanced_tree = BinarySearchTree()
        values = list(range(n))
        random.shuffle(values)
        
        for value in values:
            balanced_tree.insert(value)
        
        balanced_heights.append(balanced_tree.height())
        
        # Измерение времени поиска
        print("  Измерение времени поиска...")
        search_values = values[:min(100, n)]
        
        start_time = time.perf_counter()
        for value in search_values:
            balanced_tree.search(value)
        balanced_time = (time.perf_counter() - start_time) / len(search_values)
        balanced_times.append(balanced_time)
        
        # Вырожденное дерево
        print("  Построение вырожденного дерева...")
        degenerate_tree = BinarySearchTree()
        
        for value in range(n):
            degenerate_tree.insert(value)
        
        degenerate_heights.append(degenerate_tree.height())
        
        # Измерение времени поиска
        start_time = time.perf_counter()
        for value in search_values:
            degenerate_tree.search(value)
        degenerate_time = (time.perf_counter() - start_time) / len(search_values)
        degenerate_times.append(degenerate_time)
        
        print(f"  Результаты: высота {balanced_heights[-1]} vs {degenerate_heights[-1]}, "
              f"время {balanced_times[-1]:.8f} vs {degenerate_times[-1]:.8f}")
    
    # Построение графиков
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    
    # График 1: Время поиска
    axes[0, 0].plot(sizes, balanced_times, 'bo-', label='Сбалансированное', linewidth=2)
    axes[0, 0].plot(sizes, degenerate_times, 'ro-', label='Вырожденное', linewidth=2)
    axes[0, 0].set_xlabel('Количество элементов (n)')
    axes[0, 0].set_ylabel('Среднее время поиска (сек)')
    axes[0, 0].set_title('Время поиска')
    axes[0, 0].legend()
    axes[0, 0].grid(True, alpha=0.3)
    
    # График 2: Высота дерева
    axes[0, 1].plot(sizes, balanced_heights, 'bo-', label='Сбалансированное', linewidth=2)
    axes[0, 1].plot(sizes, degenerate_heights, 'ro-', label='Вырожденное', linewidth=2)
    axes[0, 1].plot(sizes, np.log2(sizes), 'g--', label='log₂(n)', alpha=0.7)
    axes[0, 1].plot(sizes, sizes, 'k--', label='n', alpha=0.3)
    axes[0, 1].set_xlabel('Количество элементов (n)')
    axes[0, 1].set_ylabel('Высота дерева')
    axes[0, 1].set_title('Высота дерева')
    axes[0, 1].legend()
    axes[0, 1].grid(True, alpha=0.3)
    
    # График 3: Отношение времен
    ratios = [d/b if b > 0 else 0 for d, b in zip(degenerate_times, balanced_times)]
    axes[1, 0].plot(sizes, ratios, 'purple', linewidth=2, marker='o')
    axes[1, 0].set_xlabel('Количество элементов (n)')
    axes[1, 0].set_ylabel('Отношение времен (вырожд./сбаланс.)')
    axes[1, 0].set_title('Во сколько раз вырожденное дерево медленнее')
    axes[1, 0].grid(True, alpha=0.3)
    
    # График 4: Зависимость времени от высоты
    axes[1, 1].scatter(balanced_heights, balanced_times, c='blue', 
                      label='Сбалансированное', alpha=0.6, s=50)
    axes[1, 1].scatter(degenerate_heights, degenerate_times, c='red', 
                      label='Вырожденное', alpha=0.6, s=50)
    axes[1, 1].set_xlabel('Высота дерева')
    axes[1, 1].set_ylabel('Время поиска (сек)')
    axes[1, 1].set_title('Зависимость времени поиска от высоты')
    axes[1, 1].legend()
    axes[1, 1].grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()
    
    # Вывод результатов
    print("\n" + "="*60)
    print("ИТОГОВЫЕ РЕЗУЛЬТАТЫ")
    print("="*60)
    
    for i, n in enumerate(sizes):
        print(f"\nn = {n}:")
        print(f"  Сбалансированное: высота={balanced_heights[i]}, "
              f"время={balanced_times[i]:.9f} сек")
        print(f"  Вырожденное: высота={degenerate_heights[i]}, "
              f"время={degenerate_times[i]:.9f} сек")
        if balanced_times[i] > 0:
            ratio = degenerate_times[i] / balanced_times[i]
            print(f"  Отношение: {ratio:.2f}:1")


if __name__ == "__main__":
    main()