#!/usr/bin/env python
# -*- encoding:utf-8 -*-

"""
Solution to Project Euler Problem 35
http://projecteuler.net/

by Apalala <apalala@gmail.com>
(cc) Attribution-ShareAlike 
http://creativecommons.org/licenses/by-sa/3.0/


The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
"""
from primality import is_prime, primes_upto

def rotations(n):
    d = str(n)
    result = []
    for i in xrange(len(d)):
        r = d[i:] + d[:i]
        result.append(r)
    return [int(r) for r in result]

def is_circular_prime(n):
    return all(is_prime(r) for r in rotations(n))

def count_circular_primes(m):
    return sum(is_circular_prime(n) for n in primes_upto(m))

if __name__ == '__main__':
    print rotations(197)
    print is_circular_prime(197)
    print count_circular_primes(10 ** 6)
