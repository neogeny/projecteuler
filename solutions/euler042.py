#!/usr/bin/env python
# -*- encoding:utf-8 -*-

"""
Solution to Project Euler Problem 22
http://projecteuler.net/

by Apalala <apalala@gmail.com>
(cc) Attribution-ShareAlike
http://creativecommons.org/licenses/by-sa/3.0/

"""
import csv
from words import alphabetical_value
from series import is_triangle

FILENAME = 'data/words.txt'


def count_triangle_words(names):
    return sum(1 for w in names if is_triangle(alphabetical_value(w)))


def test():
    assert 55 == alphabetical_value('SKY')
    assert is_triangle(55)


def run():
    names = csv.reader(open(FILENAME, 'r')).next()
    print count_triangle_words(names)


if __name__ == '__main__':
    test()
    run()
