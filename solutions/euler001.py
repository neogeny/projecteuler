#!/usr/bin/env python
"""
Solution to Project Euler Problem 1
http://projecteuler.net/

by Apalala <apalala@gmail.com>
(cc) Attribution-ShareAlike
http://creativecommons.org/licenses/by-sa/3.0/

If we list all the natural numbers below 10 that are multiples i
of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""


def sum_of_3_or_5_div(m):
    return sum(i for i in range(m) if not (i % 3 and i % 5))


def test():
    assert 23 == sum_of_3_or_5_div(10)


def run():
    print(sum_of_3_or_5_div(1000))


if __name__ == '__main__':
    test()
    run()
