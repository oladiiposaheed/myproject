class Test:
    def m1(x):
        print('m1 of Test')

class Demo:
    def m1(x):
        print('m1 of Demo')

class Sample:
    def m1(x, y):
        x.m1()
        y.m1()
t = Test()
d = Demo()
Sample.m1(t, d)
print('******************************')
Sample.m1(d, t)