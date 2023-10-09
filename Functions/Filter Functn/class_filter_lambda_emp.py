class Employee:
    def __init__(self, name, sal, age, has_wife):
        self.name = name
        self.sal = sal
        self.age = age
        self.has_wife = has_wife

    def display(self):
        print(self.name)

e1 = Employee('Ola', 20000, 80, True)
e2 = Employee('Abdullah', 4000, 23, True)
e3 = Employee('Daniel', 20000, 60, False)
e4 = Employee('Ahmad', 50000, 74, True)
e5 = Employee('Mike', 40000, 50, True)
e6 = Employee('Kunle', 150000, 66, False)

lst = [e1, e2, e3, e4, e5, e6]
print('Employees Eligible for Pub Entry')
op = filter(lambda e: e.sal > 10000 and e.age > 22 and e.has_wife, lst)
for e in op:
    e.display()
    #print(e.name)

print('Employees Eligible for Bonus')
op = filter(lambda e: e.sal < 10000 or e.sal > 50000, lst)
for e in op:
    e.display()
    #print(e.name)

op = map(lambda e: Employee(e.name, e.sal + 10000, e.age, e.has_wife), lst)
for e in op:
    print(e.name, '......', e.sal,'$')