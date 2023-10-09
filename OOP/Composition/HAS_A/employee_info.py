class Car:
    def __init__(self, name, model, color):
        self.name = name
        self.model = model
        self.color = color

    def carInfo(self):
        print('Car: {}, Model: {}, Color: {}'.format(self.name, self.model, self.color))

class Employee:
    def __init__(self, name, id, car):
        self.name = name
        self.id = id
        self.car = car

    def employeeInfo(self):
        print('Employee Information')
        print('Employee Name: {}'.format(self.name))
        print('Employee ID: {}'.format(self.id))
        #print('Car Information')
        self.car.carInfo()

car = Car('Venza', '10.4v', 'Yellow')
e = Employee('Fatimah', '0012', car)
e.employeeInfo()