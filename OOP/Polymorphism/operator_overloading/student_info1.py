class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __lt__(self, other):
        if self.marks == other.marks:
            result = self.name < other.name
            return result
        else:
            result = self.marks < other.marks
            return result

s1 = Student('Saheed', 98)
s2 = Student('Fatima', 100)
s3 = Student('Abdullah', 198)
print(s1 < s2)
print(s1 < s3)
print(s2 > s3)