# -*- encondig:utf8 -*-
"""
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

MONTH_DAYS = [31,28,31,30,31,30,31,31,30,31,30,31]
MONTH_DAYS_B = MONTH_DAYS
MONTH_DAYS_B[1] = 29

if __name__ == '__main__':
    n = 2 # wednesday in 1901
    sundays = 0
    for y in xrange(1901,2000+1):
        days = MONTH_DAYS if y%4 else MONTH_DAYS_B
        for d in days:
            n += d
            if n%7 == 0:
                sundays += 1
    print sundays
