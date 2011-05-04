'''
Created on May 4, 2011

@author: apalala
'''

from itertools import permutations

TARGET = 10 ** 6

if __name__ == '__main__':
    perms = permutations('0123456789')
    for _ in xrange(TARGET - 1):
        perms.next()
    print ''.join(perms.next())
