'''
Даны две рациональные дроби: a/b и c/d. Сложите их и
результат представьте в виде несократимой дроби m/n.

>>>>> ФОРМАТ ВВОДА <<<<<
Программа получает на вход 4 натуральных числа a, b, c, d,
каждое из которых не больше 100.

>>>>> ФОРМАТ ВЫВОДА <<<<<
Программа должна вывести два натуральных числа m и n такие,
что m/n=a/b+c/d и дробь m/n – несократима.
'''

from typing import Callable, Any
from utils import inp_imitation


'''FOR TESTING'''

inp = {
    1: '1 2 1 2'
}

def check_cases(f_calling: Callable[[Any], None]) -> None:
    for key, item in inp.items():
        print(f'>>>>CASE_{key}<<<<')
        inp_imitation(f_calling, l_inp=[item, ])
        print(end='\n\n')

'''~~~~~~~~~~~'''

def greatest_common_divisor(n_a: int, n_b: int) -> int:
    while n_b:
        n_a, n_b = n_b, (n_a % n_b)
    return n_a

def form_answer() -> None:
    a, b, c, d = list(map(int, str(input()).split()))
    numerator = a + c
    denominator = (b if b == d else b * d)
    gcd = greatest_common_divisor(numerator, denominator)
    print((numerator // gcd), (denominator // gcd))


check_cases(form_answer)
