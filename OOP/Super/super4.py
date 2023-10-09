class P:
    a = 10
    def __init__(self):
        self.b = 20

class C(P):
    a = 9999
    def __init__(self):
        #super().__init__()
        self.b = 30
        #super(C, self).__init__()
        super().__init__()

    def m1(self):
        #print(self.a)
        print(self.b)
        print(self.a)
        print(super().a)
        #print(super().a)
        #print(super().b)
        #print(P.m1())

c = C()
c.m1()