# -*- encoding:utf-8 -*-i
"""
Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
"""
from math import sqrt

def spiral_diagonal_sum(m):
    diag_no = 1
    diag_sum = 1
    for r in range(1, 1+m // 2):
        diff = 2*r
        for i in range(4):
            diag_no += diff
            diag_sum+=diag_no
#            print diag_sum,diag_no,diff,r
    return diag_sum

if __name__ == '__main__':
    print spiral_diagonal_sum(5)
    print spiral_diagonal_sum(7)
    print spiral_diagonal_sum(1001)
