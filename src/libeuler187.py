#!/usr/bin/env python
# -*- encoding:utf-8 -*-

"""
Solution to Project Euler Problem 187
http://projecteuler.net/

by Apalala <apalala@gmail.com>
(cc) Attribution-ShareAlike 
http://creativecommons.org/licenses/by-sa/3.0/

Cast as a library so Cython can be used.
"""
from factorization import factor_count
from primality import primes_upto

def count_numbers_with_factors(k, m):
    c = 0
    for i in xrange(4, m):
        if factor_count(i, upto=k) == k:
            c += 1
            if not (c % 10 ** 6): print '.', c // 10 ** 6
    return c

def count_numbers_with_factors_fast(k, m):
    c = 0
    for a in primes_upto(m // 2 + 1):
        for b in primes_upto(a):
            if a * b > m:
                break
            c += 1
            if not (c % 10 ** 6): print '.', c // 10 ** 6
    return c
from bisect import bisect
from math import sqrt
N = 10 ** 8

# by logopetria
#def count_numbers_with_factors_fastest(k, m):
#    TOTAL = 0
#    for x in range(bisect(PRIMES, sqrt(N))):
#        p = PRIMES[x]
#        TOTAL += bisect(PRIMES, N / p) - x
#    return TOTAL

if __name__ == '__main__':
    pass
