#!/usr/bin/env python
# -*- encoding:utf-8 -*-

"""
Solution to Project Euler Problem 1
http://projecteuler.net/

by Apalala <apalala@gmail.com>
(cc) Attribution-ShareAlike 
http://creativecommons.org/licenses/by-sa/3.0/

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

def sum_of_3_or_5_div(m):
    total = 0
    for i in xrange(m):
        if not (i % 3 and i % 5):
            total += i
    return total

def test():
    assert 23 == sum_of_3_or_5_div(10)

if __name__ == '__main__':
    test()
    print sum_of_3_or_5_div(1000)
