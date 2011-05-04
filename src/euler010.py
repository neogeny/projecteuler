"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""
from primality import nth_prime
from itertools import count

TARGET = 2 * 10 ** 6

def all_primes():
    for n in count(1):
        yield nth_prime(n)

def sum_primes(up_to):
    result = 0
    for p in all_primes():
        if p > up_to:
            break
        result += p
    return result

if __name__ == '__main__':
    print sum_primes(TARGET)
