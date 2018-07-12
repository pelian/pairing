from pairing import *
import numpy as np

# Test variables
LB = -100000 # Random integer lower bound
UB = 100000 # Random integer upper bound
TESTS = 10000 # Number of test runs

def pairing_test(lower: int, upper: int, tests: int):
    cp_error = []
    sp_error = []
    sxp_error = []
    for test in range(tests):
        x = np.random.randint(lower, upper)
        y = np.random.randint(lower, upper)
        print('\n')
        # Pair and unpair using Cantor pairing algorithm
        cp = cantor_pair((x, y))
        cu = cantor_unpair(cp)
        print('({}, {}) - Cantor unpair: {}, Cantor pair {}'.format(x, y, cu, cp))
        if cu[0] != x or cu[1] != y:
            cp_error.append([test, (x, y), cu])
            print('error in Cantor pairing function')

        # Pair and unpair using Szudzik pairing algorithm
        sp = szudzik_pair((x, y))
        su = szudzik_unpair(sp)
        print('({}, {}) - Szudzik A unpair: {}, Szudzik A pair {}'.format(x, y, su, sp))
        if su[0] != x or su[1] != y:
            sp_error.append([test, (x, y), su])
            print('error in Szudzik A pairing function')

        # Pair and unpair using Szudzik B pairing algorithm - map to negative integers
        sxp = szudzik_pair((x, y), True)
        sxu = szudzik_unpair(sxp)
        print('({}, {}) - Szudzik B unpair: {}, Szudzik B pair {}'.format(x, y, sxu, sxp))
        if sxu[0] != x or sxu[1] != y:
            sxp_error.append([test, (x, y), sxu])
            print('error in Szudzik B pairing function')

    if len(cp_error) > 0 or len(sp_error) > 0:
        return cp_error, sp_error

pairing_test(LB, UB, TESTS)