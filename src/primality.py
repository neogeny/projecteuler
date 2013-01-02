#!/usr/bin/env python
# -*- encoding:utf-8 -*-

"""
Solution to Project Euler Problem
http://projecteuler.net/

by Apalala <apalala@gmail.com>
(cc) Attribution-ShareAlike 
http://creativecommons.org/licenses/by-sa/3.0/

Prime numbers.
"""
from math import sqrt
from bisect import bisect_left as bisect
from itertools import count

__primes = [
           2, 3, 5, 7,
           11, 13, 17, 19,
           23, 29,
           31, 37,
           41, 43, 47,
           53, 59,
           61, 67,
           71, 73, 79,
           83, 89,
           97
           ]

def nth_prime(n):
    global __primes
    if not __primes:
        __primes = [2]

    if n <= len(__primes):
        return __primes[n - 1]

    k = __primes[-1]
    limit = 1 + bisect(__primes, int(sqrt(k)))
    while len(__primes) < n:
        k += 2
        while __primes[limit] ** 2 < k:
            limit += 1
        if all(k % p for p in __primes[1:limit]):
            __primes.append(k)
    return __primes[-1]

def known_prime(n):
    if n <= __primes[-1]:
        i = bisect(__primes, n)
        return __primes[i] == n
    return False

def is_prime(n):
    n = abs(n)
    if n < 2:
        return False
    elif n <= __primes[-1]:
        return known_prime(n)
    else:
        return all(n % p for p in sieve_upto(sqrt(n)))

def all_primes():
    for n in count(1):
        yield nth_prime(n)

def primes_upto(m):
    for p in all_primes():
        if p <= m:
            yield p
        else:
            break

def sieve_upto(m):
    sieve = (m + 1) * [True]
    p = 1
    for p in __primes:
        if p <= m:
            yield p
            for j in xrange(p*p, m, p):
                sieve[j] = False
        else:
            break
    for p in xrange(p+2, m, 2):
        if sieve[p]:
            if p > __primes[-1]:
                __primes.append(p)
            yield p
            for j in xrange(p*p, m, p):
                sieve[j] = False

def test(pr):
    N = 10 ** 6
    s = 0
    for p in pr(N):
        s += 1
        assert p <= N
        assert is_prime(p)
    print s, p

if __name__ == '__main__':
    from timeit import timeit
    print timeit('test(primes_upto)', 
                    'from primality import test, primes_upto', 
                    number=4)
    print timeit('test(sieve_upto)', 
                    'from primality import test, sieve_upto', 
                    number=4)
