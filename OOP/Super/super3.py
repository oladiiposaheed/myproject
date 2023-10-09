class A:
    def m1(self):
        print('A class Method')

class B(A):
    def m1(self):
        print('B class Method')

class C(B):
    def m1(self):
        print('C class Method')

class D(C):
    def m1(self):
        print('D class Method')

class E(D):
    def m1(self):
        #super().m1()
        B.m1(self)
        #C.m1(self)
        super(B, self).m1()

e = E()
e.m1()
E().m1()