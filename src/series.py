def fibs(n):
    a = b = 1
    for _ in range(n):
        yield a
        a, b = b, a + b

def sum_of_squares(n):
    return (n * (n + 1) * (2 * n + 1)) // 6

def square_of_sum(n):
    return (n ** 2 * (n + 1) ** 2) // 4

if __name__ == '__main__':
    pass
