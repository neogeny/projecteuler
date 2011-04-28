# 2520 is the smallest number that can be divided by each of the numbers
# from 1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible by all of
# the numbers from 1 to 20?

TARGET = 20

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
    for m in xrange(2, n//2+1):
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

if __name__ == '__main__':
    print mcm(xrange(TARGET))
