#!/usr/bin/env python
# -*- encoding:utf-8 -*-

"""
Solution to Project Euler Problem 4
http://projecteuler.net/

by Apalala <apalala@gmail.com>
(cc) Attribution-ShareAlike 
http://creativecommons.org/licenses/by-sa/3.0/

A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91 x 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

from palindromes import is_palindrome

def largest_palindromic(digits):
    top = int('9' * digits)
    bot = int('9' * (digits - 1))
    best = 0
    for a in xrange(top, bot, -1):
        for b in xrange(top, bot, -1):
            n = a * b
            if n < best:
                break
            if is_palindrome(n):
                best = n
    return best

if __name__ == '__main__':
    print largest_palindromic(3)

