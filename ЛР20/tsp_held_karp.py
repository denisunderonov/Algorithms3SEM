"""TSP: точное решение методом Held-Karp (динамическое программирование по битмаске).

Особенности реализации:
- Граф задаётся матрицей весов `matrix` размера n x n.
- Значение `matrix[i][j]` должно быть положительным числом — вес ребра i->j.
  Если ребра нет, используйте `math.inf` или большое число; в этой учебной реализации
  0 считается отсутствием ребра за исключением диагонали.
- Функция `held_karp(matrix, start=0)` возвращает кортеж `(cost, path)`, где path —
  цикл, начинающийся и заканчивающийся в `start` (если цикл существует), либо пустой список.

Сложность: O(n^2 * 2^n) по времени и O(n * 2^n) по памяти — подходит для n ≲ 20.
"""
from typing import List, Tuple
import math


def held_karp(matrix: List[List[float]], start: int = 0) -> Tuple[float, List[int]]:
    """Выполнить Held-Karp для матрицы весов.

    Параметры:
    - matrix: квадратная матрица весов (n x n). matrix[i][j] > 0 — вес ребра i->j.
              Для отсутствия ребра можно использовать math.inf.
    - start: стартовая вершина (по умолчанию 0).

    Возвращает (min_cost, path). `path` — список вершин в порядке посещения, начиная и
    заканчивая `start`. Если гамильтонов круг не найден (например, граф несвязный),
    возвращается (math.inf, []).
    """
    if not matrix or any(len(row) != len(matrix) for row in matrix):
        raise ValueError("Матрица весов должна быть квадратной и не пустой")
    n = len(matrix)
    if not (0 <= start < n):
        raise IndexError("start вне диапазона вершин")

    # Если n == 1 — тривиальный случай
    if n == 1:
        return 0.0, [start, start]

    # Приведём нули (кроме диагонали) к inf, т.к. 0 в учебных матрицах обычно означает отсутствие ребра
    W = [[(math.inf if (i != j and matrix[i][j] == 0) else matrix[i][j]) for j in range(n)] for i in range(n)]

    # dp[mask][v] = минимальная стоимость пройти по множеству mask (mask включает старт и v), закончить в v
    # Представление: mask — int 0..(1<<n)-1
    # Для экономии памяти можно хранить только маски, содержащие старт и размер > 0.

    # Используем словари для строк dp[mask] -> list по вершинам
    N = 1 << n
    dp = [ [math.inf]*n for _ in range(N) ]
    parent = [ [ -1 ]*n for _ in range(N) ]

    start_mask = 1 << start
    dp[start_mask][start] = 0.0

    # Итерируем по маскам, содержащим start
    for mask in range(N):
        if not (mask & start_mask):
            continue
        for u in range(n):
            if not (mask & (1 << u)):
                continue
            cur = dp[mask][u]
            if cur == math.inf:
                continue
            # попробовать добавить v, который ещё не в mask
            rem = (~mask) & (N - 1)
            v = rem
            while v:
                # перебираем биты из rem
                lsb = v & -v
                nxt = (lsb.bit_length() - 1)
                # релаксация u -> nxt
                w = W[u][nxt]
                if w != math.inf:
                    new_mask = mask | (1 << nxt)
                    new_cost = cur + w
                    if new_cost < dp[new_mask][nxt]:
                        dp[new_mask][nxt] = new_cost
                        parent[new_mask][nxt] = u
                v = v & (v - 1)

    full_mask = (1 << n) - 1
    best = math.inf
    last = -1
    # завершить цикл — вернуться в старт
    for u in range(n):
        if u == start:
            continue
        if dp[full_mask][u] == math.inf:
            continue
        w = W[u][start]
        if w == math.inf:
            continue
        cost = dp[full_mask][u] + w
        if cost < best:
            best = cost
            last = u

    if best == math.inf:
        return math.inf, []

    # Восстановление пути: идём от (full_mask, last) по parent до start.
    # Собираем узлы от last до start (исключая дополнительное добавление start дважды),
    # затем обращаем порядок и добавляем start в конец, чтобы получить цикл.
    path_rev = []
    mask = full_mask
    cur = last
    while cur != -1 and cur != start:
        path_rev.append(cur)
        prev = parent[mask][cur]
        mask = mask ^ (1 << cur)
        cur = prev

    # Если мы не достигли start — восстановление не удалось
    if cur != start:
        return math.inf, []

    path_rev.append(start)
    path = list(reversed(path_rev))
    # Закрываем цикл, добавив старт в конец
    path.append(start)
    return best, path


if __name__ == "__main__":
    # Небольшой тестовый пример (симметричная матрица расстояний)
    mat = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0],
    ]
    cost, path = held_karp(mat, start=0)
    print("TSP Held-Karp:")
    print("Cost:", cost)
    print("Path:", path)
