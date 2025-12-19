"""Демонстрация работы алгоритмов Краскала и Прима (ЛР19).

Запуск этого скрипта распечатает MST, найденные двумя алгоритмами, и их суммарный вес.
"""
from mst_kruskal import kruskal
from mst_prim import prim


def demo():
    # Пример связного неориентированного взвешенного графа
    mat = [
        [0, 2, 0, 6, 0],
        [2, 0, 3, 8, 5],
        [0, 3, 0, 0, 7],
        [6, 8, 0, 0, 9],
        [0, 5, 7, 9, 0],
    ]

    print("Матрица смежности:")
    for row in mat:
        print(row)

    print("\n--- Kruskal ---")
    mst_k, total_k = kruskal(mat)
    print("Рёбра MST (Kruskal):")
    for u, v, w in mst_k:
        print(f"  {u} - {v} (w={w})")
    print("Суммарный вес:", total_k)

    print("\n--- Prim ---")
    mst_p, total_p = prim(mat, start=0)
    print("Рёбра MST (Prim):")
    for u, v, w in mst_p:
        print(f"  {u} - {v} (w={w})")
    print("Суммарный вес:", total_p)


if __name__ == "__main__":
    demo()
