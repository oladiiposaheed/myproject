def decor(func):
    def inner():
        res = func()
        return res ** 3
    return inner

def decor1(func):
    def inner1():
        res = 2 * func()
        return res
    return inner1

def decor2(func):
    def inner2():
        res = func() * 15
        return 'Final Result = {}'.format(res)
    return inner2

@decor2
@decor1
@decor
def cal():
    x = 10
    return x

print(cal())