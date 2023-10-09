class P:
    a = 10
    def __init__(self):
        print('Parent constructor')

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
        print('Child Constructor')

    def method1(self):
        #print(super().a)
        #super().m1()
        #super().m2()
        #super().m3()
        #super().__init__()
        self.m1()
        self.m2()
        self.m3()
        self.__init__()

        #if parent and child classes contain a member with the same name, then to call parent class member explicitly from the child class, then go for super().

c = C()
c.method1()
print('**************')
c.m1()