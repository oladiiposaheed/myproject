class P:
    def m1(self):
        print('Parent Method')

class C(P):
    def m1(self):
        print('Child Method')
        super().m1()

c = C()
c.m1()
print('****************')