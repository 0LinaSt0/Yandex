from typing import Callable, Any

from .inp_outp import *
from utils import testing, TestingModes


def exec_test(
    f_exec: Callable[[], Any],
    test_name: str,
    t_mode: TestingModes = TestingModes.PRINTING
) -> None:
    testing(f_exec, test_name, D_INP, D_EXPECTED, t_mode)