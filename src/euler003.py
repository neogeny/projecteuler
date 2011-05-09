#!/usr/bin/env python
# -*- encoding:utf-8 -*-

"""
Solution to Project Euler Problem 3
http://projecteuler.net/

by Apalala <apalala@gmail.com>
(cc) Attribution-ShareAlike 
http://creativecommons.org/licenses/by-sa/3.0/

Find the largest prime factor of the given number
"""
TARGET = 600851475143

def largest_prime_factor(n):
    def factor(n, i):
        while n > i:
            a, r = divmod(n, i)
            if r: break
            n = a
        return n

    n = factor(n, 2)
    i = 3
    while i < n:
        n = factor(n, i)
        i += 2
    return n

if __name__ == '__main__':
    print largest_prime_factor(TARGET)
