'''
Реализуйте сортировку слиянием, используя алгоритм merging из C_merging.py.

На каждом шаге делите массив на две части, сортируйте их независимо
и сливайте с помощью уже реализованной функции.

>>>>> ФОРМАТ ВВОДА <<<<<
В первой строке - число N: количество элементов массива (0 ≤ N ≤ 106).
Во второй строке - N целых чисел ai, разделенных пробелами (-109 ≤ ai ≤ 109).

>>>>> ФОРМАТ ВЫВОДА <<<<<
Выведите результат сортировки, то есть N целых чисел, разделенных пробелами,
в порядке неубывания.
'''


from typing import List

from utils import TestingModes
from .utils.exec_test import *
from .C_merging import merging


def merging_sort(l: List[int], idx_start: int, idx_next_end: int) -> List[int]:
    dif = idx_next_end - idx_start
    if dif <= 1:
        return [l[idx_start]] if dif else ['']
    sep = dif // 2 + idx_start
    left_list = merging_sort(l, idx_start, sep)
    right_list = merging_sort(l, sep, idx_next_end)
    merged = merging(left_list, len(left_list), right_list, len(right_list))
    return merged


def execution():
    len_inp = int(input())
    inp = list(map(int, str(input()).split()))
    l_sorted = merging_sort(inp, 0, len_inp)
    result = ' '.join(map(str, l_sorted))

    print(result)


def main() -> None:
    exec_test(
        execution,
        'D',
        arr_mode=ArrayModes.GENERATED_D,
        t_mode=TestingModes.COMPARING
    )
