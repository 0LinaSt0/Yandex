'''
Дан ориентированный взвешенный граф. Найдите кратчайшее
расстояние от одной заданной вершины до другой.

>>>>> ФОРМАТ ВВОДА <<<<<
В первой строке содержатся три числа: N, S и F (1≤ N ≤ 100, 1 ≤ S, F ≤ N),
где N — количество вершин графа, S — начальная вершина, а F — конечная.
В следующих N строках вводится по N чисел, не превосходящих 100,
– матрица смежности графа, где -1 означает что ребра между вершинами нет,
а любое неотрицательное число — наличие ребра данного веса. На главной
диагонали матрицы записаны нули.

>>>>> ФОРМАТ ВЫВОДА <<<<<
Выведите искомое расстояние или -1, если пути между указанными вершинами
не существует.
'''

from .algo_implementation import *
from .utils import exec_test
from utils import TestingModes


def graph_to_adj_matrix(v_count: int) -> VerticesMatrix:
    l_vertices = []

    for _ in range(0, v_count):
        current_weights = list(map(int, str(input()).split()))
        l_vertices.append(current_weights)

    vertises = VerticesMatrix(v_count, l_vertices)

    return vertises


def graph_to_adj_list(v_count: int) -> VerticesList:
    vertises = VerticesList()

    for from_idx in range(1, v_count + 1):
        current_weights = list(map(int, str(input()).split()))
        for to_idx in range(1, v_count + 1):
            vertises.set_vertex(from_idx, to_idx, current_weights[to_idx-1])

    return vertises


def execution() -> None:
    dijkstras_algo = Dijkstras()
    v_count, v_from, v_to = map(int, str(input()).split())

    vertises = graph_to_adj_list(v_count)
    # vertises = graph_to_adj_matrix(v_count)

    # print(vertises(), vertises.inverse_vertices, vertises.v_count, sep='\n')
    dist = dijkstras_algo.define_distance(vertises, v_from, v_to)
    print(dist)


def main() -> None:
    exec_test(execution, 'A', t_mode=TestingModes.PRINTING)
