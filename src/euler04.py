#A palindromic number reads the same both ways. The largest palindrome made
#from the product of two 2-digit numbers is 9009 = 91 x 99.
#
#Find the largest palindrome made from the product of two 3-digit numbers.

def is_palindrome(n):
    n = str(n)
    m, r = divmod(len(n), 2)
    if r: return False
    #print n, n[:m], n[len(n)+1:m-1:-1]
    return n[:m] == n[len(n)+1:m-1:-1]

def largest_palindromic(digits):
    top = int('9'*digits)
    bot = int('9'*(digits-1))
    best = 0
    for a in xrange(top, bot, -1):
        for b in xrange(top, bot, -1):
            n = a*b
            if n < best: 
                break
            if is_palindrome(n):
                best = n
    return best

print largest_palindromic(3)

