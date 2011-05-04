# -*- coding: utf-8 -*-
"""
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; 
therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""

from math import sqrt
from itertools import combinations
from factorization import factors

TARGET = 10000

def multiples(q):
    if not q:
        yield 1
    else:
        n, k = q[0]
        for j in multiples(q[1:]):
            for i in xrange(1, k + 1):
                yield n ** i * j

def divisors(t):
    f = factors(t)
    for s in xrange(1, len(f) + 1):
        for c in combinations(f, s):
            for m in multiples(c):
                yield m

__seen = {}
def d(n):
    if n not in __seen:
        __seen[n] = 1 + sum(divisors(n)) - n
    return __seen[n]

def amicable(n):
    s = d(n)
    return s != n and n == d(s)

def amicables(n):
    for i in xrange(2, n):
        if amicable(i):
            print i
            yield i

if __name__ == '__main__':
    print list(divisors(220))
    print list(divisors(284))
    print d(220)
    print d(284)
    print sum(amicables(TARGET))
