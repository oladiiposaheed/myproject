class A:
    A = 2

print(hasattr(A, 'A'))

class R:
    def __init__(self):
        pa


class A:
    v = 2

class B(A):
    v = 1

class C(B):
    pass
o = C()
print(o.v)

class X:
    def a(self):
        print('a')

class Y:
    def a(self):
        print('b')

class Z(Y, X):
    def c(self):
        self.a()

o = Z()
o.c()