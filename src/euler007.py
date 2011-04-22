#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, 
#we can see that the 6th prime is 13.
#
#What is the 10001st prime number?
from math import sqrt
from bisect import bisect

__known_primes = [
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
    global __known_primes
    if not __known_primes:
        __known_primes = [2]

    if n <= len(__known_primes):
        return __known_primes[n - 1]

    n -= len(__known_primes)
    k = __known_primes[-1] + 2
    while n > 0:
        l = bisect(__known_primes, sqrt(k))
        for p in __known_primes[1:l]:
            if not k % p: break
        else:
            __known_primes.append(k)
            n -= 1
        k += 2

    return __known_primes[-1]

print nth_prime(10001)
print nth_prime(10001)
