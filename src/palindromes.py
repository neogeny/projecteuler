#!/usr/bin/env python
# -*- encoding:utf-8 -*-

"""
Solution to Project Euler Problem
http://projecteuler.net/

by Apalala <apalala@gmail.com>
(cc) Attribution-ShareAlike 
http://creativecommons.org/licenses/by-sa/3.0/


"""
def is_palindrome(n):
    n = str(n)
    m, r = divmod(len(n), 2)
    return n[:m] == n[len(n) + 1:m + r - 1:-1]
