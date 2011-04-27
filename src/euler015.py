__seen = {}
def count_routes(n,m):
    if n == 0 or m == 0:
        return 1

    if (n,m) in __seen:
        return __seen[(n,m)]

    if n == m:
        result  =2*count_routes(n,m-1)
    else:
        result = (
          count_routes(n-1,m)  
        + count_routes(n,m-1)  
        )
    __seen[(n,m)] = result
    __seen[(m,n)] = result
    return result
    
try:
    for n in xrange(21):
        print n, count_routes(n,n)
except KeyboardInterrupt:
    pass
