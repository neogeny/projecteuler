# -*- encoding:utf-8 -*-
"""
The prime 41, can be written as the sum of six consecutive primes:
41 = 2 + 3 + 5 + 7 + 11 + 13

This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?
"""
from itertools import count
from primality import nth_prime

def primes(m):
    for i in count(1):
        p = nth_prime(i)
        if p < m + 1:
            yield p
        else:
            break

def first_prime_that_sums():
    prl = list(primes(10 ** 6))
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
    print first_prime_that_sums()
