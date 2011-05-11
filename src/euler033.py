#!/usr/bin/env python
# -*- encoding:utf-8 -*-

"""
Solution to Project Euler Problem 33
http://projecteuler.net/

by Apalala <apalala@gmail.com>
(cc) Attribution-ShareAlike 
http://creativecommons.org/licenses/by-sa/3.0/


The fraction 49/98 is a curious fraction, as an inexperienced mathematician in 
attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is 
correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than
one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, 
find the value of the denominator.
"""
import  operator
from functools import reduce
from fractions import Fraction as frac

def unortodox_denom(lower, d):
    ds = str(d)
    if ds[-1] == '0':
        digits = ds[:-1]
    else:
        digits = ds
    for n in xrange(lower, d):
        f = frac(n, d)
        ns = str(n)
        for x in digits:
            if x in ns:
                nr = int(ns.replace(x, '', 1))
                dr = int(ds.replace(x, '', 1))
                if nr and dr and f == frac(nr, dr):
                    return f

def unortodox_fractions(k):
    lower = 10 ** (k - 1)
    upper = int(k * '9')
    for d in xrange(lower, upper + 1):
        f = unortodox_denom(lower, d)
        if f:
            yield f
def test():
    assert frac(4, 8) == unortodox_denom(49, 98)

if __name__ == '__main__':
    test()
    numbers = list(unortodox_fractions(2))
    print reduce(operator.mul, numbers, 1)
