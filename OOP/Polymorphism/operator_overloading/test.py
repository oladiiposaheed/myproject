class Test:
    def m1(self, x):
        print('{}-argument method'.format(x.__class__.__name__))

t = Test()
t.m1(10)
t.m1(12.56)
t.m1('Python')