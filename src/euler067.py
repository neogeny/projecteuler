# -*- coding: utf-8 -*-
'''
By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom in triangle.txt (right click and 'Save Link/Target As...'), a 15K text file containing a triangle with one-hundred rows.

NOTE: This is a much more difficult version of Problem 18. It is not possible to try every route to solve this problem, as there are 299 altogether! If you could check one trillion (1012) routes every second it would take over twenty billion years to check them all. There is an efficient algorithm to solve it. ;o)
'''
from euler018 import bruteforce

STRIANGLE = open('../data/triangle.txt', 'r').read()
LINES = [s.split() for s in STRIANGLE.strip().split('\n')]
TRIANGLE = [[int(s) for s in line] for line in LINES]


if __name__ == '__main__':
#    graph, start, stop = build_graph_from_triangle(TRIANGLE)
#    print find_max_path(graph, start, stop)
    print bruteforce(TRIANGLE)
