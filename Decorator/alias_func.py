def f1(func):
    print('f1 function has {} function as arg'.format(func))
    func()

def fx():
    print('fx function')

def fy():
    print('fy function')

f1(fx)
f1(fy)