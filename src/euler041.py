#!/usr/bin/env python
# -*- encoding:utf-8 -*-

"""
Solution to Project Euler Problem
http://projecteuler.net/

by Apalala <apalala@gmail.com>
(cc) Attribution-ShareAlike 
http://creativecommons.org/licenses/by-sa/3.0/


We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
"""
from digits import is_pandigital, digits_upto, seq2str
from itertools import permutations
from primality import is_prime

def pandigital_primes(digits=7):
    # 9 and 8-pandigital numbers are divisible by 3
    digits = min(digits, 7)
    for k in xrange(digits, 3, -1):
        for p in permutations(reversed(digits_upto(k, 1))):
            ip = int(seq2str(p))
            if is_prime(ip):
                yield ip

def test():
    assert not is_prime(123)
    assert not is_prime(132)
    assert not is_prime(213)
    assert not is_prime(231)
    assert not is_prime(312)
    assert not is_prime(321)
    assert is_prime(2143)
    assert is_pandigital(2143, 4)
    assert 2143 in set(pandigital_primes(digits=4))

if __name__ == '__main__':
    test()
    print 'ok'
    for n in pandigital_primes():
        print n
        break
