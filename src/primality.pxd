import cython

@cython.locals(
k = cython.int,
p = cython.int,
limit  = cython.int
)
cpdef int nth_prime(int n)

@cython.locals(
i = cython.int,
k = cython.int,
p = cython.int
)
cpdef int is_prime(int n)


@cython.locals(
n = cython.int
)
cpdef object all_primes():
    for n in count(1):
        yield nth_prime(n)

@cython.locals(
p = cython.int
)
cpdef object primes_upto(int m):
    for p in all_primes():
        if p <= m:
            yield p
        else:
            break


if __name__ == '__main__':
    for p in primes_upto(1000000):
        assert is_prime(p)
