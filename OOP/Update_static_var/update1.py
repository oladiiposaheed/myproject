class Test:
    a = 10
    @classmethod
    def m1(cls):
        cls.a = 20

    @staticmethod
    def m2():
        Test.a = 30

Test.m1()
Test.m2()
print(Test.a)