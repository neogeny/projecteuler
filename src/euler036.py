# -*- encoding:utf-8 -*-i
"""
The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
"""

from palindromes import is_palindrome

def to_binary(n):
    return '{:b}'.format(n)

def dec_and_bin_palindromes(m):
    for n in xrange(1, m, 2):
        if is_palindrome(n) and is_palindrome(to_binary(n)):
            yield n

if __name__ == '__main__':
    s = 0
    for x in dec_and_bin_palindromes(10 ** 6):
        s += x
        print x, to_binary(x)
    print 'sum:', s
