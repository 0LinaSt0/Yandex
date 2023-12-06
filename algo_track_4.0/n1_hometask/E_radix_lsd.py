'''
Поразрядная сортировка является одним из видов сортировки,
которые работают практически за линейное от размера сортируемого массива время.
Такая скорость достигается за счет того, что эта сортировка использует
внутреннюю структуру сортируемых объектов.
Пусть задан массив строк s1 , ..., si причём все строки имеют одинаковую длину m.
Работа алгоритма состоит из m фаз. На i -ой фазе строки сортируются па i -ой с
конца букве. Происходит это следующим образом. Будем, для простоты, в этой
задаче рассматривать строки из цифр от 0 до 9. Для каждой цифры создается
«корзина» («bucket»), после чего строки si распределяются по «корзинам» в
соответствии с i-ой цифрой с конца. Строки, у которых i-ая с конца цифра равна
j попадают в j-ую корзину (например, строка 123 на первой фазе попадет в третью
корзину, на второй — во вторую, на третьей — в первую). После этого элементы
извлекаются из корзин в порядке увеличения номера корзины. Таким образом,
после первой фазы строки отсортированы по последней цифре, после двух фаз
— по двум последним, ..., после m фаз — по всем. При важно, чтобы элементы
в корзинах сохраняли тот же порядок, что и в исходном массиве (до начала
этой фазы). Например, если массив до первой фазы имеет вид: 111, 112, 211, 311,
то элементы по корзинам распределятся следующим образом: в первой корзине будет.
111, 211, 311, а второй: 112. Напишите программу, детально показывающую работу
этого алгоритма на заданном массиве.

>>>>> ФОРМАТ ВВОДА <<<<<
Первая строка - целое число n (1 ≤ n ≤ 1000)
Последующие n строк содержат каждая по одной строке si .Длины всех si ,
одинаковы и не превосходят 20. Все si состоят только из цифр от 0 до 9.

>>>>> ФОРМАТ ВЫВОДА <<<<<
В выходной файл выведите исходный массив строк в, состояние «корзин» после
распределения элементов по ним для каждой фазы и отсортированный массив.
Следуйте формату, приведенному в примере.

Initial array:
12, 32, 45, 67, 98, 29, 61, 35, 09
**********
Phase 1
Bucket 0: empty
Bucket 1: 61
Bucket 2: 12, 32
Bucket 3: empty
Bucket 4: empty
Bucket 5: 45, 35
Bucket 6: empty
Bucket 7: 67
Bucket 8: 98
Bucket 9: 29, 09
**********
Phase 2
Bucket 0: 09
Bucket 1: 12
Bucket 2: 29
Bucket 3: 32, 35
Bucket 4: 45
Bucket 5: empty
Bucket 6: 61, 67
Bucket 7: empty
Bucket 8: empty
Bucket 9: 98
**********
Sorted array:
09, 12, 29, 32, 35, 45, 61, 67, 98

'''


from .utils.exec_test import *

from typing import Dict, List, Tuple


SEPARATOR = '**********'


class StableCountingSort:

    @classmethod
    def __elems_counter(
        cls, idx_sorted_by: int, l_sort: List[str]) -> List[int]:
        r_count = [0] * 10
        for elem in l_sort:
            r_count[int(elem[idx_sorted_by])] += 1
        return r_count


    @classmethod
    def __first_indexes_definer(
        cls, count: List[int], iter_num: int
    ) -> List[int]:
        idxs_retruned = [0]
        idx_current = 0

        for idx in range(iter_num):
            idx_current += count[idx]
            idxs_retruned.append(idx_current)

        return idxs_retruned


    @classmethod
    def sc_sort(
        cls, idx_sorted_by: int, l_sort: List[str], l_size: int
    ) -> Tuple[List[str], Dict[int, List[str]]]:
        l_returned = [None] * l_size
        d_returned = {i: [] for i in range(10)}
        count = cls.__elems_counter(idx_sorted_by, l_sort)
        idxs_start = cls.__first_indexes_definer(count, 9)

        for elem in l_sort:
            current_value = int(elem[idx_sorted_by])

            d_returned[current_value].append(elem)

            l_returned[idxs_start[current_value]] = elem
            idxs_start[current_value] += 1

        return l_returned, d_returned


class RadixLSD:

    def __init__(self, seq_len: int, seq: List[int]) -> None:
        self.seq = seq[:]
        self.len = seq_len
        self.discharge_count = len(self.seq[0]) if len(self.seq) else 0


    def __print_buckets(self, buskets: Dict[int, List[str]], n_phase: int) -> None:
        print(f'Phase {n_phase}')
        for key, value in buskets.items():
            nums = 'empty' if len(value) == 0 else ', '.join(value)
            print(f'Bucket {key}: ', end='')
            print(nums)


    def radix_lsd_sort(self):
        idx_next_last_discharge = (self.discharge_count + 1) * -1

        for discharge in range(-1, idx_next_last_discharge, -1):
            self.seq, current_buckets = StableCountingSort.sc_sort(
                discharge, self.seq, self.len
            )
            self.__print_buckets(current_buckets, (discharge * -1))
            print(SEPARATOR)

        return self.seq


def print_array(text: str, printed: List[str], is_sep: bool = False) -> None:
    print(text)
    print(', '.join(printed))
    if is_sep:
        print(SEPARATOR)


def execution():
    n = int(input())
    l_inp = [str(input()) for _ in range(n)]

    print_array('Initial array:', l_inp, is_sep=True)

    alg = RadixLSD(n, l_inp)
    l_sorted = alg.radix_lsd_sort()

    print_array('Sorted array:', l_sorted)



def main() -> None:
    exec_test(execution, 'E')
