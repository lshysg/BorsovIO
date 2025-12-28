"""
Визуализация работы алгоритмов динамического программирования.
"""

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from typing import List, Tuple
from dynamic_programming import LCS, Levenshtein, Knapsack


class DPVisualizer:
    """Класс для визуализации таблиц ДП."""
    
    @staticmethod
    def visualize_lcs_table(str1: str, str2: str) -> None:
        """Визуализация таблицы LCS."""
        m, n = len(str1), len(str2)
        
        # Создаем таблицу DP
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # Заполняем таблицу
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if str1[i-1] == str2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        # Визуализация
        fig, ax = plt.subplots(figsize=(10, 8))
        
        # Создаем матрицу для heatmap
        matrix = np.array(dp)
        
        # Создаем heatmap
        sns.heatmap(matrix, annot=True, fmt='d', cmap='YlOrRd', 
                   linewidths=0.5, ax=ax)
        
        # Настраиваем подписи
        ax.set_xticklabels([''] + list(str2))
        ax.set_yticklabels([''] + list(str1))
        ax.set_xlabel('Строка 2')
        ax.set_ylabel('Строка 1')
        ax.set_title(f'Таблица LCS для "{str1}" и "{str2}"')
        
        # Вычисляем LCS
        lcs_len, lcs_str = LCS.bottom_up(str1, str2)
        ax.text(0.5, -0.1, f'Длина LCS: {lcs_len}, LCS: "{lcs_str}"', 
               transform=ax.transAxes, ha='center', fontsize=12)
        
        plt.tight_layout()
        plt.savefig('lcs_table.png', dpi=300, bbox_inches='tight')
        plt.show()
        
        print(f"\nLCS для '{str1}' и '{str2}':")
        print(f"  Длина: {lcs_len}")
        print(f"  Последовательность: {lcs_str}")
        print(f"  Таблица сохранена как 'lcs_table.png'")
    
    @staticmethod
    def visualize_levenshtein_table(str1: str, str2: str) -> None:
        """Визуализация таблицы расстояния Левенштейна."""
        m, n = len(str1), len(str2)
        
        # Создаем таблицу DP
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # Инициализируем
        for i in range(m + 1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j
        
        # Заполняем таблицу
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if str1[i-1] == str2[j-1]:
                    cost = 0
                else:
                    cost = 1
                
                dp[i][j] = min(
                    dp[i-1][j] + 1,
                    dp[i][j-1] + 1,
                    dp[i-1][j-1] + cost
                )
        
        # Визуализация
        fig, ax = plt.subplots(figsize=(10, 8))
        
        matrix = np.array(dp)
        sns.heatmap(matrix, annot=True, fmt='d', cmap='Blues',
                   linewidths=0.5, ax=ax)
        
        ax.set_xticklabels([''] + list(str2))
        ax.set_yticklabels([''] + list(str1))
        ax.set_xlabel('Строка 2')
        ax.set_ylabel('Строка 1')
        ax.set_title(f'Таблица расстояния Левенштейна')
        
        distance = dp[m][n]
        ax.text(0.5, -0.1, f'Расстояние: {distance}', 
               transform=ax.transAxes, ha='center', fontsize=12)
        
        plt.tight_layout()
        plt.savefig('levenshtein_table.png', dpi=300, bbox_inches='tight')
        plt.show()
        
        print(f"\nРасстояние Левенштейна между '{str1}' и '{str2}': {distance}")
        print(f"Таблица сохранена как 'levenshtein_table.png'")
    
    @staticmethod
    def visualize_knapsack_table(weights: List[int], values: List[int], capacity: int) -> None:
        """Визуализация таблицы задачи о рюкзаке."""
        n = len(weights)
        
        # Создаем таблицу DP
        dp = [[0] * (capacity + 1) for _ in range(n + 1)]
        
        # Заполняем таблицу
        for i in range(1, n + 1):
            for w in range(1, capacity + 1):
                if weights[i-1] <= w:
                    dp[i][w] = max(dp[i-1][w], 
                                  dp[i-1][w - weights[i-1]] + values[i-1])
                else:
                    dp[i][w] = dp[i-1][w]
        
        # Визуализация
        fig, ax = plt.subplots(figsize=(12, 8))
        
        matrix = np.array(dp)
        sns.heatmap(matrix, annot=True, fmt='d', cmap='Greens',
                   linewidths=0.5, ax=ax, annot_kws={"size": 8})
        
        # Настраиваем подписи
        ax.set_xticks(np.arange(capacity + 1))
        ax.set_xticklabels([str(i) for i in range(capacity + 1)], rotation=0)
        ax.set_yticks(np.arange(n + 1))
        ax.set_yticklabels([''] + [f'Предмет {i}' for i in range(1, n + 1)])
        ax.set_xlabel('Вместимость рюкзака')
        ax.set_ylabel('Предметы')
        ax.set_title(f'Таблица задачи о рюкзаке (емкость={capacity})')
        
        max_value = dp[n][capacity]
        ax.text(0.5, -0.1, f'Максимальная стоимость: {max_value}', 
               transform=ax.transAxes, ha='center', fontsize=12)
        
        plt.tight_layout()
        plt.savefig('knapsack_table.png', dpi=300, bbox_inches='tight')
        plt.show()
        
        print(f"\nЗадача о рюкзаке:")
        print(f"  Веса: {weights}")
        print(f"  Стоимости: {values}")
        print(f"  Вместимость: {capacity}")
        print(f"  Максимальная стоимость: {max_value}")
        print(f"  Таблица сохранена как 'knapsack_table.png'")


def main():
    """Основная функция для визуализации."""
    print("Визуализация таблиц динамического программирования")
    print("="*60)
    
    # Пример 1: LCS
    print("\n1. Наибольшая общая подпоследовательность (LCS)")
    str1 = "ABCDGH"
    str2 = "AEDFHR"
    DPVisualizer.visualize_lcs_table(str1, str2)
    
    # Пример 2: Расстояние Левенштейна
    print("\n2. Расстояние Левенштейна")
    str1 = "kitten"
    str2 = "sitting"
    DPVisualizer.visualize_levenshtein_table(str1, str2)
    
    # Пример 3: Задача о рюкзаке
    print("\n3. Задача о рюкзаке 0-1")
    weights = [1, 3, 4, 5]
    values = [1, 4, 5, 7]
    capacity = 7
    DPVisualizer.visualize_knapsack_table(weights, values, capacity)


if __name__ == "__main__":
    main()