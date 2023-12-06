'''
Реализуйте быструю сортировку, используя алгоритм partition is A_partition.py.

На каждом шаге выбирайте опорный элемент и выполняйте partition относительно него.
Затем рекурсивно запуститесь от двух частей, на которые разбился исходный массив.

>>>>> ФОРМАТ ВВОДА <<<<<
В первой строке - число N: количество элементов массива (0 ≤ N ≤ 106).
Во второй строке - N целых чисел ai, разделенных пробелами (-109 ≤ ai ≤ 109).

>>>>> ФОРМАТ ВЫВОДА <<<<<
Выведите результат сортировки, то есть N целых чисел, разделенных пробелами.
'''


from typing import List
from random import randrange

from .A_partition import Partition
from .utils.exec_test import *
from utils import TestingModes


class QuickSort:

    @classmethod
    def __split_by(
        cls, idx_next_end: int, idx_equal: int, idx_greater: int, idx_start: int
    ) -> int:
        idx = idx_next_end

        if idx_equal < idx_next_end:
            idx = idx_equal if idx_equal != idx_start else (idx_equal + 1)
        elif idx_greater < idx_next_end:
            idx = idx_greater

        return idx


    @classmethod
    def quick_sort(
        cls, seq: List[int], idx_start: int, idx_next_end: int
    ) -> None:
        ''' Attention! It changes passed sequence "seq" '''

        if (idx_next_end - idx_start) <= 1:
            return

        idx_x = randrange(idx_start, idx_next_end)
        idx_equal, idx_greater = Partition.partition(
            seq, idx_start, idx_next_end, seq[idx_x]
        )
        idx_spliting = cls.__split_by(
            idx_next_end, idx_equal, idx_greater, idx_start
        )

        cls.quick_sort(seq, idx_start, idx_spliting)
        cls.quick_sort(seq, idx_spliting, idx_next_end)




def execution() -> None:
    seq_len = int(input())
    seq = list(map(int, str(input()).split()))
    QuickSort.quick_sort(seq, 0, seq_len)

    print(' '.join(map(str, seq)))



def main() -> None:
    exec_test(
        execution,
        'B',
        tests_count=100,
        arr_mode=ArrayModes.GENERATED_D,
        t_mode=TestingModes.COMPARING
    )
