#!/usr/bin/env python
# -*- encoding:utf-8 -*-

"""
Solution to Project Euler Problem
http://projecteuler.net/

by Apalala <apalala@gmail.com>
(cc) Attribution-ShareAlike 
http://creativecommons.org/licenses/by-sa/3.0/

If the numbers 1 to 5 are written out in words: one, two, three, four, five, 
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in
 words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and 
forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 
letters. The use of "and" when writing out numbers is in compliance with British 
usage.
"""

from num2word import n2w #@UnresolvedImport

def nonsplen(s):
    return len(s.replace(' ', '').replace('-', ''))

def sum_spellings(n):
    s = 0
    for i in xrange(n):
        number = i + 1
        words = n2w.to_cardinal(number) #@UndefinedVariable
        s += nonsplen(words)
    return s

def test():
    assert 19 == sum_spellings(5)

if __name__ == '__main__':
    test()
    print sum_spellings(1000)
