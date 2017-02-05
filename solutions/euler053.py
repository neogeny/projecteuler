#!/usr/bin/env python
# -*- encoding:utf-8 -*-

"""
Solution to Project Euler Problem 53
http://projecteuler.net/

by Apalala <apalala@gmail.com>
(cc) Attribution-ShareAlike 
http://creativecommons.org/licenses/by-sa/3.0/

There are exactly ten ways of selecting three from five, 12345:

123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

In combinatorics, we use the notation, 5C3 = 10.

In general,

nCr =	
n!
r!(nr)!
,where r  n, n! = n(n1)...321, and 0! = 1.
It is not until n = 23, that a value exceeds one-million: 23C10 = 1144066.

How many, not necessarily distinct, values of  nCr, for 1  n  100, are greater than one-million?
"""
from math import factorial as fact

# brute force using Python's long integers
def count_combinations_greater(nlimit, target_max):
    count = 0
    for n in xrange(1, nlimit+1):
        for r in xrange(1, n):
            c = fact(n)//(fact(r)*fact(n-r))
            if c >= target_max:
                count += 1
    return count

def test():
    assert 4075 == count_combinations_greater(100, 10**6)

def run():
    print count_combinations_greater(100, 10**6)

if __name__ == '__main__':
    test()
    run()
