'''
The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.
'''

def last_n_digits(k, n):
    return n % (10 ** k)

def n_digits_from_power(k, n):
    p = 1
    for _ in range(n):
        p = last_n_digits(k, p * n)
    return p

def n_digits_from_sum_of_powers(k, p):
    s = 0
    for i in xrange(1, p + 1):
        s = s + n_digits_from_power(k, i)
    return last_n_digits(k, s)

if __name__ == '__main__':
    print n_digits_from_sum_of_powers(15, 10)
    print n_digits_from_sum_of_powers(10, 1000)
    print sum(x ** x for x in range(1, 1000 + 1)) % (10 ** 10)
