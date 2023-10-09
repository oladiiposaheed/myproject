class ExampleClass:
    def __init__(self, val = 1):
        self.__first = val

    def set_second(self, val = 2):
        self.__second = val
obj1 = ExampleClass()
obj1.__fifth = 32
obj1.tenth = 'Python'
obj2 = ExampleClass(2)
obj2.set_second(3)
obj3 = ExampleClass(4)
obj3.__third = 5
print(obj1.__dict__)
print(obj2.__dict__)
print(obj3.__dict__)