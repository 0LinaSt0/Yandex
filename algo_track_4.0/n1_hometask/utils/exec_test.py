from enum import Enum
from typing import Dict, List, Any, Callable
from random import randint

from .inp import *
from utils import testing, TestingModes


__all__ = ['ArrayModes', 'exec_test']


class ArrayModes(Enum):
    DEFAULT_D = 1
    GENERATED_D = 2


def random_list_generator(
    max_len: int, range_from_to: List[int], sort_mode: bool = False
    ) -> List[str]:
    len_random = randint(0, max_len)
    l_inp = list()
    for _ in range(len_random):
        l_inp.append(randint(*range_from_to))
    if sort_mode:
        l_inp = sorted(l_inp)
    return [str(len_random), ' '.join(map(str, l_inp))]


def testing_dict(test_name: str, how_many_tests: int = 10) -> dict:
    max_lens_count = 1_00
    range_from_to = [-1_000_000, 1_000_000]
    testing_d = {test_name: {}}

    if test_name == 'B' or test_name == 'D':
        for test in range(1, how_many_tests + 1):
            current = random_list_generator(max_lens_count, range_from_to)
            testing_d[test_name][test] = current
    elif test_name == 'C':
        for test in range(1, how_many_tests + 1):
            a_current = random_list_generator(max_lens_count, range_from_to, sort_mode=True)
            b_current = random_list_generator(max_lens_count, range_from_to, sort_mode=True)
            testing_d[test_name][test] = a_current + b_current
    return testing_d


def test_name_preparation(test_name: str) -> str:
    return 'B' if test_name == 'D' else test_name


def d_inp_preparation(
    arr_mode: ArrayModes, test_name: str, tests_count
) -> Dict[str, Dict[int, List[str]]]:
    d_inp = (
        D_INP if arr_mode == ArrayModes.DEFAULT_D else testing_dict(
            test_name, tests_count
        )
    )

    return d_inp


def expected_parser(
    test_name: str, d_inp: Dict[str, Dict[int, List[str]]]
) -> Dict[str, Dict[int, str]]:

    if test_name == 'B' or test_name == 'D':
        f_expect_generator = (
            lambda item: ' '.join(
                map(str, sorted(list(map(int, item[1].split()))))
            ) + '\n'
        )
    elif test_name == 'C':
        f_expect_generator = (
            lambda item: ' '.join(map(str, sorted(list(
                map(int, item[1].split())) + list(map(int, item[3].split())
            )))) + '\n'
        )
    else:
        f_expect_generator = (
            lambda _:
                f'The test for {test_name} and item has not been developed'
        )

    d_expected = {test_name: {}}


    for key, item in d_inp[test_name].items():
        d_expected[test_name][key] = f_expect_generator(item)

    return d_expected


def exec_test(
    f_exec: Callable[[], Any],
    test_name: str,
    tests_count: int = 10,
    arr_mode: ArrayModes = ArrayModes.DEFAULT_D,
    t_mode: TestingModes = TestingModes.PRINTING
) -> None:

    test_name = test_name_preparation(test_name)
    d_inp = d_inp_preparation(arr_mode, test_name, tests_count)
    d_expected = expected_parser(test_name, d_inp)

    testing(f_exec, test_name, d_inp, d_expected, t_mode)
