from itertools import combinations
from primality import primes_upto, is_prime

def factor(n, m):
    k = 0
    while n >= m:
        d, r = divmod(n, m)
        if r:
            break
        n = d
        k += 1
    return (n, m, k)

def factors(n):
    while n > 1:
        if is_prime(n):
            yield (n, 1)
            break
        for m in primes_upto(n // 2):
            f, _, k = factor(n, m)
            if k:
                yield (m, k)
                n = f
                break

def factor_count(n, upto=None):
    s = 0
    for _, k in factors(n):
        s += k
        if upto and s > upto:
            break
    return s

def mcm(numbers):
    max_factor = {}
    for i in numbers:
        for f, k in factors(i):
            max_factor[f] = max(max_factor.get(f, 0), k)
    result = 1
    for f, k in max_factor.items():
        result *= f ** k
    return result

def multiples(q):
    if not q:
        yield 1
    else:
        n, k = q[0]
        for j in multiples(q[1:]):
            for i in xrange(1, k + 1):
                yield n ** i * j

def divisors(t):
    f = factors(t)
    for s in xrange(0, len(f) + 1):
        for c in combinations(f, s):
            for m in multiples(c):
                yield m


if __name__ == '__main__':
    print list(factors(4))
    print list(factors(7))
    print list(factors(27))
    print list(factors(30))
    print list(factors(100))
    print list(factors(64 * 3 * 5))
