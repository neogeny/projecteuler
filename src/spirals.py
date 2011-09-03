#!/usr/bin/env python
# -*- encoding:utf-8 -*-

"""
Solutions to Project Euler Problems
http://projecteuler.net/

by Apalala <apalala@gmail.com>
(cc) Attribution-ShareAlike 
http://creativecommons.org/licenses/by-sa/3.0/

Spirals.
"""
from itertools import count

def spiral_diagonal_numbers():
    yield 1,1,0
    number = 1
    for side in count(1):
        diff = 2 * side
        for diag_no in xrange(4):
            number += diff
            yield number, side+1, diag_no

def test():
    pass

def run():
    pass

if __name__ == '__main__':
    test()
    run()
