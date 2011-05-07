# -*- encoding:utf-8 -*-i
"""
"""

from factorization import factor_count

def count_numbers_with_factors(k, m):
    c = 0
    for i in xrange(4, m):
        if factor_count(i, upto=k) == k:
            c += 1
        if not (i % 10 ** 4): print '.', i
    return c

if __name__ == '__main__':
    print count_numbers_with_factors(2, 30)
    print count_numbers_with_factors(2, 10 ** 8)
