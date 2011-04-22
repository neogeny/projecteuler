# Find the largest prime factor of the given number
target = 600851475143

def largest_prime_factor(n):
    def factor(n, i):
        while n > i:
            a, r = divmod(n, i)
            if r: break
            n = a
        return n

    n = factor(n, 2)
    for i in xrange(3, n, 2):
        n = factor(n, i)
        if n <= i: break
    return n

if __name__ == '__main__':
    print largest_prime_factor(target)
