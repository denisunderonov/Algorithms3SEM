"""Демонстрация алгоритма Дейкстры (ЛР18).

Запуск покажет минимальные расстояния и восстановленные кратчайшие пути.
Формат матрицы: 0 — ребра нет, положительное число — вес ребра.
"""
from dijkstra import dijkstra, reconstruct_path


def demo():
    # Пример из учебных материалов
    mat = [
        [0, 7, 9, 0, 0, 14],
        [0, 0, 10, 15, 0, 0],
        [0, 0, 0, 11, 0, 2],
        [0, 0, 0, 0, 6, 0],
        [0, 0, 0, 6, 0, 9],
        [0, 0, 0, 0, 0, 0],
    ]
    start = 0
    print("Матрица взвешенной смежности (0 = нет ребра):")
    for row in mat:
        print(row)

    dist, prev = dijkstra(mat, start)
    print(f"\nМинимальные расстояния от вершины {start}:")
    for i, d in enumerate(dist):
        print(f"  {start} -> {i} = {d}")

    print("\nПримеры восстановленных путей:")
    for target in range(len(mat)):
        path = reconstruct_path(prev, start, target)
        if path:
            print(f"  {start} -> {target}: {path} (длина {dist[target]})")
        else:
            print(f"  {start} -> {target}: путь отсутствует")


if __name__ == "__main__":
    demo()
