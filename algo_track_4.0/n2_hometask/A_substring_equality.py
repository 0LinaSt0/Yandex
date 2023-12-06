'''
Дана строка S, состоящая из строчных латинских букв.

Определите, совпадают ли строки одинаковой длины L, начинающиеся с позиций A и B.

>>>>> ФОРМАТ ВВОДА <<<<<
- В первой строке: S (1 ≤ |S| ≤ 2 ⋅ 105), состоящая из строчных латинских букв.
- Во второй строке: число Q (1 ≤ Q ≤ 2 ⋅ 105) — количество запросов.
- В следющих Q строках запросы:
    целые числа L, A и B (1 ≤ L ≤ |S|, 0 ≤ A, B ≤ (|S| - L))
    длина подстрок и позиции, с которых они начинаются.

>>>>> ФОРМАТ ВЫВОДА <<<<<
Если строки совпадают — выведите "yes", иначе — "no".
'''

from typing import Tuple, List

from .utils import exec_tests
from utils import TestingModes


__all__ = ['StringHashing', 'substring_equality', 'main']


class StringHashing:

    def __init__(self, s_inp: str, p: int = (10**9 + 7), x: int = 257):
        self.p = p
        self.x = x
        self.s = ('_' + s_inp)
        self.s_len = len(s_inp)
        self.hashes, self.xs = self.__hashing()

    def __call__(self):
        return self.hashes

    def __hashing(self) -> Tuple[List[int], List[int]]:
        '''
        h[0] = 0
        h[1] = 0*x + s[0]                                           | (h[0]*x + s[idx])
        h[2] = 0*x^2 + s[0]*x + s[1]                                | (h[1]*x + s[1])
        h[3] = 0*x^3 + s[0]*x^2 + s[1]*x + s[2]                     | (h[2]*x + s[2])
        h[4] = 0*x^4 + s[0]*x^3 + s[1]*x^2 + s[2]*x + s[3]          | (h[3]*x + s[3])
                                ............
        h[n] = 0*x^n + s[0]*x^(n-1) + s[1]*x^(n-2) + ... + s[n-1]   | (h[n-1]*x + s[n-1])
        '''

        hashes = [0] * (self.s_len + 1)
        xs = [0] * (self.s_len + 1)

        xs[0] = 1

        for idx in range(1, self.s_len + 1):
            hashes[idx] = (hashes[idx - 1] * self.x + ord(self.s[idx])) % self.p
            xs[idx] = (xs[idx - 1] * self.x) % self.p

        return hashes, xs


def substring_equality(
    hashed: StringHashing, sub_len: int, from_1: int, from_2: int
) -> bool:
    '''
    Comparing two substrings:

    hash_sub1 = h[from1 + len - 1] - h[from1 - 1] * x^len
    hash_sub2 = h[from2 + len - 1] - h[from2 - 1] * x^len
    =>
    [hash_sub1 == hash_sub2] = [(h[from1 + len - 1] + h[from2 - 1] * x^len) == (h[from2 + len - 1] + h[from1 - 1] * x^len)]
    '''

    is_compare = (
        (hashed()[from_1 + sub_len - 1] +
            hashed()[from_2 - 1] * hashed.xs[sub_len]) % hashed.p
        ==
        (hashed()[from_2 + sub_len - 1] +
            hashed()[from_1 - 1] * hashed.xs[sub_len]) % hashed.p
    )

    return is_compare


def execution() -> None:
    s_inp_hashed = StringHashing(str(input()))
    query_count = int(input())
    compared_conditions = []

    for _ in range(query_count):
        current_q = list(map(int, str(input()).split()))
        current_q[1] += 1
        current_q[2] += 1
        compared_conditions.append(current_q)
        print('yes' if substring_equality(s_inp_hashed, *current_q) else 'no')


def main() -> None:
    exec_tests(execution, 'A', t_mode=TestingModes.COMPARING)
