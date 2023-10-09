class Student:
    def __init__(self):
        print('Constructor Execution Successfully')
        self.name = 'Saheed'
        self.age = 14
        self.rollno = 100
        self.mark = 99

    def info(self):
        print('Student Name: {}'.format(self.name))
        print('Student Age: {}'.format(self.age))
        print('Student Seat Number: {}'.format(self.rollno))
        print('Student Mark: {}'.format(self.mark))

s = Student()
s1 = Student()
print('My name is',s.name)
print('Am {} years old'.format(s.age))
print('My Score in Mathematics is {}'.format(s.mark))
print('*********************************')
s.info()
print('++++++++++++++++++++++++++++++++')
s1.info()
print(id(s.info()))
print(id(s1.info()))