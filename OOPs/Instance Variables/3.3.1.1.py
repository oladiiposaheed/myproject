class ExampleClass:
    def __init__(self, val = 1):
        self.first = val

    def set_second(self, val):
        self.second = val

obj1 = ExampleClass()
#obj1 = ExampleClass(10)
obj2 = ExampleClass(2)
obj2.set_second(3)
obj2.set_second((12, 9))
obj3 = ExampleClass(4)
obj3.third = 5
obj3.fourth = 'Python'
obj1.fifth = 'django'
#obj1.set_second('Data Science')
obj1.set_second(23)

print(obj1.__dict__)
print(obj2.__dict__)
print(obj3.__dict__)