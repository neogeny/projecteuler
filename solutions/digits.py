#!/usr/bin/env python
"""
Solution to Project Euler Problem
http://projecteuler.net/

by Apalala <apalala@gmail.com>
(cc) Attribution-ShareAlike
http://creativecommons.org/licenses/by-sa/3.0/

Dealing with digits.
"""
from memoization import memoize


def seq2str(q):
    return ''.join(q)


def sdigits(n):
    return (c for c in str(n))


def digits(n):
    return (int(c) for c in str(n))


def sorted_digits(n):
    return tuple(sorted(digits(n)))


def last_k_digits(k, n):
    return n % (10 ** k)


@memoize
def digits_upto(k, i=0):
    return seq2str(str(c) for c in xrange(i, min(9, k) + 1))


def digits_downfrom(k, i=0):
    return digits_upto(k, i)[::-1]


def sorted_digits_str(n):
    return seq2str(sorted(str(n)))


def is_semi_pandigital(n):
    s = str(n)
    return '0' not in s and len(s) == len(set(s))


def is_pandigital(n, k=9):
    return sorted_digits(n) == digits_upto(k, 1)


def digit_rotations(n):
    d = str(n)
    for i in xrange(len(d)):
        yield int(d[i:] + d[:i])
