# -*- encoding:utf-8 -*-i
"""
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
"""
from itertools import count
from digits import digits
from series import factorial

def sum_fact_digits(n):
    return sum(factorial(d) for d in digits(n))

def list_sum_fact_digits():
    f9 = factorial(9)
    for n in count(3):
        k = len(str(n))
        if k * f9 < 9 * 10 ** k:
            break
        if n == sum_fact_digits(n):
            print n
            yield n

if __name__ == '__main__':
    print sum_fact_digits(145)
    print sum(list_sum_fact_digits())
