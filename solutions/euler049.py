#!/usr/bin/env python
# -*- encoding:utf-8 -*-

"""
Solution to Project Euler Problem 49
http://projecteuler.net/

by Apalala <apalala@gmail.com>
(cc) Attribution-ShareAlike 
http://creativecommons.org/licenses/by-sa/3.0/

The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases 
by 3330, is unusual in two ways: (i) each of the three terms are prime, and, 
(ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, 
exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this 
sequence?
"""
from itertools import permutations
from primality import primes_upto, is_prime

def intperms(n):
    return set(int(''.join(x)) for x in permutations(str(n)))

def find_prime_series(n, q):
    r = list(sorted(q))
    q = set(q)
    for i in xrange(len(r) - (n - 1)):
        first = r[i]
        for second in r[i + 1:len(r) - (n - 2)]:
            diff = second - first
            result = [first, second]
            k = n - 2
            t = second + diff
            while k > 0 and t in r:
                result.append(t)
                k -= 1
                t += diff
            if not k:
                return result

def prime_perms(p):
    return (x for x in intperms(p) if x >= p and is_prime(x))

def all_prime_perm_series(k, n):
    left = int('1' * k)
    right = int('9' * k)
    pri = set(x for x in primes_upto(right) if x >= left)
    for p in sorted(pri):
        e = find_prime_series(n, prime_perms(p))
        if e:
            yield e

def test():
    q = [4871, 7841, 8741, 1847, 7481, 1487, 4817, 8147]
    assert q == list(prime_perms(1487))
    assert [1487, 4817, 8147] == find_prime_series(3, q)

if __name__ == '__main__':
    test()
    for p in all_prime_perm_series(4, 3):
        print p, ''.join(str(c) for c in p)
