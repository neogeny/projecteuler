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

void draw_dragon(
            complex *pos, 
            complex *dir, 
            char *seq, 
            long long *count, 
            int n
) 
{
    for (;*count > 0 && *seq; seq++)
    {
        if (*seq == 'F') 
        {
            *pos += *dir;
            --*count;
            if (*count % powi(10,6) == 0) 
                printf("%lld %d %f %f\n", 
                    *count, n, creal(*pos), cimag(*pos));
        }
        else if (*seq == 'R')
        {
            *dir *= -I; 
        }
        else if (*seq == 'L')
        {
            *dir *= I; 
        }
        else if (n > 0)
        {
            if (*seq == 'a')
            {
                draw_dragon(pos, dir, "aRbFR", count, n-1);
            }
            else if (*seq == 'b')
            {
                draw_dragon(pos, dir, "LFaLb", count, n-1);
            }
        }
    } 
}

void main()
{
    complex pos = 0;
    complex dir = I;
    long long count = 500;
    draw_dragon(&pos, &dir, "Fa", &count, 10);
    printf("%d %d\n", (int) creal(pos), (int) cimag(pos));

    count = powi(10,8);
    draw_dragon(&pos, &dir, "Fa", &count, 50);
    printf("%d %d\n", (int) creal(pos), (int) cimag(pos));
}
