from math import exp
ex = 1

try:
    while True:
        print('Exponenet of {} = {}'.format(ex, exp(ex)))
        ex *= 2
except OverflowError:
    print('The number is too big.')