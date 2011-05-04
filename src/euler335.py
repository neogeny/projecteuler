def count_bean_moves(n):
    bowls = [1]*n
    count = 0
    i = 0
    while True:
        b = bowls[i]
        bowls[i] = 0
        for k in xrange(b):
            j =(i+1+k)%n
            bowls[j] += 1
        i = j
        count += 1
#        print bowls
        if all(bowls):
            return count

for i in xrange(20):
    n = 2**i+1
#    n = i+2
    print n,count_bean_moves(n)