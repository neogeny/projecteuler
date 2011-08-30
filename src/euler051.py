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
from primality import all_primes, is_prime

def disimillarity(n, m):
    pairs = zip(digits(n), digits(m))
    return tuple(a != b for a, b in pairs)

def digits2num(digits):
    num = 0
    for d in digits:
        num = num*10 + d
    return num 

def exchanged_primes(dig, pattern, start):
    for i in xrange(start, 9+1):
        n = digits2num(i if p else d for p, d in zip(pattern, dig))
        if len(str(n)) == len(pattern) and is_prime(n):
            yield n
        

def largest_family(limit, largest):
    best_family = set()
    current_len = 0
    for p in all_primes():
        pdigs = list(digits(p))
        newlen = len(pdigs)
        if newlen < limit:
            continue
#        if newlen > limit:
#            break
        if newlen != current_len:
            current_len = newlen
            different = (False,)*current_len
            families = OrderedDict()
            known = set()
        for k in families.iterkeys():
            dis = disimillarity(k, p)
            if dis == different or (p,dis) in known:
                continue
            changed = tuple(compress(pdigs, dis))
            kchanged = tuple(compress(digits(k), dis))
            if len(set(changed)) != 1 or len(set(kchanged)) != 1:
                continue
            family = families[k].get(dis, set([k]))
            for c in exchanged_primes(pdigs, dis, list(changed)[0]):
                family.add(c)
                known.add((c,dis))
            if len(family) > len(best_family):
                best_family = family
                print dis, family
            families[k][dis] = family
        families[p] = {different:set((p,))}
        if len(best_family) >= largest:
            break
    return list(sorted(best_family))

def test():
    assert (False,False,True,True,False) == disimillarity(56443,56003)
    print largest_family(2, 6)
    assert [13, 23, 43, 53, 73, 83] == largest_family(2, 6)
    l57 = largest_family(5, 7)
    print l57
    assert [56003, 56113, 56333, 56443, 56663, 56773, 56993] == l57
    print 'tested'

def run():
    print largest_family(6, 8)

if __name__ == '__main__':
    test()
    run()
