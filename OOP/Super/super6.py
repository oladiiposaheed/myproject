class P:
    def __init__(self):
        print('Parent Constructor')

    def m1(self):
        print('Parent Instance Method')

    @classmethod
    def m2(cls):
        print('Parent Class Method')

    @staticmethod
    def m3():
        print('Parent Static Method')

class C(P):
    def __init__(self):
        super().__init__()
        super().m1()
        super().m2()
        super().m3()

    @classmethod
    def method2(cls):
        super(C, cls).__init__(cls)
        super(C, cls).m1(cls)

    @staticmethod
    def method3():
        super(C, C).m3()

c = C()
print('###################')
C.method2()