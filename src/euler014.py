
def next_collaz(n):
    if n % 2:
        return 3 * n + 1
    else:
        return n // 2

__count = {1:1}
def _collaz_seq_len(n):
    s = set()
    c = 0
    i = n
    while i != 0:
        if i in __count:
            c += __count[i]
            break
        c += 1
        s.add(i)
        i = next_collaz(i)
        if i in s:
            break
    __count[n] = c
    return c

def collaz_seq_len(n):
    if n not in __count:
        __count[n] = 1 + collaz_seq_len(next_collaz(n))
    return __count[n]

@memoize
def collaz_seq_len2(n):
    if n == 1:
        return 1
    return 1 + collaz_seq_len(next_collaz(n))

if __name__ == '__main__':
    print collaz_seq_len(13)
    print collaz_seq_len(1)
    m = 0
    n = 0
    for i in range(1, 10 ** 6):
        c = collaz_seq_len(i)
        if c < m: continue
        #print i,c,'*'
        m = c
        n = i
print n
print m
