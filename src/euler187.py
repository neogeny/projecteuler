# -*- encoding:utf-8 -*-i
"""
A composite is a number containing at least two prime factors. For example, 15 = 3 × 5; 9 = 3 × 3; 12 = 2 × 2 × 3.

There are ten composites below thirty containing precisely two, not necessarily distinct, prime factors: 4, 6, 9, 10, 14, 15, 21, 22, 25, 26.

How many composite integers, n < 108, have precisely two, not necessarily distinct, prime factors?
"""
#import pyximport; pyximport.install()
from timeit import timeit
import libeuler187 as lib #@UnusedImport

istmt = """import libeuler187 as lib
"""
calls = [
    'print lib.count_numbers_with_factors(2, 30)',
    'print lib.count_numbers_with_factors(2, 10 ** 2)',
    'print lib.count_numbers_with_factors_fast(2, 10 ** 2)',
    'print lib.count_numbers_with_factors_fast(2, 10 ** 8)'
    ]

if __name__ == '__main__':
    for c in calls:
        print timeit(c, setup=istmt, number=2)
