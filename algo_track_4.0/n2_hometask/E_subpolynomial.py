'''
Строка называется палиндромом, если она читается одинаково как слева направо,
так и справа налево. Например, строки abba, ata являются палиндромами.

Вам дана строка. Ее подстрокой называется некоторая непустая последовательность
подряд идущих символов. Напишите программу, которая определит, сколько подстрок
данной строки является палиндромами.

>>>>> ФОРМАТ ВВОДА <<<<<
Вводится одна строка, состоящая из прописных латинских букв.
Длина строки не превышает 100000 символов.

>>>>> ФОРМАТ ВЫВОДА <<<<<
Выведите одно число — количество подстрок данной строки,
которые являются палиндромами
'''


from .D_cubes_in_the_mirror import *
from .utils import exec_tests
from utils import TestingModes


def subpolynomial_count(inp_hashed: HashingFromBothEnds) -> int:
    subpoly_count = 0

    for idx in range(1, inp_hashed.s_len + 1):
        for sub_len in range(1, inp_hashed.s_len - idx + 2):
            is_equal = two_dimentional_substring_equality(
                inp_hashed,
                sub_len,
                idx,
                (-1 * idx) - sub_len + 1
            )

            if is_equal:
                subpoly_count += 1

    return subpoly_count


def execution() -> None:
    s_inp = str(input())
    inp_hashed = HashingFromBothEnds(s_inp, len(s_inp))
    print(subpolynomial_count(inp_hashed))


def main() -> None:
    exec_tests(execution, 'E', t_mode=TestingModes.COMPARING)
