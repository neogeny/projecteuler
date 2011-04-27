from num2word import n2w

def nonsplen(s):
    return len(s.replace(' ', '').replace('-', ''))

if __name__ == '__main__':
    s = 0
    for i in xrange(1000):
        number = i+1
        words = n2w.to_cardinal(number)
        print words
        s += nonsplen(words)
    print s
