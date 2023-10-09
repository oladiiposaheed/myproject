class A:
    def __str__(self):
        return 'a'

class B:
    def __str__(self):
        return 'b'

class C(B):
    pass

o = C()
print(o)

class P:
    def __init__(self, v = 1):
        self.v = v

    def set(self, v):
        self.v = v
        return v
a = P()
print(a.set(a.v + 1))