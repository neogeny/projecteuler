# The sum of the numbers less than 1000 that are divisible by 3 or 5.
sum = 0
for i in range(1000):
    if not (i % 3 and  i % 5):
        print i
        sum += i
print sum
