class P:
    def m1(self):
        print('Parent Method')

class C(P):
    def m2(self):
        print('Child Method')
        self.m1()

c = C()
c.m2()
c.m1()
print('****************')
c.m2()