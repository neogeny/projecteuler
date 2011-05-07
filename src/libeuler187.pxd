# -*- encoding:utf-8 -*-i
"""
"""
import cython

@cython.locals(c=cython.long,i=cython.long)
cpdef long count_numbers_with_factors(long k, long m)

@cython.locals(c=cython.long,a=cython.long,b=cython.long)
cpdef long count_numbers_with_factors_fast(long k, long m)

if __name__ == '__main__':
    pass
