class Student:
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks
s1 = Student('Ola', 99, 98)

class Test:
    def m1(self):
        print('Method execution')
t = Test()
t.m1()