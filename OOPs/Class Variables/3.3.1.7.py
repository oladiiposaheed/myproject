class ExampleClass:
    def __init__(self, val):
        if val % 2 != 0:
            self.a = 1
        else:
            self.b = 5
obj = ExampleClass(2)
print(obj.b)

if hasattr(obj, 'b'):
    print(obj.b)