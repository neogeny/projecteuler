#!/usr/bin/env python

"""
Solution to Project Euler Problem 2
http://projecteuler.net/

by Apalala <apalala@gmail.com>
(cc) Attribution-ShareAlike
http://creativecommons.org/licenses/by-sa/3.0/

The sum of the fibonacci numbers less than 4000000
"""
from series import all_fibs


def even_fibs_sum(m):
    result = 0
    for i in all_fibs():
        if i > m:
            break
        if not i % 2:
            result += i
    return result


def test():
    assert 10 == even_fibs_sum(10)


if __name__ == '__main__':
    test()
    print(even_fibs_sum(4 * 10 ** 6))
