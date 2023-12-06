# Graph printer: https://programforyou.ru/graph-redactor

__all__ = ['D_INP', 'D_EXPECTED']

D_MATRIX = {
    1: ['0 1 1', '4 0 1', '2 1 0'],
    2: ['0 5 0 0 0 0', '0 0 1 2 5 0', '0 0 0 0 2 0', '0 0 0 0 1 4', '0 0 0 0 0 0', '1 0 0 0 0 0']
}


D_INP = {
    'A': {
        1: ['3 2 1'] + D_MATRIX[1],
        2: ['6 1 5'] + D_MATRIX[2],
        3: ['6 6 5'] + D_MATRIX[2],
        4: ['6 5 1'] + D_MATRIX[2],
    }
}


D_EXPECTED = {
    'A': {
        1: '3\n',
        2: '8\n',
        3: '9\n'
    }
}
