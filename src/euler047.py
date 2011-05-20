#!/usr/bin/env python
# -*- encoding:utf-8 -*-

"""
Solution to Project Euler Problem 47
http://projecteuler.net/

by Apalala <apalala@gmail.com>
(cc) Attribution-ShareAlike 
http://creativecommons.org/licenses/by-sa/3.0/


The first two consecutive numbers to have two distinct prime factors are:

14 = 2 × 7
15 = 3 × 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2² × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.

Find the first four consecutive integers to have four distinct primes factors. 
What is the first of these numbers?
"""
from itertools import count
from factorization import factors

def n_factors(n):
    return len(list(factors(n)))

def k_consecutive_with_k_factors(k):
    for n in count(5):
        for i in xrange(n, n + k):
            if n_factors(i) != k:
                break
        else:
            return n

def test():
    assert 2 == n_factors(14)
    assert 2 == n_factors(15)
    assert 3 == n_factors(644)
    assert 3 == n_factors(645)
    assert 3 == n_factors(646)
    assert 14 == k_consecutive_with_k_factors(2)
    assert 644 == k_consecutive_with_k_factors(3)

if __name__ == '__main__':
    test()
    n = k_consecutive_with_k_factors(4)
    for i in xrange(n, n + 4):
        print i, list(factors(i))


