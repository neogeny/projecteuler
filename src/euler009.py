#!/usr/bin/env python
# -*- encoding:utf-8 -*-

"""
Solution to Project Euler Problem 9
http://projecteuler.net/

by Apalala <apalala@gmail.com>
(cc) Attribution-ShareAlike 
http://creativecommons.org/licenses/by-sa/3.0/

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

# Solve for b the system of eauations
# a2 + b2 = c2
# a + b + c = 1000

from math import sqrt
from functools import reduce

def pythagorean_triplet_that_sums(s):
    def solve_b(a):
        return s * (s // 2 - a) // (s - a)

    for a in xrange(1, s):
        b = solve_b(a)
        if b < a:
            break

        c = sqrt(a ** 2 + b ** 2)
        if c != int(c):
            continue
        c = int(c)

#        print a, b, c, a + b + c
        if a + b + c == s:
            return (a , b , c)

def prod(q):
    return reduce(lambda x, y:x * y, q, 1)

def test():
    assert 3 * 4 * 5 == prod(pythagorean_triplet_that_sums(3 + 4 + 5))

if __name__ == '__main__':
    test()
    print prod(pythagorean_triplet_that_sums(1000))
