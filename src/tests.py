#!/usr/bin/env python
# -*- encoding:utf-8 -*-

"""
Solutions to Project Euler Problems
http://projecteuler.net/

by Apalala <apalala@gmail.com>
(cc) Attribution-ShareAlike 
http://creativecommons.org/licenses/by-sa/3.0/


"""
import sys
from glob import glob
from os import path
from timeit import timeit

def test_assertions_on():
    try:
        assert False
        print 'Please turn on assertions!'
        sys.exit()
    except AssertionError:
        pass


if __name__ == '__main__':
    test_assertions_on()
    total = 0
    count = 0
    failed = 0
    for filename in sorted(glob('euler*.py')):
        name, _ = path.splitext(filename)
        try:
            t = timeit('test()', 'from ' + name + ' import test', number=1)
            total += t
            count += 1
#            print name, '{:4.6f}'.format(t)
        except KeyboardInterrupt:
            break
        except ImportError:
            print name, 'untested'
        except AssertionError as ae:
            failed += 1
            print name, 'FAILED!'
    print 'total time for', count, 'problems,', failed, 'failed, is:', total
