from operator import mul
from memoization import memoize
from functools import reduce

@memoize
def factorial(n):
    return reduce(mul, xrange(2, n + 1), 1)

def all_fibs():
    a = b = 1
    while True:
        yield a
        a, b = b, a + b

def fibs(n):
    for i, f in enumerate(all_fibs()):
        if i >= n:
            break
        yield f


def sum_of_squares(n):
    return (n * (n + 1) * (2 * n + 1)) // 6

def square_of_sum(n):
    return (n ** 2 * (n + 1) ** 2) // 4

if __name__ == '__main__':
    print list(fibs(4))
