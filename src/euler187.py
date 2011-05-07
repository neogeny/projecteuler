# -*- encoding:utf-8 -*-i
"""
"""
import pyximport; pyximport.install()
from timeit import timeit
from libeuler187 import *

istmt="""from libeuler187 import *
"""
calls = [
    'print count_numbers_with_factors(2, 30)',
    'print count_numbers_with_factors(2, 10 ** 2)',
    'print count_numbers_with_factors_fast(2, 10 ** 2)',
    'print count_numbers_with_factors_fast(2, 10 ** 8)'
    ]

if __name__ == '__main__':
    for c in calls:
        print timeit(c, setup=istmt, number=2)
