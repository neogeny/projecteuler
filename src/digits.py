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

def sdigits(n):
    return (c for c in str(n))

def digits(n):
    return (int(c) for c in str(n))

def last_k_digits(k, n):
    return n % (10 ** k)
