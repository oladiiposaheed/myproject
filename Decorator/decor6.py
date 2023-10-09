def decor(func):
    return func

@decor
def main_func():
    print('Original Function')

@decor
def f1():
    print('F1 Method')

f1()
main_func()