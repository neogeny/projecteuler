#!/usr/bin/env python
# -*- encoding:utf-8 -*-

"""
Solution to Project Euler Problems
http://projecteuler.net/

by Apalala <apalala@gmail.com>
(cc) Attribution-ShareAlike 
http://creativecommons.org/licenses/by-sa/3.0/


"""
from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

setup(
    cmdclass={'build_ext': build_ext},
    ext_modules=[
        Extension("libeuler187", ["libeuler187.pyx"]),
        Extension("primality", ["primality.py"])
    ]
)
