from typing import Tuple, Optional
from math import floor, sqrt

def encode(z: int) -> int:
    '''
    Transformation for negative values when encoding
    '''
    if z >= 0:
        return z * 2 + 1
    else:
        return -z * 2

def decode(n: int) -> int:
    '''
    Transformation for negative values when decoding
    '''
    if n <= 0:
        raise ValueError("must be a natural number")
    if n % 2 == 0:
        return -n // 2 # PEP238 operator to do integer division
    else:
        return int(floor(n / 2))


def cantor_pair(t: Tuple[int, int]) -> int:
    '''
    George Cantor (1891) pairing algorithm for tuple of integers (x, y)
    Modified to handle negative integers
    Arguments: 
    t: tuple(x, y) where x, y is an integer in set ℤ
    '''
    # encode adds support for negative integers
    a = encode(t[0]) - 1
    b = encode(t[1]) - 1

    return floor((a + b) * (a + b + 1) / 2) + b + 1


def cantor_unpair(z: int) -> Tuple[int, int]:
    '''
    George Cantor (1891) unpairing algorithm for integer in set ℤ*
    Arguments:
    z: int where z is an integer in set ℤ*
    '''

    if z <= 0:
        raise ValueError("must be a natural number")

    z = z - 1
    w = floor((sqrt(8 * z + 1) - 1) / 2)
    t = (w * w + w) / 2

    y = int(z - t)
    x = int(w - y)

    return decode(x + 1), decode(y + 1)


def szudzik_pair(t: Tuple[int, int], map: Optional[bool] = False) -> int:
    '''
    Matthew Szudzik (2006) pairing algorithm for integers (x, y)
    Modified to handle negative integers
    Arguments: 
    t: tuple(x, y) where x, y is an integer in set ℤ
    map: boolean where [true] will map to integer in set ℤ : [false] will map to integers in set ℤ*

    '''
    x = t[0]
    y = t[1]
    a = encode(t[0]) - 1
    b = encode(t[1]) - 1
    c = (b * b) + a if a < b else (a * a) + a + b

    return -c - 1 if map and ((x >= 0 and y < 0) or (x < 0 and y >= 0)) else c  

def szudzik_unpair(z: int) -> Tuple[int, int]:
    '''
    Matthew Szudzik (2006) unpairing algorithm for integer in set ℤ
    Arguments:
    z: int where z is an integer in set ℤ
    '''
    if z < 0: # handle szudzik pair mapped to negative numbers
        z = -(z + 1)
    s = floor(sqrt(z))
    q = s * s
    (x, y) = (z - q, s) if z - q < s else (s, z - q - s)

    return decode(x + 1), decode(y + 1)

# Todo n-tuples pairing function
# Reference: An Elegant Pairing Function by Matthew Szudzik @ Wolfram Research, Inc.