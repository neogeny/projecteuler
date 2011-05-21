#!/usr/bin/env python
# -*- encoding:utf-8 -*-

"""
Solution to Project Euler Problem
http://projecteuler.net/

by Apalala <apalala@gmail.com>
(cc) Attribution-ShareAlike 
http://creativecommons.org/licenses/by-sa/3.0/


"""
from math import sqrt
from collections import defaultdict

def perimeter_combinations_for(limit):
    perims = defaultdict(set)
    for a in xrange(1, limit // 2):
        for b in xrange(1, limit-a-1):
            c = sqrt(a**2 + b**2)
            if c == int(c) and a+b+c < limit:
                c = int(c)
                tr = tuple(sorted((a,b,c)))
                perims[a+b+c].add(tr) 
    return perims

def test():
    assert 3 == len(perimeter_combinations_for(125)[120])

def run():
    print max((len(s), p) for p,s in perimeter_combinations_for(1001).items())

if __name__ == '__main__':
    test()
    run()

