class Parent:
    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def display(self):
        print('Name: ',self.name)
        print('Age: ', self.age)
        print('Height: ', self.height)
        print('Weight: ', self.weight)

class Student(Parent):
    def __init__(self, name, age, height, weight, rollno, marks):
        super().__init__(name, age, height, weight)
        self.rollno = rollno
        self.marks = marks

    def display(self):
        super().display()
        print('Seat Number:', self.rollno)
        print('Marks:', self.marks)

s = Student('Fatima', 15, 101, 6.9, 120, 99)
s.display()