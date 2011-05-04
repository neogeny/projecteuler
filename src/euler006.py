#The sum of the squares of the first ten natural numbers is,
#12 + 22 + ... + 102 = 385
#
#The square of the sum of the first ten natural numbers is,
#(1 + 2 + ... + 10)2 = 552 = 3025
#
#Hence the difference between the sum of the squares of the first ten 
#natural numbers and the square of the sum is 3025 - 385 = 2640.
#
#Find the difference between the sum of the squares of the first one
#hundred natural numbers and the square of the sum.

from series import sum_of_squares, square_of_sum

TARGET = 100

if __name__ == '__main__':
    print square_of_sum(TARGET) - sum_of_squares(TARGET)
