"""
By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:
"""
STRIANGLE = """
75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
"""
"""
NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route. However, Problem 67, is the same challenge with a triangle containing one-hundred rows; it cannot be solved by brute force, and requires a clever method! ;o)
"""

from collections import namedtuple
from copy import deepcopy
from heapq import heappop as pop, heappush as push

Node = namedtuple('Node', 'cost i j')
Graph = namedtuple('Graph', 'nodes edges')

LINES = [s.split() for s in STRIANGLE.strip().split('\n')]
TRIANGLE = [[int(s) for s in line] for line in LINES]

def buildgraph():
    T = deepcopy(TRIANGLE)
    edges = {}
    for i in xrange(len(T)):
        for j,c in enumerate(T[i]):
            n = Node(c,i,j)
            edges[n] = []
            T[i][j] = n
    for i in xrange(len(T)-1):
        for j in xrange(len(T[i])):
            n = T[i][j]
            edges[n].append(T[i+1][j])
            edges[n].append(T[i+1][j+1])
    stop = Node(0,-1,-1)   
    edges[stop] = []
    for j in xrange(len(T[-1])-1):
        edges[T[-1][j]].append(stop)
    start = T[0][0]
    return (Graph(edges.keys(), edges), start, stop)

def findpath(graph, start, stop):
    f = max(n.cost for n in graph.nodes)
    heap = [(f-start.cost, start, [])]
    while heap:
        c,n,p = pop(heap)
        if n == stop:
            return (f+f*len(p)-c, list(reversed([(x.i,x.j) for x in p])))
        for m in graph.edges[n]:
            push(heap,(f-m.cost+c,m,[n]+p))

def bruteforce():
    T = deepcopy(TRIANGLE)
    for i in reversed(xrange(len(T)-1)):        
        for j,c in enumerate(T[i]):
            T[i][j] += max(T[i+1][j],T[i+1][j+1])
    return T[0][0]

if __name__ == '__main__':
    graph,start,stop = buildgraph()
    print findpath(graph, start, stop)
    print bruteforce()
