class Student:
    collegeName = 'Taoheed College School'
    director = 'Oladiipo'
    def __init__(self, name, age, rollno):
        self.name = name
        self.age = age
        self.rollno = rollno

    def getStudentInfo(self):
        print('Student Name: {}'.format(self.name))
        print('Student Age: {}'.format(self.age))
        print('Student Seat Number: '.format(self.rollno))

    @classmethod
    def getCollegeInfo(cls):
        print('College Name: {}'.format(cls.collegeName))
        print('Director Name: {}'.format(cls.director))

    @staticmethod
    def getAverage(a, b, c):
        return (a + b + c)/3

name = input('Please Enter Student Name: ')
age = int(input('Please Enter Student Age: '))
rollno = int(input('Please Enter Student Seat Number: '))
s = Student(name, age, rollno)
s.getStudentInfo()
print('*'*20)
s.getCollegeInfo()
print('*'*20)
average = Student.getAverage(10, 20, 40)
print('Average: {}'.format(average))