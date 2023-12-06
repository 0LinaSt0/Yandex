# from utils import timechecker, inp_imitation
# from warm_up import A_not_minimum
# from warm_up import B_add_two_fractions

from typing import List


import n1_hometask
import n2_hometask
import n3_hometask


d_call = {
    'n1_hometask': {
        'A': n1_hometask.A_partition.main,
        'B': n1_hometask.B_quick_sort.main,
        'C': n1_hometask.C_merging.main,
        'D': n1_hometask.D_merging_sort.main,
        'E': n1_hometask.E_radix_lsd.main
    },

    'n2_hometask': {
        'A': n2_hometask.A_substring_equality.main,
        'B': n2_hometask.B_line_base.main,
        'C': n2_hometask.C_z_function.main,
        'D': n2_hometask.D_cubes_in_the_mirror.main,
        'E': n2_hometask.E_subpolynomial.main
    },

    'n3_hometask': {
        'A': n3_hometask.A_Dijkstras.main,
    }
}


def call_tasks(module_name: str, cases_idxs: List[str]) -> None:
    for case_idx in cases_idxs:
        print(f'~~~~~~~~~~~~~~~~ DESICIONS FOR TASK {case_idx} ~~~~~~~~~~~~~~~~')
        d_call[module_name][case_idx]()
        print('\n\n')


if __name__ == '__main__':
    # call_tasks('n1_hometask', ['A', 'B', 'C', 'D', 'E'])
    # call_tasks('n2_hometask', ['A', 'B', 'C', 'D', 'E'])
    call_tasks('n3_hometask', ['A'])#, 'B', 'C', 'D', 'E'])
