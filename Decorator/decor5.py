def decor(func):
    def inner(*args, **kwargs):
        print('Wrapper Executed This before {}'.format(func.__name__))
        return func(*args, **kwargs)
    return inner

@decor
def display():
    print('Display Function Ran!!!')

@decor
def display_info(name, age, rollno):
    print('Display Information Ran With Arguments [{}, {}, {}]'.format(name, age, rollno))

display_info('Fatima', 15, 100)
display()