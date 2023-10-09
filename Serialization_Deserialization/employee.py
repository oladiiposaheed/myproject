import json
class Employee:
    def __init__(self, eid, name, age, salary, address):
        self.eid = eid
        self.name = name
        self.age = age
        self.salary = salary
        self.address = address
    def display(self):
        print('Seat Number: {} Name: {} Age: {} Salary: {} Address: {}'.format(self.eid, self.name, self.age, self.salary, self.address))

e = Employee(100, 'Fatima', 15, 20000000, 'Nigeria')
e.display()
#emp_dict = {'eid': e.eid, 'name': e.name, 'age': e.age, 'salary':e.salary, 'address': e.address}
emp_dict = e.__dict__
print(type(emp_dict))
#print(emp_dict)

with open('emp.json', 'w') as f:
    json.dump(emp_dict, f, indent=4) #convert python dict to json

#Deserialization
with open('emp.json', 'r') as f:
    d = json.load(f)
newE = Employee(d['eid'], d['name'], d['age'], d['salary'], d['address'])
newE.display()