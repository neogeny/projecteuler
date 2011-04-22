#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, 
#we can see that the 6th prime is 13.
#
#What is the 10001st prime number?
from math import sqrt
from bisect import bisect

__primes = [
           2, 3, 5, 7,
           11, 13, 17, 19,
           23, 29,
           31, 37,
           41, 43, 47,
           53, 59,
           61, 67,
           71, 73, 79,
           83, 89,
           97
           ]

def nth_prime(n):
    global __primes
    if not __primes:
        __primes = [2]

    if n <= len(__primes):
        return __primes[n - 1]

    n -= len(__primes)
    k = __primes[-1] + 2
    while n > 0:
        limit = bisect(__primes, sqrt(k))
        if all(k % p for p in __primes[1:limit]):
            __primes.append(k)
            n -= 1
        k += 2

    return __primes[-1]

if __name__ == '__main__':
    print nth_prime(10001)
    print nth_prime(10001)
