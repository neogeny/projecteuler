#!/usr/bin/env python

"""
Solution to Project Euler Problem 3
http://projecteuler.net/

by Apalala <apalala@gmail.com>
(cc) Attribution-ShareAlike
http://creativecommons.org/licenses/by-sa/3.0/

Find the largest prime factor of the given number
"""
from factorization import factors


TARGET = 600851475143


def largest_prime_factor(n):
    return list(factors(n))[-1]


def test():
    assert 29 == largest_prime_factor(13195)


if __name__ == '__main__':
    test()
    print(largest_prime_factor(TARGET))
