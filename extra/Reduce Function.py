from __future__ import print_function
from fractions import Fraction

from fractions import Fraction
from functools import reduce

def product(fracs):
    t =reduce(lambda x,y:Fraction(x.numerator*y.numerator,x.denominator*y.denominator),fracs)
    return t.numerator, t.denominator



if __name__ == '__main__':
    fracs = []
    for _ in range(input()):
        fracs.append(Fraction(*map(int, raw_input().split())))
    result = product(fracs)
    print(*result)
