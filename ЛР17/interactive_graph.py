"""Демонстрация работы обходов графа (ЛР17).

Запустите `python3 ЛР17/interactive_graph.py` для просмотра примера.
"""
from graph import Graph


def demo():
    # Пример 1: неориентированный граф
    mat1 = [
        [0, 1, 1, 0, 0],
        [1, 0, 0, 1, 0],
        [1, 0, 0, 1, 1],
        [0, 1, 1, 0, 1],
        [0, 0, 1, 1, 0],
    ]
    print("Пример: неориентированный граф (5 вершин)")
    g1 = Graph(mat1, directed=False)
    g1.display()
    print("BFS от 0:", g1.bfs(0))
    print("DFS рекурсивный от 0:", g1.dfs(0))
    print("DFS итеративный от 0:", g1.dfs_iterative(0))

    print("\n---\n")

    # Пример 2: ориентированный граф
    mat2 = [
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1],
        [1, 0, 0, 0],
    ]
    print("Пример: ориентированный граф (цикл)")
    g2 = Graph(mat2, directed=True)
    g2.display()
    print("BFS от 0:", g2.bfs(0))
    print("DFS рекурсивный от 0:", g2.dfs(0))


if __name__ == "__main__":
    demo()
