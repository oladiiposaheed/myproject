class Test:
    a = 10
    b = 20
    c = 30
    def __init__(self):
        print(self.a)
        print(Test.a)

    def m1(self):
        print(self.a)
        print(Test.a)

    @classmethod
    def m2(cls):
        print(cls.b)
        print(Test.c)

    @staticmethod
    def m3():
        print(Test.c)

t = Test()
t.m1()
t.m2()
t.m3()
Test.m2()
#print(t.a)