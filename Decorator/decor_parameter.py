def outer(name):
    def decor(func):
        def inner():
            return func().title() + name
        return inner
    return decor

@outer(' Fatimah')
def ordinary():
    return 'good morning'
print(ordinary())