class A:
    constrictor = 4
    def __init__(self):
        self.a = 5

obj = A()
print(hasattr(obj, 'a')) #T
print(hasattr(obj, 'constrictor')) #T
print(hasattr(A, 'a'))  #F
print(hasattr(A, 'constrictor'))  #T
