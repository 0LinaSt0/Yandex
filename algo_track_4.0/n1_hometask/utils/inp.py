__all__ = ['D_INP']


D_INP = {
    'A': {
        # less=2, another=3
        1: ['5', '1 9 4 2 3', '3'],
        # less=0, another=4
        2: ['4', '1 1 1 1', '1'],
        # less=4, another=0
        3: ['4', '1 1 1 1', '2'],
        # Doesnt have x : less=4, another=0
        4: ['4', '1 1 1 1', '0'],

        5: ['0', '', '0'],

        6: ['1', '0', '0']
    },

    'B': {
        # 1 2 3 4 9
        1: ['5', '1 9 4 2 3'],

        # 1 1 1 1
        2: ['4', '1 1 1 1'],

        # 0 1 1 1 1 1 3 4 5 6 9 85
        3: ['12', '1 5 1 3 6 1 1 9 85 4 0 1'],

        4: ['0', ''],

        5: ['1', '0'],

        6: ['4', '-12 -11 -12 -6']
    },
    'C': {
        # 1 2 3 5 5 5 6 9
        1: ['5', '1 3 5 5 9', '3', '2 5 6'],
        # 0
        2: ['1', '0', '0', ''],
        # 0
        3: ['0', '', '1', '0'],
        # empty
        4: ['0', '', '0', ''],
    },
    'E': {
        1: ['9', '12', '32', '45', '67', '98', '29', '61', '35', '09']
    }
}
