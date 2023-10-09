class Student:
    def __init__(self, fname, lname, marks):
        self.fname = fname
        self.lname = lname
        self.marks = marks

    def display(self):
        print('{} Information'.format(self.fname))
        print('Full Name: {} {}'.format(self.fname, self.lname))
        print('Score: {}'.format(self.marks))
        self.grade()

    def grade(self):
        if self.marks >= 70:
            print('You got First Class')
        elif self.marks >= 60:
            print('You got Second Class Upper')
        elif self.marks >= 50:
            print('You got Second Class Lower')
        elif self.marks >= 40:
            print('You got Third Class')
        else:
            print('You are Failed')

n = int(input('Enter Number of Student: '))
for i in range(n):
    fname = input('Enter First Name: ')
    lname = input('Enter Last Name: ')
    marks = int(input('Enter Student Marks: '))
    s = Student(fname, lname, marks)
s.display()
print('*'*20)

#s.grade()