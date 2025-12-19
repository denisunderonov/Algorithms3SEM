"""Алгоритм Краскала для поиска остова минимального веса (MST).

Работает для связного неориентированного взвешенного графа, заданного матрицей смежности.
Матрица: matrix[u][v] > 0 — вес ребра, matrix[u][v] == 0 — ребра нет.

Функция `kruskal(matrix)` возвращает кортеж (mst_edges, total_weight),
где mst_edges — список рёбер в формате (u, v, w) и total_weight — суммарный вес.
"""
from typing import List, Tuple


class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a: int, b: int) -> bool:
        ra = self.find(a)
        rb = self.find(b)
        if ra == rb:
            return False
        if self.rank[ra] < self.rank[rb]:
            self.parent[ra] = rb
        elif self.rank[ra] > self.rank[rb]:
            self.parent[rb] = ra
        else:
            self.parent[rb] = ra
            self.rank[ra] += 1
        return True


def kruskal(matrix: List[List[float]]) -> Tuple[List[Tuple[int, int, float]], float]:
    """Вычислить MST алгоритмом Краскала.

    Предполагается, что matrix — квадратная матрица.
    Для неориентированного графа матрица должна быть симметричной (или функция обработает u<v).
    """
    if not matrix or any(len(row) != len(matrix) for row in matrix):
        raise ValueError("Матрица смежности должна быть квадратной и не пустой")
    n = len(matrix)

    # собрать все рёбра (u,v,w) с u < v, где вес > 0
    edges: List[Tuple[int, int, float]] = []
    for i in range(n):
        for j in range(i + 1, n):
            w = matrix[i][j]
            if w:
                edges.append((i, j, w))

    # сортировка по весу
    edges.sort(key=lambda e: e[2])

    uf = UnionFind(n)
    mst: List[Tuple[int, int, float]] = []
    total = 0.0

    for u, v, w in edges:
        if uf.union(u, v):
            mst.append((u, v, w))
            total += w
            if len(mst) == n - 1:
                break

    if len(mst) != n - 1:
        raise ValueError("Граф несвязный: MST не существует")

    return mst, total


if __name__ == "__main__":
    # Простой пример
    mat = [
        [0, 2, 0, 6, 0],
        [2, 0, 3, 8, 5],
        [0, 3, 0, 0, 7],
        [6, 8, 0, 0, 9],
        [0, 5, 7, 9, 0],
    ]
    mst, total = kruskal(mat)
    print("MST (Kruskal):", mst)
    print("Total weight:", total)
