'''
'''

def sdigits(n):
    return (c for c in str(n))

def digits(n):
    return (int(c) for c in str(n))

def last_k_digits(k, n):
    return n % (10 ** k)