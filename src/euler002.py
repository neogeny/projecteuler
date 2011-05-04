# The sum of the fibonacci numbers less than 4000000
from fibonacci import fibs

def even_fibs_sum():
    result = 0
    for i in fibs(1000):
        if i > 4000000:
            break
        if not i % 2:
            result += i
            #print i, result
    return result

if __name__ == '__main__':
    print even_fibs_sum()
