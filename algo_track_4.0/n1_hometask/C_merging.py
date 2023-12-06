'''
Базовый алгоритм для сортировки слиянием — алгоритм слияния двух упорядоченных
массивов в один упорядоченный массив. Эта операция выполняется за линейное время
с линейным потреблением памяти

>>>>> ФОРМАТ ВВОДА <<<<<
В первой строке - число N: количество элементов первого массива (0 ≤ N ≤ 106).
Во второй строке - N целых чисел ai, разделенных пробелами,
                    отсортированные по неубыванию (-109 ≤ ai ≤ 109).
В третьей строке - число M: количество элементов второго массива (0 ≤ M ≤ 106).
В четвертой строке - M целых чисел bi, разделенных пробелами,
                    отсортированные по неубыванию (-109 ≤ bi ≤ 109).

>>>>> ФОРМАТ ВЫВОДА <<<<<
Выведите результат слияния этих двух массивов, то есть M + N целых чисел,
разделенных пробелами, в порядке неубывания.
'''


from typing import List

from utils import TestingModes
from .utils.exec_test import *


def merging(a: List[int], len_a: int, b: List[int], len_b: int) -> List[int]:
    idx_a, idx_b = 0, 0
    l_result = []

    while (idx_a < len_a) & (idx_b < len_b):
        if a[idx_a] <= b[idx_b]:
            insert_elem = a[idx_a]
            idx_a += 1
        else:
            insert_elem = b[idx_b]
            idx_b += 1
        l_result.append(insert_elem)

    l_result += [a[idx] for idx in range(idx_a, len_a)]
    l_result += [b[idx] for idx in range(idx_b, len_b)]

    return l_result


def execution():
    len_a = int(input())
    l_a = list(map(int, str(input()).split()))
    len_b = int(input())
    l_b = list(map(int, str(input()).split()))

    l_merged = merging(l_a, len_a, l_b, len_b)
    result = ' '.join(map(str, l_merged))

    print(result)


def main() -> None:
    exec_test(
        execution,
        'C',
        arr_mode=ArrayModes.GENERATED_D,
        t_mode=TestingModes.COMPARING
    )
