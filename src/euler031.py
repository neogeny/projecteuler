#!/usr/bin/env python
# -*- encoding:utf-8 -*-

"""
Solution to Project Euler Problem 31
http://projecteuler.net/

by Apalala <apalala@gmail.com>
(cc) Attribution-ShareAlike 
http://creativecommons.org/licenses/by-sa/3.0/


In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:

    1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).

It is possible to make £2 in the following way:

    1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p

How many different ways can £2 be made using any number of coins?
"""

def add_change(amount, denominations):
    if not amount:
        yield []
    elif denominations:
        denominations = list(sorted(denominations))
        d = denominations[-1]
        denominations = denominations[:-1]
        for i in xrange(1 + amount // d):
            for w in add_change(amount - i * d, denominations):
                if w is not None:
                    if i:
                        yield [(i, d)] + w
                    else:
                        yield w


if __name__ == '__main__':
    ways = 0
    for w in add_change(200, [1, 2, 5, 10, 20, 50, 100, 200]):
        assert 200 == sum(n * d for n, d in w)
        print w
        ways += 1
    print ways
