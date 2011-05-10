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
    total = 0
    for filename in sorted(glob('euler*.py')):
        name, _ = path.splitext(filename)
        try:
            t = timeit('test()', 'from ' + name + ' import test', number=1)
            total += t
#            print name, '{:4.6f}'.format(t)
        except KeyboardInterrupt:
            break
        except ImportError:
            print name, 'untested'
        except AssertionError as ae:
            print name, 'FAILED!'
    print 'total time:', total
