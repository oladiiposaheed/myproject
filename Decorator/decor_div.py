def div_decor(func):
    def inner(*args):
        lst = []
        lst = args[1:]
        for i in lst:
            if i == 0:
                return 'Cannot be divided by Zero!!'
        return func(*args)
    return inner
@div_decor
def div(a, b):
    return a / b

@div_decor
def div2(a, b, c):
    return a/b/c

print(div(4, 0))
print('*'*23)
print(div(10,3))
print('*'*23)
print(div2(12,5, 7))