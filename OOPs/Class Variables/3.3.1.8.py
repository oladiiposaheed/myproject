class A:
    a = 1
    def __init__(self):
        self.b = 2

obj = A()
print(hasattr(obj, 'b'))
print(hasattr(obj, 'a'))
print(hasattr(A, 'b'))
print(hasattr(A, 'a'))