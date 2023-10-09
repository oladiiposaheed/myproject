class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __lt__(self, other):
        mark = self.marks < other.marks
        #names = self.name < other.name
        return mark

    def __ge__(self, other):
        return self.marks >= other.marks

s1 = Student('Ola', 100)
s2 = Student('Fatimah', 120)
s3 = Student('Tunde', 50)
print(s1 < s2)
print(s2 < s1)
print(s3 < s1)
print(s1 > s3)
print(s1 >= s2)
print(s1 <= s2)