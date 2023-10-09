from functools import *
def fact(x, y):
    return x * y

n = int(input('Enter a Positive Integer: '))
op = reduce(fact, range(1, n + 1))
print(op)