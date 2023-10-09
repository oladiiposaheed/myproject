def outer(p):
    def decor1(func):
        def inner1():
            #return func() + p
            return 'The Square of {} + {} = {}'.format(func(), p, func() + p)
        return inner1
    return decor1

@outer(12)
def ordinary():
    x = 10
    return x

print(ordinary())