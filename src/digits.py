#!/usr/bin/env python
# -*- encoding:utf-8 -*-

"""
Solution to Project Euler Problem
http://projecteuler.net/

by Apalala <apalala@gmail.com>
(cc) Attribution-ShareAlike 
http://creativecommons.org/licenses/by-sa/3.0/

Dealing with digits.
"""
from memoization import memoize

def sdigits(n):
    return (c for c in str(n))

def digits(n):
    return (int(c) for c in str(n))

def last_k_digits(k, n):
    return n % (10 ** k)

@memoize
def digits_upto(k, i=0):
    return ''.join(str(c) for c in xrange(i, min(9, k) + 1))

def digits_downfrom(k, i=0):
    return ''.join(reversed(digits_upto(k, 1)))

def sorted_digits(n):
    return ''.join(sorted(str(n)))

def is_semi_pandigital(n):
    s = str(n)
    return '0' not in s and len(s) == len(set(s))

def is_pandigital(n, k=9):
    return sorted_digits(n) == digits_upto(k, 1)

