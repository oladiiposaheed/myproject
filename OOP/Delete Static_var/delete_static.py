class Test:
    a = 10
    b = 20
    @classmethod
    def m1(cls):
        del cls.a
        cls.b = 20
        Test.c = 30
Test.m1()
print(Test.__dict__)