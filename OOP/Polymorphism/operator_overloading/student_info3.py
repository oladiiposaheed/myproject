class Student:
    def __int__(self, name, marks):
        self.name = name
        self.marks = marks

    def __str__(self):
        return str(self.marks)
        #return 'Student Name: {}  Student Mark: {}'.format(self.name, str(self.marks))
s1 = Student('Daud', 98)
print(s1)