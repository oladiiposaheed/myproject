def print_function(args, poly, exp):
    for x in args:
        print('f(', x, ')=', poly(x), sep='')
    print('***************')

    for x in args:
        print('f(', x, ')=', exp(x), sep='')

def poly(x):
    return 2 * x ** 3 - 4 * x + 2

def exp(e):
    return e ** 2 + 5 * e - 100

print_function([x for x in range(-2, 3)], poly, exp)