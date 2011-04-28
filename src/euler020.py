# encoding=utf-8
"""
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
"""
from operator import mul
def fact(n):
    return reduce(mul,xrange(2,n+1),1)

def sumdigits(n):
    return sum(int(c) for c in str(n))

if __name__ == '__main__':
    print sumdigits(fact(10))
    print sumdigits(fact(100))
