class Test:
    x = 10
    def __init__(self):
        self.y = 20

    def m1(self):
        self.x = 888
        self.y = 999

    @classmethod
    def m2(cls):
        cls.x = 111
        cls.y = 222

t1 = Test()
t2 = Test()
t3 = Test()
t1.m1()
t3.m2()
print('t1: ', t1.x, t1.y)
print('t2: ', t2.x, t2.y)
print('t3:', t3.x, t3.y)
print('T3:', Test.x, Test.y)