#!/usr/bin/env python
# -*- encoding:utf-8 -*-

"""
Solution to Project Euler Problem 5
http://projecteuler.net/

by Apalala <apalala@gmail.com>
(cc) Attribution-ShareAlike
http://creativecommons.org/licenses/by-sa/3.0/

2520 is the smallest number that can be divided by each of the numbers
from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of
the numbers from 1 to 20?
"""
from factorization import mcm

TARGET = 20


def range_mcm(m):
    return mcm(xrange(2, m + 1))


def test():
    assert 2520 == range_mcm(10)


if __name__ == '__main__':
    test()
    print range_mcm(TARGET)
