class Student:
    def __init__(self, name, age, rollno, mark):
        print('Constructor Execution Successfully')
        self.name = name
        self.age = age
        self.rollno = rollno
        self.mark = mark

    def info(self):
        name = 'Saheed'
        rollno = 120
        print(self.name)
        print(self.rollno)
        print('Student Name: {}'.format(self.name))
        print('Student Age: {}'.format(self.age))
        print('Student Seat Number: {}'.format(self.rollno))
        print('Student Mark: {}'.format(self.mark))

s = Student('Fatimah', 15, 100, 99)
s1 = Student('Mustapha', 12, 102, 87)
print('My name is',s.name)
print('Am {} years old'.format(s.age))
print('My Score in Mathematics is {}'.format(s.mark))
print('*********************************')
s.info()
print('++++++++++++++++++++++++++++++++')
s1.info()
print(id(s.info()))
print(id(s1.info()))