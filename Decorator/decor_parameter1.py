def decor(func):
    def inner():
        r = func()
        return r*2
    return inner

@decor
def ordinary():
    x = 10
    return 'The value of x = {}'.format(x)
print(ordinary())