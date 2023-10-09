class A:
    pass
class B:
    pass
class C:
    pass
class X(A, B):
    pass
class Y(B, C):
    pass
class P(X, Y, C):
    pass
print(A.mro())
print(X.mro())
print(Y.mro())
print(P.mro())
print(B.mro())