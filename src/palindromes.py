def is_palindrome(n):
    n = str(n)
    m, r = divmod(len(n), 2)
    return n[:m] == n[len(n) + 1:m + r - 1:-1]
