import io
import sys

from unittest.mock import patch
from typing import Callable, Any, List, Dict
from enum import Enum

__all__ = ['testing', 'TestingModes']


class TestingModes(Enum):
    PRINTING = 1
    COMPARING = 2


def input_simulation(
    f_exec: Callable[[Any], Any], inp: List, f_args: list = list()
) -> None:
    with patch("builtins.input", side_effect=inp):
        f_exec(*f_args)


def compare_results(item: Any, expected: str, result: str) -> None:
    if expected == result:
        print("Correct")
    else:
        print("!Wrong!")
        print(f'Passed: {item}\n')
        print(f'{expected[:-1]} <- expected')
        print(f'{result[:-1]} <- result')
        print('\n\n')


def testing(
    f_exec: Callable[[], Any],
    test_name: str,
    d_inp: Dict[str, Dict[int, List[str]]],
    d_expected: Dict[str, Dict[int, str]],
    t_mode: TestingModes = TestingModes.PRINTING
) -> None:
    for key, item in d_inp[test_name].items():
        print(f'>>>CASE_{key}<<<')
        if t_mode == TestingModes.COMPARING:
            output = io.StringIO()
            sys.stdout = output
            input_simulation(f_exec, item)
            r_output = output.getvalue()
            sys.stdout = sys.__stdout__
            expected = d_expected[test_name][key]

            compare_results(item, expected, r_output)
        else:
            input_simulation(f_exec, item)
            print('\n\n')
