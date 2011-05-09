#!/usr/bin/env python
# -*- encoding:utf-8 -*-

"""
Solution to Project Euler Problem 21
http://projecteuler.net/

by Apalala <apalala@gmail.com>
(cc) Attribution-ShareAlike 
http://creativecommons.org/licenses/by-sa/3.0/


Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; 
therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""

from factorization import divisors

TARGET = 10000


__seen = {}
def d(n):
    if n not in __seen:
        __seen[n] = sum(divisors(n)) - n
    return __seen[n]

def amicable(n):
    s = d(n)
    return s != n and n == d(s)

def amicables(n):
    for i in xrange(2, n):
        if amicable(i):
            yield i

if __name__ == '__main__':
    print list(divisors(220))
    print list(divisors(284))
    print d(220)
    print d(284)
    print sum(amicables(TARGET))
