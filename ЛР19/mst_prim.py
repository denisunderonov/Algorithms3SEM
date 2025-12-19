"""Алгоритм Прима для поиска остова минимального веса (MST).

Реализован для графа, заданного матрицей смежности (взвешенный неориентированный граф).
Используется простой O(n^2) подход — подходящ для матрицы смежности и средних n.
"""
from typing import List, Tuple, Optional
import math


def prim(matrix: List[List[float]], start: int = 0) -> Tuple[List[Tuple[int, int, float]], float]:
    """Вычислить MST алгоритмом Прима, начиная с вершины start.

    Возвращает (mst_edges, total_weight).
    """
    if not matrix or any(len(row) != len(matrix) for row in matrix):
        raise ValueError("Матрица смежности должна быть квадратной и не пустой")
    n = len(matrix)
    if not (0 <= start < n):
        raise IndexError("start вне диапазона вершин")

    in_mst = [False] * n
    key = [math.inf] * n
    parent: List[Optional[int]] = [None] * n

    key[start] = 0.0

    for _ in range(n):
        # выбрать неприсоединённую вершину с минимальным key
        u = -1
        best = math.inf
        for v in range(n):
            if not in_mst[v] and key[v] < best:
                best = key[v]
                u = v

        if u == -1:
            break
        in_mst[u] = True

        # обновить ключи соседей
        for v in range(n):
            w = matrix[u][v]
            if w and not in_mst[v] and w < key[v]:
                key[v] = w
                parent[v] = u

    # собрать рёбра MST
    edges: List[Tuple[int, int, float]] = []
    total = 0.0
    for v in range(n):
        p = parent[v]
        if p is not None:
            w = matrix[p][v]
            edges.append((p, v, w))
            total += w

    if len(edges) != n - 1:
        raise ValueError("Граф несвязный: MST не существует")

    return edges, total


if __name__ == "__main__":
    mat = [
        [0, 2, 0, 6, 0],
        [2, 0, 3, 8, 5],
        [0, 3, 0, 0, 7],
        [6, 8, 0, 0, 9],
        [0, 5, 7, 9, 0],
    ]
    edges, total = prim(mat, start=0)
    print("MST (Prim):", edges)
    print("Total weight:", total)
