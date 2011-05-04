# -*- encoding:utf-8 -*-
'''
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file 
containing over five-thousand first names, begin by sorting it into alphabetical
order. Then working out the alphabetical value for each name, 
multiply this value by its alphabetical position in the list to obtain 
a name score.

For example, when the list is sorted into alphabetical order, 
COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th 
name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
'''
import csv
names = sorted(csv.reader(open('../data/names.txt', 'r')).next())

def alphabetical_value(s):
    return sum(1 + ord(c) - ord('A') for c in s)

if __name__ == '__main__':
    print sum((i + 1) * alphabetical_value(s) for i, s in enumerate(names))

