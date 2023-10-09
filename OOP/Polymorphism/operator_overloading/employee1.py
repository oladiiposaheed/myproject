class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __mul__(self, other):
        total_salary = self.salary * other.days
        return total_salary

class TimeSheet:
    def __init__(self, name, days):
        self.name = name
        self.days = days

    def __mul__(self, other):
        total_salary = self.days * other.salary
        return total_salary

e = Employee('Saheed', 600)
t = TimeSheet('Saheed', 20)
print('Your This month Salary ${}'.format(e * t)) # self = e, other = t
print('Your This month Salary ${}'.format(t * e))

# self = t == self.days(20)
# other = e ==other.salary = 600
