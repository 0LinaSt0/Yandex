'''
Строка S была записана много раз подряд, после чего от получившейся строки
взяли префикс и дали вам. Ваша задача определить минимально возможную длину
исходной строки S.

>>>>> ФОРМАТ ВВОДА <<<<<
В первой и единственной строке входного файла записана строка,
которая содержит только латинские буквы, длина строки не превышает
50000 символов.

>>>>> ФОРМАТ ВЫВОДА <<<<<
Выведите ответ на задачу.
'''


from utils import TestingModes
from .utils import exec_tests
from .A_substring_equality import StringHashing, substring_equality


def find_line_base(s_inp_hashed: StringHashing) -> int:
    line_base_len = s_inp_hashed.s_len
    for l in range(1, s_inp_hashed.s_len+1):
        for sub_pos in range(l+1, s_inp_hashed.s_len+1, l):
            sub_len = l if (sub_pos + l) <= s_inp_hashed.s_len else (s_inp_hashed.s_len - sub_pos + 1)
            is_equal = substring_equality(s_inp_hashed, sub_len, 1, sub_pos)
            if is_equal is not True:
                break
        else:
            line_base_len = l
            break

    return line_base_len


def execution() -> None:
    s_inp_hashed = StringHashing(str(input()))
    print(find_line_base(s_inp_hashed))


def main() -> None:
    exec_tests(execution, 'B', t_mode=TestingModes.COMPARING)
