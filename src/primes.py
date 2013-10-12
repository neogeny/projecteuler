#!/usr/bin/env python
# -*- encoding:utf-8 -*-

"""
Solution to Project Euler Problem
http://projecteuler.net/

by Apalala <apalala@gmail.com>
(cc) Attribution-ShareAlike :
http://creativecommons.org/licenses/by-sa/3.0/

Prime numbers.
"""
import sys
from math import sqrt
from bisect import bisect_left as bisect
from itertools import count

__primes = [
           2, 3, 5, 7,
           11, 13, 17, 19,
           23, 29,
           31, 37,
           41, 43, 47,
           53, 59,
           61, 67,
           71, 73, 79,
           83, 89,
           97
           ]

__excludes = set([4, 2, 8])

def discard_multiples(p, m):
    start = max([max(__excludes), p * p])
    for j in xrange(start, m, p):
        if j in __excludes:
            break
        __excludes.add(j)

def init(m=None):
    if m == None:
        m = __primes[-1]
    for p in __primes[1:]:
        discard_multiples(p, m)
init()

def known_prime(n):
    if n <= __primes[-1]:
        i = bisect(__primes, n)
        return __primes[i] == n
    return False

def is_prime(n):
    n = abs(n)
    if n < 2:
        return False
    elif known_prime(n):
        return True
    else:
        return all(n % p for p in primes_upto(int(sqrt(n))))

def primes_upto(m):
    for p in __primes:
        if p < m:
            yield p
            discard_multiples(p, m)
    for i in xrange(p + 2, m, 2):
        if i not in __excludes:
            yield i
            __primes.append(i)
            discard_multiples(i, m)


if __name__ == '__main__':
    list(primes_upto(10 ** 7))
    print len(__primes)
    print len(__excludes)
    print len(__primes), __primes[-1]
#    print __excludes
