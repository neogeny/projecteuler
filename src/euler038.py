#!/usr/bin/env python
# -*- encoding:utf-8 -*-

"""
Solution to Project Euler Problem 38
http://projecteuler.net/

by Apalala <apalala@gmail.com>
(cc) Attribution-ShareAlike 
http://creativecommons.org/licenses/by-sa/3.0/

Take the number 192 and multiply it by each of 1, 2, and 3:

    192 × 1 = 192
    192 × 2 = 384
    192 × 3 = 576

By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?

"""
from digits import is_pandigital

def product_string(n, k=9):
    d = str(n)
    for i in xrange(2, k):
        if len(d) >= k:
            break
        d += str(i * n)
    return d

def find_pandigital_product(init):
    p, m = init, int(product_string(init))
    for n in xrange(91, 9876):
        d = product_string(n)
        if is_pandigital(d) and int(d) > m:
            p, m = n, int(d)
    return p, m


def test():
    assert '918273645' == product_string(9)
    assert is_pandigital(product_string(9))

if __name__ == '__main__':
    test()
    print find_pandigital_product(init=9)
