class Test:
    def m1(self, a=None, b=None, c=None):
        if a is not None and b is not None and c is not None:
            print('3-arg method')

        elif a is not None and b is not None:
            print('2-arg method')

        elif a is not None:
            print('3-arg method')

t = Test()
t.m1(20)
t.m1(12, 32)
t.m1(1, 2,4)