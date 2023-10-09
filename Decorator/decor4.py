def decor(func):
    def inner():
        print('Wrapper Executed This before {}'.format(func.__name__))
        return func()
    return inner

@decor
def display():
    print('Dispaly Function Ran!!!!!')

display()