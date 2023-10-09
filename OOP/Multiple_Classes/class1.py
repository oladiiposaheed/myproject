class Test:
    def m1(x):
        print('m1 of Test')

class Demo:
    def m1(x):
        print('m1 of Demo')

class Sample:
    def m1(x, y):
        print('The type of x: ', type(x))
        print('The type of y: ', type(y))
t = Test()
d = Demo()
Sample.m1(t, d)
print('******************************')
Sample.m1(d, t)