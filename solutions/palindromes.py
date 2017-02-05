#!/usr/bin/env python

"""
Solution to Project Euler Problems
http://projecteuler.net/

by Apalala <apalala@gmail.com>
(cc) Attribution-ShareAlike
http://creativecommons.org/licenses/by-sa/3.0/

Palindromes.
"""


def is_palindrome(n):
    ns = str(n)
    return ns == ns[::-1]
