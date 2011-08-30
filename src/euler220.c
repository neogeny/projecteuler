#include <complex.h>
#include <math.h>
#include <stdio.h>

long long powi(long x, unsigned n)
{
    long long  p;
    long long  r;

    p = x;
    r = 1.0;
    while (n > 0)
    {
        if (n % 2 == 1)
            r *= p;
        p *= p;
        n /= 2;
    }

    return(r);
}

complex _pos; 
complex _dir; 
long long _count; 
long long _itersize;

void draw_dragon(char *seq, int n) 
{
    for (;_count > 0; seq++)
    {
        char c = *seq;
        if (c == 0) 
        {
            break;
        }
        else if (c == 'F') 
        {
            _pos += _dir;
            --_count;
            if (_count % _itersize  == 0) 
            {
                printf("%lld %d %d %d\n", 
                    count / _itersize, n, 
                    (int)creal(_pos), (int)cimag(_pos));
            }
        }
        else if (c == 'R')
        {
            _dir *= -I; 
        }
        else if (c == 'L')
        {
            _dir *= I; 
        }
        else if (n > 0)
        {
            if (c == 'a')
            {
                draw_dragon("aRbFR", n-1);
            }
            else if (c == 'b')
            {
                draw_dragon("LFaLb", n-1);
            }
        }
    } 
}

void print_dragon_pos(long long count, int n)
{
    _pos = 0;
    _dir = I;
    _count = count;
    _itersize = powi(10,8);
    draw_dragon("Fa",n);
    printf("%d %d\n", (int) creal(_pos), (int) cimag(_pos));
}

void main()
{
    print_dragon_pos(500, 10);
    print_dragon_pos(powi(10,12), 40);
}
