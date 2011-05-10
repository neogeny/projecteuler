#!/usr/bin/env python
# -*- encoding:utf-8 -*-

"""
Solution to Project Euler Problem 50
http://projecteuler.net/

by Apalala <apalala@gmail.com>
(cc) Attribution-ShareAlike 
http://creativecommons.org/licenses/by-sa/3.0/

The prime 41, can be written as the sum of six consecutive primes_upto:
41 = 2 + 3 + 5 + 7 + 11 + 13

This is the longest sum of consecutive primes_upto that adds to a prime below one-hundred.

The longest sum of consecutive primes_upto below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes_upto?
"""
from primality import primes_upto

def consecutive_primes_that_sum_prime():
    prl = list(primes_upto(10 ** 6))
    prs = set(prl)
    last = []
    for i in xrange(len(prl)):
        seq = prl[i:i + len(last)]
        for p in prl[i + len(last):]:
            seq.append(p)
            if len(seq) <= len(last):
                continue
            if sum(seq) > prl[-1]:
                break
            if len(seq) > len(last) and sum(seq) in prs:
                #print sum(seq), seq
                print sum(seq), len(seq), prl[i]
                last = seq[:]
    return sum(last), len(last)

if __name__ == '__main__':
    print consecutive_primes_that_sum_prime()
