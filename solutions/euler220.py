#!/usr/bin/env python
# -*- encoding:utf-8 -*-

"""
Solution to Project Euler Problem
http://projecteuler.net/

by Apalala <apalala@gmail.com>
(cc) Attribution-ShareAlike 
http://creativecommons.org/licenses/by-sa/3.0/


"""
from math  import pi
from cmath import polar, phase
from factorization import factor

__prod = {intern('a'):intern('aRbFR'),
          intern('b'):intern('LFaLb'),
          intern('F'):intern('F'),
          intern('R'):intern('R'),
          intern('L'):intern('L')
          }

def heighway_dragon(n):
    assert n >= 0
    if n == 0:
        yield 'F'
        yield 'a'
    else:
        for x in heighway_dragon(n-1):
            if x == 'a':
                for c in 'aRbFR':
                    yield c
            elif x == 'b':
                for c in 'LFaLb':
                    yield c
            else:
                yield x

def draw_dragon(n, steps = None):
    p = 0  # position
    o = 1j # orientation
    k = 0
    for instr in heighway_dragon(n):
        if instr == 'F':
            p += o
            k += 1
#            if not k%10**6: print p,o,polar(p)
#            if phase(p) == pi/2: print k,k%8,p,o,polar(p)
            if steps is not None and k >= steps:
                break
        elif instr == 'R':
            o *= -1j
        elif instr == 'L':
            o *= 1j
        else:
            pass
    return int(p.real), int(p.imag)
            
def cool_draw_dragon(n, steps = None):
    import turtle

    turtle.reset()
    turtle.pencolor('red')
    turtle.hideturtle()
    turtle.delay(0)
    turtle.speed(0)
    turtle.left(90)
    FWD = 2
    k = 0
    for instr in heighway_dragon(n):
        if instr == 'F':
            turtle.forward(FWD)
            k += 1
            if steps is not None and k >= steps:
                break
        elif instr == 'R':
            turtle.right(90)
        elif instr == 'L':
            turtle.left(90)
        else:
            pass
    result = tuple(p // FWD for p in turtle.position())
    turtle.bye()
    return result

def fast_dragon(turns):
    g = [(0,0),(0,1),(1,1),(1,0)]
    p = 0  # position
    o = 1j
    i = 0
    for _ in xrange(turns):
        p += o
        turn_right = not g[i][0] and g[i][1]
        i = (i+1) % len(g)
        if turn_right:
            o *= -1j
        else:
            o *= 1j
    return int(p.real), int(p.imag)
            
def test():
    assert 'FaRbFRRLFaLbFR' == ''.join(heighway_dragon(2))
    assert (18,16) == draw_dragon(10, 500)
    assert draw_dragon(50, 500) == draw_dragon(10,500)

def run():
    print( draw_dragon(40, 10**7) )

if __name__ == '__main__':
    test()
    run()