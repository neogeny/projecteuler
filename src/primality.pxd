import cython

@cython.locals(
k = cython.long,
p = cython.long,
limit  = cython.long
)
cpdef long nth_prime(long n)

@cython.locals(
i = cython.long,
k = cython.long,
p = cython.long
)
cpdef long is_prime(long n)
