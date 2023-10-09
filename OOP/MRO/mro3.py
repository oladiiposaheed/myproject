class A:
    #def m1(self):
     #   print('A class method')
     pass

class B:
    #def m1(self):
     #   print('B class method')
     pass

class C:
    #def m1(self):
     #   print('C class method')
     pass

class X(A, B):
    pass

class Y(B, C):
    pass

class P(X, Y, C):
    pass

p = P()
#p.m1()
print(P.mro())