class Car:
    def __init__(self, name, model, color):
        self.name = name
        self.model = model
        self.color = color

    def getinfo(self):
        print('Car Information')
        print('Name: {}\n Model: {}\n Color: {}'.format(self.name, self.model, self.color))

class Person:
    def __init__(self, name, age, nationality):
        self.name = name
        self.age = age
        self.nationality = nationality

    def eatndrink(self):
        print('Eating and Drinking')

class Employee(Person):
    def __init__(self, name, age, nationality, eno, esal, car):
        super().__init__(name, age, nationality) # calling parent class constructor
        self.eno = eno
        self.esal = esal
        self.car = car

    def work(self):
        print('Python Coding based')

    def empinfo(self):
        print('Employee Name: {}'.format(self.name))
        print('Employee Age: {}'.format(self.age))
        print('Employee Number: {}'.format(self.eno))
        print('Employee Salary: {}'.format(self.esal))
        print('Employee Nationality: {}'.format(self.nationality))
        print('Employee Car Information')
        self.car.getinfo()

car = Car('Toyota', '34.6v', '#fa32c5')
e = Employee('Mustapha', 95, 'Nigeria', '00001', 340000000, car)
e.eatndrink()
e.work()
print('*'*20)
e.empinfo()