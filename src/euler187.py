# -*- encoding:utf-8 -*-i
"""
"""
import pyximport; pyximport.install()
from timeit import timeit
#import libeuler187 as lib

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
