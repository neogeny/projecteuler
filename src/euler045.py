#!/usr/bin/env python
# -*- encoding:utf-8 -*-

"""
Solution to Project Euler Problem
http://projecteuler.net/

by Apalala <apalala@gmail.com>
(cc) Attribution-ShareAlike 
http://creativecommons.org/licenses/by-sa/3.0/

Triangle, pentagonal, and hexagonal numbers are generated by the following 
formulae:

Triangle           Tn=n(n+1)/2            1, 3, 6, 10, 15, ...
Pentagonal         Pn=n(3n−1)/2           1, 5, 12, 22, 35, ...
Hexagonal          Hn=n(2n−1)             1, 6, 15, 28, 45, ...

It can be verified that T285 = P165 = H143 = 40755.

Find the next triangle number that is also pentagonal and hexagonal.
"""
from math import sqrt
from itertools import count

def is_triangle(n):
    c = (-1 + sqrt(1 + 8 * n)) / 2
    return c == int(c)

def is_pentagonal(n):
    c = (1 + sqrt(1 + 3 * 8 * n)) / 6
    return c == int(c)

def is_exagonal(n):
    c = (1 + sqrt(1 + 8 * n)) / 4
    return c == int(c)

def exagonals():
    for n in count(1):
        yield n * (2 * n - 1)

def next_multiagonal(upfrom):
    for n in exagonals():
        if n > upfrom and is_pentagonal(n) and is_triangle(n):
            return n

def test():
    assert is_triangle(6)
    assert is_triangle(10)
    assert not is_triangle(5)
    assert is_pentagonal(5)
    assert is_pentagonal(12)
    assert is_exagonal(15)
    assert not is_exagonal(10)
    assert is_triangle(40755)
    assert is_pentagonal(40755)
    assert is_exagonal(40755)
    assert 40755 == next_multiagonal(40750)

if __name__ == '__main__':
    test()
    print next_multiagonal(40755)

