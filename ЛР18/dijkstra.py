"""Реализация алгоритма Дейкстры для взвешенного ориентированного графа,
заданного взвешенной матрицей смежности.

Уточнение формата матрицы:
- `matrix[u][v]` > 0 — вес ребра u->v.
- `matrix[u][v] == 0` — ребра нет (кроме диагонали); нулевой вес ребра не поддерживается в этой учебной реализации.

API:
- `dijkstra(matrix, start)` -> (distances, prev)
    - distances: список минимальных расстояний от start до каждой вершины (float('inf') если недостижима).
    - prev: список предков для восстановления путей (None если нет предка).
- `reconstruct_path(prev, start, end)` -> список вершин пути start..end или пустой список если пути нет.

Все сообщения и докстринги на русском.
"""
from typing import List, Optional, Tuple
import math


def dijkstra(matrix: List[List[float]], start: int) -> Tuple[List[float], List[Optional[int]]]:
    """Выполнить алгоритм Дейкстры для матрицы смежности.

    Параметры:
    - matrix: квадратная матрица (список списков). matrix[u][v] > 0 означает вес ребра u->v.
    - start: индекс стартовой вершины (0..n-1).

    Возвращает (distances, prev):
    - distances[i] — минимальное расстояние от start до i (float('inf') если недостижимо).
    - prev[i] — предыдущая вершина на кратчайшем пути к i (None если нет предка или i == start).
    """
    if not matrix or any(len(row) != len(matrix) for row in matrix):
        raise ValueError("Матрица смежности должна быть квадратной и не пустой")
    n = len(matrix)
    if not (0 <= start < n):
        raise IndexError("start вне диапазона вершин")

    dist: List[float] = [math.inf] * n
    prev: List[Optional[int]] = [None] * n
    visited: List[bool] = [False] * n

    dist[start] = 0.0

    for _ in range(n):
        # выбрать непросмотренную вершину с минимальной dist
        u = -1
        best = math.inf
        for i in range(n):
            if not visited[i] and dist[i] < best:
                best = dist[i]
                u = i

        if u == -1:
            # все оставшиеся вершины недостижимы
            break

        visited[u] = True

        # релаксация всех исходящих рёбер из u
        for v in range(n):
            w = matrix[u][v]
            if w:  # если вес не 0 — ребро существует
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    prev[v] = u

    return dist, prev


def reconstruct_path(prev: List[Optional[int]], start: int, end: int) -> List[int]:
    """Восстановить путь из start в end по массиву prev.

    Возвращает список вершин от start до end включительно, или пустой список если пути нет.
    """
    path: List[int] = []
    cur = end
    while cur is not None:
        path.append(cur)
        if cur == start:
            break
        cur = prev[cur]

    if not path or path[-1] != start:
        return []
    path.reverse()
    return path


if __name__ == "__main__":
    # Короткий пример: ориентированный взвешенный граф (0 == нет ребра)
    mat = [
        [0, 7, 9, 0, 0, 14],
        [0, 0, 10, 15, 0, 0],
        [0, 0, 0, 11, 0, 2],
        [0, 0, 0, 0, 6, 0],
        [0, 0, 0, 0, 0, 9],
        [0, 0, 0, 0, 0, 0],
    ]
    start = 0
    dist, prev = dijkstra(mat, start)
    print(f"Расстояния от вершины {start}: {dist}")
    for v in range(len(mat)):
        p = reconstruct_path(prev, start, v)
        if p:
            print(f"Кратчайший путь {start} -> {v}: {p}, длина = {dist[v]}")
        else:
            print(f"Путь {start} -> {v} отсутствует")
