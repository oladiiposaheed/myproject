def decor(func):
    def inner():
        r = func()
        return 'The value of x = {}'.format(r * 3)
    return inner

@decor
def ordinary():
    x = 10
    return x
print(ordinary())