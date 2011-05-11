#!/usr/bin/env python
# -*- encoding:utf-8 -*-

"""
Solution to Project Euler Problem 32
http://projecteuler.net/

by Apalala <apalala@gmail.com>
(cc) Attribution-ShareAlike 
http://creativecommons.org/licenses/by-sa/3.0/

We shall say that an n-digit number is pandigital if it makes use of all the 
digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 
through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing 
multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity
can be written as a 1 through 9 pandigital.
HINT: Some products can be obtained in more than one way so be sure to only
include it once in your sum.
"""
from memoization import memoize

@memoize
def digits_upto(k, i=0):
    return ''.join(str(c) for c in xrange(i, min(9, k) + 1))

def sorted_digits(n):
    return ''.join(sorted(str(n)))

def is_semi_pandigital(n):
    s = str(n)
    return '0' not in s and len(s) == len(set(s))

def is_pandigital(n, k=9):
    return sorted_digits(n) == digits_upto(k, 1)

def is_pandigital_product(a, b, n, k=9):
    return is_pandigital(str(a) + str(b) + str(n), k)


def find_pandigital_products(k):
    upper = int(''.join(reversed(digits_upto(k, 1)))[:-k // 2])
    for a in xrange(2, upper):
        if not is_semi_pandigital(a): continue
        for b in xrange(a, upper):
            n = a * b
            if n > upper:
                break
            if is_pandigital_product(a, b, n):
                yield (a, b, n)


def test():
    assert '123456789' == digits_upto(9, 1)
    assert '012345' == digits_upto(5)
    assert is_pandigital(978564231)
    assert is_pandigital(13452, 5)
    assert is_semi_pandigital(543)
    assert not is_semi_pandigital(3543)

if __name__ == '__main__':
    test()
    print sum(set(n for _a, _b, n in find_pandigital_products(9)))
