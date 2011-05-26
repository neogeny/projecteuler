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
    for (;*count > 0; seq++)
    {
        if (*seq == 0) 
        {
            break;
        }
        else if (*seq == 'F') 
        {
            *pos += *dir;
            --*count;
            if (*count % powi(10,7) == 0) 
                printf("%lld %d %d %d\n", 
                    *count, n, (int)creal(*pos), (int)cimag(*pos));
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

void print_dragon_pos(long long count, int n)
{
    complex pos = 0;
    complex dir = I;
    draw_dragon(&pos, &dir, "Fa", &count, n);
    printf("%d %d\n", (int) creal(pos), (int) cimag(pos));
}

void main()
{
    print_dragon_pos(500, 10);
    print_dragon_pos(powi(10,8), 40);
}
