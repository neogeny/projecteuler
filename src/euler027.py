#!/usr/bin/env python
# -*- encoding:utf-8 -*-

"""
Solution to Project Euler Problem 27
http://projecteuler.net/

by Apalala <apalala@gmail.com>
(cc) Attribution-ShareAlike 
http://creativecommons.org/licenses/by-sa/3.0/

Euler published the remarkable quadratic formula:

n² + n + 41

It turns out that the formula will produce 40 primes for the consecutive values 
n = 0 to 39. However, when n = 40, 402 + 40 + 41 = 40(40 + 1) + 41 is divisible 
by 41, and certainly when n = 41, 41² + 41 + 41 is clearly divisible by 41.

Using computers, the incredible formula  n² − 79n + 1601 was discovered, which 
produces 80 primes for the consecutive values n = 0 to 79. The product of the 
coefficients, −79 and 1601, is −126479.

Considering quadratics of the form:

    n² + an + b, where |a| < 1000 and |b| < 1000

    where |n| is the modulus/absolute value of n
    e.g. |11| = 11 and |−4| = 4

Find the product of the coefficients, a and b, for the quadratic expression 
that produces the maximum number of primes for consecutive values of n, 
starting with n = 0.
"""

from itertools import count
from primality import is_prime, primes_upto

def even(x):
    return not x % 2

def odd(x):
    return x % 2

def quadratic(n, a, b):
    return n ** 2 + a * n + b

def ab_generated_primes_len(a, b):
    for n in count(1):
        q = quadratic(n, a, b)
        if even(q) or not is_prime(q):
            return n - 2

def ab_prime_generators(i, j):
    for b in primes_upto(j):
        for a in xrange(i, j):
            if odd(a):
                yield (1 + ab_generated_primes_len(a, b), a, b)
            else:
                yield (1, a, b)  # True == even(1**2 + 1 * a + b)

def ab_prime_generator_with_max_len(i, j):
    return max(ab_prime_generators(i, j))

def test():
    assert (39, 1, 41) == ab_prime_generator_with_max_len(0, 43)

if __name__ == '__main__':
    test()
    longest = ab_prime_generator_with_max_len(-1000 + 1, 1000)
    print longest
    print longest[1] * longest[2]
