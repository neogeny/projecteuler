# -*- encoding:utf-8 -*-i
"""
Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

    1634 = 14 + 64 + 34 + 44
    8208 = 84 + 24 + 04 + 84
    9474 = 94 + 44 + 74 + 44

As 1 = 14 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
"""

from itertools import count
from digits import digits

def sum_power_of_digits(n, k):
    return sum(x ** k for x in digits(n))

def numbers_that_sum_power_of_digits(k):
    for n in count(2):
        d = list(digits(n))
        if len(d) * (9 ** k) < n:
            break
        if n == sum_power_of_digits(n, k):
            yield n

def sum_of_numbers_that_sum_power_of_digits(k):
    s = 0
    for n in numbers_that_sum_power_of_digits(k):
        s += n
        print n, s
    return s

if __name__ == '__main__':
    print sum_of_numbers_that_sum_power_of_digits(5)
