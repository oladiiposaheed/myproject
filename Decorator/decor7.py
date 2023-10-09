def decor(func):
    def inner(name):
        return func(name).title()
    return inner

@decor
def f1(name):
    return 'Hi {}'.format(name)
name = input('Enter Your Name: ')
print(f1(name))