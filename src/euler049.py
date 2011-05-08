# -*- encoding:utf-8 -*-i
"""
The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?
"""
from itertools import permutations, combinations
from primality import primes_upto, is_prime

def intperms(n):
    return set(int(''.join(x)) for x in permutations(str(n)))

def diffs(q):
    if q:
        q = sorted(q)
        s = q[0]
        for n in q[1:]:
            yield (n - s)
            s = n

def find_series1(q, n):
    q = list(sorted(q))
    if len(q) < 2: return None
    for c in combinations(q, n):
        d = list(diffs(c))
        if all(d[i] == d[0] for i in xrange(1, len(d))):
            return c

def find_series(q, n):
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



def prime_palindromes(p):
    return (x for x in intperms(p) if x >= p and is_prime(x))

def prime_perms(k, n):
    left = int('1' * k)
    right = int('9' * k)
    pri = set(x for x in primes_upto(right) if x >= left)
    for p in sorted(pri):
        perms = (x for x in intperms(p) if x >= p and x in pri)
        e = find_series(perms, n)
        if e:
            yield e

if __name__ == '__main__':
    for p in prime_perms(4, 3):
        print p, ''.join(str(c) for c in p)
#    for p in prime_perms(6,4):
#        print p, ''.join(str(c) for c in p)