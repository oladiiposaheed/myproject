class Employee:
    def __init__(self, ename, esal, eno):
        self.ename = ename
        self.esal = esal
        self.eno = eno

    def display(self):
        print('Employee Number: {}'.format(self.eno))
        print('Employee Name: {}'.format(self.ename))
        print('Employee Salary: {}'.format(self.esal))

class Manager:
    def updateSalary(emp):
        emp.esal = emp.esal + 10000
        emp.display()
e = Employee('Ola', 40000, 100)
Manager.updateSalary(e)