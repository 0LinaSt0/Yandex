__all__ = ['D_INP', 'D_EXPECTED']


D_INP = {
    'A': {
        1: ['acabaca', '3', '4 3 2', '3 4 0', '2 0 1'],
        2: ['caeabaeadedcbdcdccec', '10', '13 4 3', '2 12 15', '10 1 3',
            '3 8 15', '13 5 6', '7 2 6', '9 8 8', '19 0 0', '19 0 0', '6 7 13'],
        3: ['1234123123', '2', '3 0 4', '1 1 5'],
        4: ['', '0']
    },
    'B': {
        1: ['zzz'],
        2: ['bcabcab'],
        3: ['qwertyu'],
        4: ['1231231'],
        5: ['121212121'],
        6: ['1121121121'],
        7: ['aaaaabaaaaabaaaaabaaa'],
        8: [''],
        9: ['a'],
        10: ['fd'],
        11: ['fgh'],
        12: ['qwertyuiopasdfghjklzxcvbnq']
    },
    'C': {
        1: ['abracadabra'],
        2: [''],
        3: ['aaaaa'],
        4: ['qwertyq'],
        5: ['baaaaa'],
        6: ['a'],
        7: ['qwerqwerqwerqwq'],
        8: ['qwqwqwqwqwqwqwwe'],
        9: ['abracadabraabracadabra'],
        10: ['lllklllklkklk'],
        11: ['ww'],
        12: ['qw']
    },
    'D': {
        1: ['6 2', '1 1 2 2 1 1'],
        2: ['5 5', '1 2 3 4 5'],
        3: ['1 1', '1'],
        4: ['7 2', '1 1 1 1 1 1 2'],
        5: ['8 3', '1 2 3 3 3 2 1 1'],
        6: ['9 3', '1 1 2 3 3 2 1 1 3'],
        7: ['10 1', '1 1 1 1 1 1 1 1 1 1'],
        8: ['3 1', '1 1 1'],
        9: ['9 3', '1 2 3 1 2 3 1 2 3'],
        10: ['7 2', '1 2 1 2 1 2 1'],
        11: ['8 4', '1 1 1 1 2 1 1 1'],
        12: ['10 10', '1 2 3 4 5 6 7 8 9 10']
    },
    'E': {
        1: ['aaa'],
        2: ['aba'],
        3: ['abcdefg'],
        4: ['abacadaba'],
        5: ['']
    }
}

D_EXPECTED = {
    'A': {
        1: 'no\nyes\nno\n',
        2: 'no\nno\nno\nno\nno\nno\nyes\nyes\nyes\nno\n',
        3: 'yes\nyes\n',
        4: ''
    },
    'B': {
        1: '1\n',
        2: '3\n',
        3: '7\n',
        4: '3\n',
        5: '2\n',
        6: '3\n',
        7: '6\n',
        8: '0\n',
        9: '1\n',
        10: '2\n',
        11: '3\n',
        12: '25\n'
    },
    'C': {
        1: '0 0 0 1 0 1 0 4 0 0 1\n',
        2: '0\n',
        3: '0 1 2 2 1\n',
        4: '0 0 0 0 0 0 1\n',
        5: '0 0 0 0 0 0\n',
        6: '0\n',
        7: '0 0 0 0 4 0 0 0 6 0 0 0 2 0 1\n',
        8: '0 0 2 0 4 0 6 0 6 0 4 0 2 0 0 0\n',
        9: '0 0 0 1 0 1 0 4 0 0 1 11 0 0 1 0 1 0 4 0 0 1\n',
        10: '0 1 1 0 4 2 1 0 1 0 0 1 0\n',
        11: '0 1\n',
        12: '0 0\n'
    },
    'D': {
        1: '3 5 6\n',
        2: '5\n',
        3: '1\n',
        4: '4 5 6 7\n',
        5: '8\n',
        6: '5 8 9\n',
        7: '5 6 7 8 9 10\n',
        8: '2 3\n',
        9: '9\n',
        10: '7\n',
        11: '6 7 8\n',
        12: '10\n'
    },
    'E': {
        1: '6\n',
        2: '4\n',
        3: '7\n',
        4: '13\n',
        5: '0\n'
    }
}