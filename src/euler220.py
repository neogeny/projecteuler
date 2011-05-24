#!/usr/bin/env python
# -*- encoding:utf-8 -*-

"""
Solution to Project Euler Problem
http://projecteuler.net/

by Apalala <apalala@gmail.com>
(cc) Attribution-ShareAlike 
http://creativecommons.org/licenses/by-sa/3.0/


"""

def heighway_dragon(n):
    def prod(c):
        if c == 'a':
            return 'aRbFR'
        elif c == 'b':
            return 'LFaLb'
        else:
            return c
    assert n >= 0
    if n == 0:
        yield 'F'
        yield 'a'
    else:
        for x in heighway_dragon(n-1):
            for c in prod(x):
                yield c

def draw_dragon(n, steps = None):
    RIGHT = {(0,1):(1,0),(1,0):(0,-1),(0,-1):(-1,0),(-1,0):(0,1)}
    LEFT = {(0,1):(-1,0),(-1,0):(0,-1),(0,-1):(1,0),(1,0):(0,1)}

    x, y = 0,0
    ox, oy = 0,1 # orientation
    k = 0
    for instr in heighway_dragon(n):
        if instr == 'F':
            x,y = x+ox, y+oy
            k += 1
            if steps is not None and k >= steps:
                break
        elif instr == 'R':
            ox,oy = RIGHT[(ox,oy)]
        elif instr == 'L':
            ox,oy = LEFT[(ox,oy)]
        else:
            pass
    return x, y
            

def test():
    assert 'FaRbFRRLFaLbFR' == ''.join(heighway_dragon(2))
    assert (18,16) == draw_dragon(10, 500)

def run():
    print( draw_dragon(50, 10**12) )

if __name__ == '__main__':
    test()
    run()
