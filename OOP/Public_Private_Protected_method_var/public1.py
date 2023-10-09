class Test:
    def __int__(self):
        self.x = 12

    def m1(self):
        print('Public m1 method')

    def m2(self):
        print(self.x)
        self.m1()

t = Test()
t.m1()
t.m2()
