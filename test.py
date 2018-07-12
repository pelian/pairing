from pairing import cantor_pair, cantor_unpair, szudzik_pair, szudzik_unpair
import numpy as np

# Test variables
LB = -100000 # Random integer lower bound
UB = 100000 # Random integer upper bound
TESTS = 10000 # Number of test runs

def pairing_test(lower: int, upper: int, tests: int):
    error = []
    for test in range(tests):
        x = np.random.randint(lower, upper)
        y = np.random.randint(lower, upper)
        print('\n')
        # Pair and unpair using Cantor pairing algorithm
        cp = cantor_pair((x, y))
        cu = cantor_unpair(cp)
        print('({}, {}) - Cantor unpair: {}, Cantor pair {}'.format(x, y, cu, cp))
        if cu[0] != x or cu[1] != y:
            error.append(['Cantor', test, (x, y), cu])            

        # Pair and unpair using Szudzik pairing algorithm
        sap = szudzik_pair((x, y))
        sau = szudzik_unpair(sap)
        print('({}, {}) - Szudzik A unpair: {}, Szudzik A pair {}'.format(x, y, sau, sap))
        if sau[0] != x or sau[1] != y:
            error.append(['Szudzik A', test, (x, y), sau])

        # Pair and unpair using Szudzik B pairing algorithm - map to negative integers
        sbp = szudzik_pair((x, y), True)
        sbu = szudzik_unpair(sbp)
        print('({}, {}) - Szudzik B unpair: {}, Szudzik B pair {}'.format(x, y, sbu, sbp))
        if sbu[0] != x or sbu[1] != y:
            error.append(['Szudzik B', test, (x, y), sbu])

    if len(error) > 0:
        print('error was found in a pairing function')
        return error

pairing_test(LB, UB, TESTS)