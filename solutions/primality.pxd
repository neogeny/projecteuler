#!/usr/bin/env python
# -*- encoding:utf-8 -*-

"""
Solution to Project Euler Problems
http://projecteuler.net/

by Apalala <apalala@gmail.com>
(cc) Attribution-ShareAlike 
http://creativecommons.org/licenses/by-sa/3.0/

Cython definitions for the module.
"""
import cython

@cython.locals(
k = cython.long,
p = cython.long,
limit  = cython.long
)
cpdef long nth_prime(long n)

@cython.locals(
i = cython.long,
k = cython.long,
p = cython.long
)
cpdef long is_prime(long n)
