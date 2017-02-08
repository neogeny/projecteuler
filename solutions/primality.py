#!/usr/bin/env python
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

    i = __primes[-1]
    limit = 1 + bisect(__primes, int(sqrt(i)))
    while len(__primes) < n:
        i += 2
        while __primes[limit] ** 2 <= i:
            limit += 1
        if all(i % p for p in __primes[1:limit]):
            __primes.append(i)
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
    elif known_prime(n):
        return True
    else:
        return all(n % p for p in primes_upto(n))


def all_primes():
    for n in count(1):
        yield nth_prime(n)


def primes_upto(m):
    for p in all_primes():
        if p < m:
            yield p
        else:
            break


def sieve_upto(n):
    if n < 2:
        return

    m = (n - 1) // 2
    b = [True] * m

    def discard_multiples(p):
        i = p // 2
        start = 2 * i * i + 6 * i + 3
        for j in xrange(start, m, 2 * i + 3):
            b[j] = False

    yield 2
    for p in __primes[1:]:
        if p > n:
            return
        yield p
        discard_multiples(p)

    p = __primes[-1] + 2
    while p * p < n:
        i = p // 2
        if b[i]:
            __primes.append(p)
            yield p
            discard_multiples(p)
        p += 2
    i = p // 2
    for i in xrange(i, m):
        if b[i]:
            __primes.append(p)
            yield p
        p += 2

__b = set()


def set_sieve_upto(n):
    if n < 2:
        return

    def discard_multiples(p):
        for j in xrange(p * p, n, p):
            if j in __b:
                break
            __b.add(j)

    yield 2
    for p in __primes[1:]:
        if p > n:
            return
        yield p
        discard_multiples(p)

    p = __primes[-1] + 2
    while p * p < n:
        if p not in __b:
            __primes.append(p)
            yield p
            discard_multiples(p)
        p += 2
    for p in xrange(p, n, 2):
        if p not in __b:
            __primes.append(p)
            yield p


def test(pr):
    N = 10 ** 7
    s = 0
    for p in pr(N):
        s += 1
        assert p <= N, '%d %d' % (p, N)
        assert is_prime(p)
    s = 0
    for p in pr(N):
        s += 1
        assert p <= N, '%d %d' % (p, N)
        assert is_prime(p)


if __name__ == '__main__':
    from timeit import timeit
    print('set_sieve_output')
    print(
        timeit(
            'test(set_sieve_upto)',
            'from primality import test, set_sieve_upto',
            number=4
        )
    )
    print('sieve_output')
    print(
        timeit(
            'test(sieve_upto)',
            'from primality import test, sieve_upto',
            number=4
        )
    )
