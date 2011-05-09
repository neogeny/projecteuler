#!/usr/bin/env python
# -*- encoding:utf-8 -*-

"""
Solution to Project Euler Problem 19
http://projecteuler.net/

by Apalala <apalala@gmail.com>
(cc) Attribution-ShareAlike 
http://creativecommons.org/licenses/by-sa/3.0/

You are given the following information, but you may prefer to do some research for yourself.

    1 Jan 1900 was a Monday.
    Thirty days has September,
    April, June and November.
    All the rest have thirty-one,
    Saving February alone,
    Which has twenty-eight, rain or shine.
    And on leap years, twenty-nine.
    A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""

from datetime import date

MONTH_DAYS = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
MONTH_DAYS_B = MONTH_DAYS
MONTH_DAYS_B[1] = 29

def byhand():
    n = 2 # wednesday in 1901
    sundays = 0
    for y in xrange(1901, 2000 + 1):
        days = MONTH_DAYS if y % 4 else MONTH_DAYS_B
        for d in days:
            n += d
            if n % 7 == 0:
                sundays += 1
    return sundays

def withdates():
    sundays = 0
    for y in xrange(1901, 2000 + 1):
        for m in xrange(1, 12 + 1):
            if date(y, m, 1).isoweekday() == 7:
                sundays += 1
    return sundays

if __name__ == '__main__':
    print byhand()
    print withdates()
