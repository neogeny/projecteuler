#!/usr/bin/env python
# -*- encoding:utf-8 -*-

"""
Solution to Project Euler Problems
http://projecteuler.net/

by Apalala <apalala@gmail.com>
(cc) Attribution-ShareAlike 
http://creativecommons.org/licenses/by-sa/3.0/

Mthematical series.
"""
from operator import mul
import math
from math import sqrt
from itertools import count
from memoization import memoize

@memoize
def factorial(n):
    return math.factorial(n)

def all_fibs():
    a = b = 1
    while True:
        yield a
        a, b = b, a + b

def fibs(n):
    for i, f in enumerate(all_fibs()):
        if i >= n:
            break
        yield f

def sum_of_squares(n):
    return (n * (n + 1) * (2 * n + 1)) // 6

def square_of_sum(n):
    return (n ** 2 * (n + 1) ** 2) // 4

def is_triangle(n):
    c = (-1 + sqrt(1 + 8 * n)) / 2
    return c == int(c)

def triangles(upto=None):
    for n in count(1):
        if upto and n > upto:
            break
        yield n * (n + 1) / 2

def is_pentagonal(n):
    c = (1 + sqrt(1 + 3 * 8 * n)) / 6
    return c == int(c)

def pentagonals(upto=None):
    for n in count(1):
        if upto and n > upto:
            break
        yield n * (3 * n - 1) / 2

def is_exagonal(n):
    c = (1 + sqrt(1 + 8 * n)) / 4
    return c == int(c)

def exagonals(upto=None):
    for n in count(1):
        if upto and n > upto:
            break
        yield n * (2 * n - 1)

def test():
    assert is_triangle(6)
    assert is_triangle(10)
    assert not is_triangle(5)
    assert is_pentagonal(5)
    assert is_pentagonal(12)
    assert is_exagonal(15)
    assert not is_exagonal(10)

if __name__ == '__main__':
    test()
