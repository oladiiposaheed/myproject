def decor_div(func):
    def inner(a, b):
        return func(a, b) * 5
    return inner

def decor_mult(func):
    def inner2(a, b):
        result = func(a, b) + func(a, b)
        return 'The Final Result {} + {}  = {}'.format(func(a, b), func(a, b), result)
    return inner2

@decor_mult
@decor_div
def div1(a, b):
    return a/b

print(div1(20, 2))