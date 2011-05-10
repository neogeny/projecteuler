#!/usr/bin/env python
# -*- encoding:utf-8 -*-

"""
Solutions to Project Euler Problems
http://projecteuler.net/

by Apalala <apalala@gmail.com>
(cc) Attribution-ShareAlike 
http://creativecommons.org/licenses/by-sa/3.0/


"""
from glob import glob
from os import path
from timeit import timeit

if __name__ == '__main__':
    for filename in sorted(glob('euler*.py')):
        name, _ = path.splitext(filename)
        __import__(name)
        try:
            print name,
            t = timeit('test()', 'from ' + name + ' import test', number=1)
            print '{:4.6f}'.format(t)
        except ImportError:
            print 'untested'
