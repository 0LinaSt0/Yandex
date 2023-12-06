'''
Базовым алгоритмом для быстрой сортировки является алгоритм partition,
который разбивает набор элементов на две части относительно заданного предиката.

Этот partition реализован на трех указателях: to_equal, to_greater and current

>>>>> ФОРМАТ ВВОДА <<<<<
В первой строке - N: количество элементов массива (0 ≤ N ≤ 106).
Во второй строке - N целых чисел ai, разделенных пробелами (-109 ≤ ai ≤ 109).
В третьей строке - опорный элемент x (-109 ≤ x ≤ 109).
Заметьте, что x не обязательно встречается среди ai.

>>>>> ФОРМАТ ВЫВОДА <<<<<
Результат работы алгоритма при использовании предиката «меньше x»:
    - в первой строке число элементов массива, меньших x
    - во второй строке количество всех остальных.
'''


from typing import List, Tuple

from .utils.exec_test import *


class Partition:

    @classmethod
    def __set_ptrs_idxs(
        cls, seq: List[int], idx_start: int, idx_next_end: int, x: int
    ) -> Tuple[int]:
        idx_equal = idx_next_end
        idx_greater = idx_next_end
        idx_current = idx_start

        while idx_current < idx_next_end:
            if (seq[idx_current] == x) & (idx_equal == idx_next_end):
                idx_equal = idx_current
            elif (seq[idx_current] < x) & (idx_equal != idx_next_end):
                seq[idx_current], seq[idx_equal] = (
                    seq[idx_equal], seq[idx_current]
                )
                idx_equal += 1
            elif seq[idx_current] > x:
                idx_greater = idx_current
                break
            idx_current += 1
        idx_current += 1
        return idx_equal, idx_greater, idx_current


    @classmethod
    def __partition_sort(
        cls, seq: List[int], idx_next_end: int, idx_current: int,
        idx_equal: int, idx_greater: int, x: int
    ) -> Tuple[int]:

        while idx_current < idx_next_end:
            if seq[idx_current] == x:
                seq[idx_current], seq[idx_greater] = (
                    seq[idx_greater], seq[idx_current]
                )
                if idx_equal == idx_next_end:
                    idx_equal = idx_greater
                idx_greater += 1
            elif seq[idx_current] < x:
                if idx_equal == idx_next_end:
                    seq[idx_current], seq[idx_greater] = (
                        seq[idx_greater], seq[idx_current]
                    )
                    idx_greater += 1
                else:
                    seq[idx_current], seq[idx_equal] = (
                        seq[idx_equal], seq[idx_current]
                    )
                    seq[idx_current], seq[idx_greater] = (
                        seq[idx_greater], seq[idx_current]
                    )
                    idx_equal += 1
                    idx_greater += 1
            idx_current += 1
        return idx_equal, idx_greater


    @classmethod
    def partition(
        cls, seq: List[int], idx_start: int, idx_next_end: int, x: int
    ) -> Tuple[int, int]:
        ''' Attention! It changes passed sequence "seq" '''
        if (x == 9):
            print('HERE1:', seq, idx_start, idx_next_end)

        idx_equal, idx_greater, idx_current = cls.__set_ptrs_idxs(
            seq, idx_start, idx_next_end, x
        )

        if idx_greater != idx_next_end:
            idx_equal, idx_greater = cls.__partition_sort(
                seq,
                idx_next_end,
                idx_current,
                idx_equal,
                idx_greater,
                x
            )
        if (x == 9):
            print('HERE2:', seq, idx_start, idx_next_end)

        return idx_equal, idx_greater


class PartitionMagic:

    def __init__(self, seq_len: int, seq: List[int]):
        self.len = seq_len
        self.seq = seq[:]


    def __count_parts(
        self, idx_equal: int, idx_greater: int) -> Tuple[int]:
        less, greater = 0, 0

        if idx_equal < self.len:
            less, greater = idx_equal, (self.len - idx_equal)
        elif greater < self.len:
            less, greater = idx_greater, (self.len - idx_greater)

        return less, greater


    def parts_len(self, x) -> Tuple[int]:

        idx_equal, idx_greater = Partition.partition(self.seq, 0, self.len, x)

        c_less, c_greater = self.__count_parts(idx_equal, idx_greater)

        return c_less, c_greater



def execution() -> None:
    c_elems = int(input())
    sequence = list(map(int, str(input()).split()))
    x = int(input())
    l, g =  PartitionMagic(c_elems, sequence).parts_len(x)

    print(l, g, sep='\n')


def main() -> None:
    exec_test(execution, 'A')
