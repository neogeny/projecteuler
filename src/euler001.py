# The sum of the numbers less than 1000 that are divisible by 3 or 5.

def sum_of_3_or_5_div():
    sum = 0
    for i in range(1000):
        if not (i % 3 and i % 5):
            sum += i
    return sum

if __name__ == '__main__':
    print sum_of_3_or_5_div()
