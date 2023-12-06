'''
Задана последовательность целых чисел a1, a2, …, an.
Задаются запросы: сказать любой элемент последовательности на отрезке от L до R
включительно, не равный минимуму на этом отрезке.

>>>>> ФОРМАТ ВВОДА <<<<<
В первой строке содержатся два целых числа:
    - N, 1 ≤ N ≤ 100 - длина последовательности
    - M, 1 ≤ M ≤ 1000 - количество запросов

Во второй строке — сама последовательность, 0 ≤ ai ≤ 1000.

Начиная с третьей строки перечисляются M запросов,
состоящих из границ отрезка L и R, где L, R - индексы массива,
нумеруются с нуля.

>>>>> ФОРМАТ ВЫВОДА <<<<<
На каждый запрос вывести в отдельной строке ответ:
    - любой элемент на [L, R], кроме минимального.
    - если такого элемента нет 'NOT FOUND'
'''

from typing import List, Callable, Any, Iterator
from itertools import islice

from utils import inp_imitation

'''FOR TESTING'''

inp = {
    # as in example_1
    1: ['10 5', '1 1 1 2 2 2 3 3 3 10',
        '0 1', '0 3', '3 4', '7 9', '3 7'],
    # as in example_2
    2: ['4 2', '1 1 1 2', '0 2', '0 3'],
    # ranges on one element
    3: ['9 5', '1 2 3 4 5 6 7 8 9',
        '0 8', '0 0', '5 5', '1 6', '7 8'],
    # same value of all elements
    4: ['5 3', '0 0 0 0 0', '0 4', '0 1', '2 4'],
    # the most minimal sequence
    5: ['1 1', '455', '0 0'],
    # unsorted sequence
    6: ['14 6', '2 85 644 1000 2 4 7 6 15 2 3 5 3 24',
        '0 3', '3 10', '5 5', '6 13', '0 13', '10 12']
}


def check_cases(f_calling: Callable[[Any], None]) -> None:
    for key, item in inp.items():
        print(f'>>>>CASE_{key}<<<<')
        inp_imitation(f_calling, l_inp=item)
        print(end='\n\n')

'''~~~~~~~~~~~'''



def take_indexes(m: int) -> List[List[int]]:
    indexes = list()
    for _ in range(m):
        idx_range = list(map(int, str(input()).split()))
        indexes.append(idx_range)
    return indexes


def find_min(sub_seq: Iterator, sub_len: int) -> str:
    min_elem = next(sub_seq)
    for _ in range(1, sub_len):
        current = next(sub_seq)
        if current < min_elem:
            min_elem = current
        elif current > min_elem:
            return str(current)
    return 'NOT FOUND'


def form_answers() -> None:
    _, m = map(int, str(input()).split())
    l_sequence = list(map(int, str(input()).split()))
    indexes = take_indexes(m)

    for idx_range in indexes:
        start, end = idx_range
        sub_seq = islice(l_sequence, start, (end + 1))
        print(find_min(sub_seq, (end - start + 1)))


check_cases(form_answers)
