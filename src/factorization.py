from itertools import combinations

def factor(n, m):
    k = 0
    while n >= m:
        d, r = divmod(n, m)
        if r: break
        n = d
        k += 1
    return (n, m, k)

def factors(n):
    if n <= 1:
        return []
    for m in xrange(2, n // 2 + 1):
        f, _, k = factor(n, m)
        if k:
            return [(m, k)] + factors(f)
    return [(n, 1)]

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
    pass
