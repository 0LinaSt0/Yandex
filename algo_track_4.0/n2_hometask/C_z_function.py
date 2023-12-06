'''
Дана непустая строка S, длина которой N не превышает 106.
Будем считать, что элементы строки нумеруются от 0 до N-1.

Вычислите z-функцию z[i] для всех i от 0 до N-1.
z[i] определяется как максимальная длина подстроки,
начинающейся с позиции i и совпадающей с префиксом всей строки.
z[0] = 0

>>>>> ФОРМАТ ВВОДА <<<<<
Одна строка длины N, 0 < N ≤ 106, состоящая из прописных латинских букв.

>>>>> ФОРМАТ ВЫВОДА <<<<<
Выведите N чисел — значения z-функции для каждой позиции, разделённые пробелом.
'''


from utils import TestingModes
from .utils import exec_tests
from .A_substring_equality import *


def z_function(s_hashed: StringHashing, start_pos: int) -> int:
    max_sub_len = 0

    possible_max_sub_len = min(
        (start_pos - 1), (s_hashed.s_len - start_pos + 1)
    )

    for current_len in range(possible_max_sub_len, 0, -1):
        is_equal = substring_equality(s_hashed, current_len, 1, start_pos)
        if is_equal:
            max_sub_len = current_len
            break

    return max_sub_len



def compare_result(s_hashed: StringHashing) -> str:
    result_str = '0'
    for idx in range(2, s_hashed.s_len + 1):
        result_str += ' ' + str(z_function(s_hashed, idx))
    return result_str


def execution() -> None:
    s_inp_hashed = StringHashing(str(input()))
    print(compare_result(s_inp_hashed))


def main() -> None:
    exec_tests(execution, 'C', t_mode=TestingModes.COMPARING)
