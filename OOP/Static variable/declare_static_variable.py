class Test:
    a = 10
    def __init__(self):
        Test.b = 20
    def m1(self):
        Test.c = 30

    @classmethod
    def m2(cls):
        cls.e = 40
        Test.f = 50

    @staticmethod
    def m3():
        Test.d = 60

t = Test()
t.m1()
Test.g = 80
print(Test.__dict__)
t.m2()
print(Test.__dict__)
t.m3()
print(Test.__dict__)