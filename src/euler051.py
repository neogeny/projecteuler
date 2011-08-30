#!/usr/bin/env python
# -*- encoding:utf-8 -*-

"""
Solution to Project Euler Problem 51
http://projecteuler.net/

by Apalala <apalala@gmail.com>
(cc) Attribution-ShareAlike 
http://creativecommons.org/licenses/by-sa/3.0/

By replacing the 1st digit of *3, it turns out that six of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.

By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit number is the first example having seven primes among the ten generated numbers, yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993. Consequently 56003, being the first member of this family, is the smallest prime with this property.

Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits) with the same digit, is part of an eight prime value family.
"""

from collections import OrderedDict
from itertools import compress
from digits import digits
from primality import all_primes

def disimillarity(n, m):
    pairs = zip(digits(n), digits(m))
    return tuple(a != b for a, b in pairs)

def all_same(l):
    return 1 == len(set(l))

def largest_family(limit, largest):
    best_family = []
    current_len = 0
    for p in all_primes():
        pdigs = list(digits(p))
        l2 = len(pdigs)
        if l2 < limit:
            continue
        if l2 > limit:
            break
        if l2 != current_len:
            current_len = l2
            different = (False,)*current_len
            seen = OrderedDict()
        for k in seen.iterkeys():
            s = disimillarity(k, p)
            if s == different:
                continue
            # the replacement number must be the same
            changed = tuple(compress(pdigs, s))
            if not all_same(changed):
                continue
#            print changed, pdigs, s
            family = seen[k].get(s, [k])
            family.append(p)
            if len(family) > len(best_family):
                best_family = family
                print s, family
            seen[k][s] = family
        seen[p] = {different:[p]}
        if len(best_family) >= largest:
            break
    return best_family

def test():
    assert (False,False,True,True,False) == disimillarity(56443,56003)
    assert [13, 23, 43, 53, 73, 83] == largest_family(2, 6)
    print 'search'
    print largest_family(5, 7)

def run():
    pass

if __name__ == '__main__':
    test()
    run()
