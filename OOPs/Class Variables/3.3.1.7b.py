class ExampleClass:
    def __init__(self, val):
        if val % 2 != 0:
            self.a = 1
        else:
            self.b = 5
obj = ExampleClass(3)
print(obj.a)
try:
    print(obj.a)
except AttributeError:
    pass