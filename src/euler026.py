from primality import primes_upto

TARGET=1000

def long_division_pattern(d):
    seen = {}
    r = 1
    k = 0
    while r:
        k += 1
        seen[r] = k
        digit, r = divmod(r*10, d)
        if r in seen:
           return k - seen[r] 
    return 0

def find_longest_recurring(m):
    firstval = lambda p: p[0]
    return max((long_division_pattern(i), i) for i in primes_upto(m))

if __name__ == '__main__':
    print find_longest_recurring(TARGET)[1]
