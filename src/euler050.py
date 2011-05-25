#!/usr/bin/env python
# -*- encoding:utf-8 -*-

"""
Solution to Project Euler Problem 50
http://projecteuler.net/

by Apalala <apalala@gmail.com>
(cc) Attribution-ShareAlike 
http://creativecommons.org/licenses/by-sa/3.0/

The prime 41, can be written as the sum of six consecutive primes:
41 = 2 + 3 + 5 + 7 + 11 + 13

This is the longest sum of consecutive primes that adds to a prime below 
one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a 
prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most 
consecutive primes?
"""
from primality import primes_upto

def consecutive_primes_that_sum_prime(upto):
    prl = list(primes_upto(upto))
    prs = set(prl)
    last = prl[:2]
    for i in xrange(len(prl)):
        pos = i + len(last)
        seq = prl[i:pos]
        for p in prl[pos:]:
            seq.append(p)
            if len(seq) % 2 or len(seq) <= len(last):
                continue
            s = sum(seq)
            if s > prl[-1]:
                break
            if s in prs:
#                print sum(seq), len(seq), prl[i]
                last = seq[:]
    return sum(last), len(last)

def test():
    assert (41, 6) == consecutive_primes_that_sum_prime(10 ** 2)

if __name__ == '__main__':
    test()
    print consecutive_primes_that_sum_prime(10 ** 6)
