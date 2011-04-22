'''
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''

# Solve for b the system of eauations
# a2 + b2 = c2
# a + b + c = 1000

import math

def pythagorean_triplet_that_sums(s):
    def solve_b(a):
        return int(1000 * (500 - a) / (1000 - a))

    for a in xrange(1, s):
        b = solve_b(a)
        if b < a:
            break

        c = math.sqrt(a ** 2 + b ** 2)
        if c != int(c):
            continue
        c = int(c)

#        print a, b, c, a + b + c
        if a + b + c == s:
            return a * b * c

if __name__ == '__main__':
    print pythagorean_triplet_that_sums(1000)
