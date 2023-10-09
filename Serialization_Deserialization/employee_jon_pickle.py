import jsonpickle

class Employee:
    def __init__(self, eid, name, age, salary, address, isMarried):
        self.eid = eid
        self.name = name
        self.age = age
        self.salary = salary
        self.address = address
        self.isMarried = isMarried
    def display(self):
        print('Seat Number: {} Name: {} Age: {} Salary: {} Address: {}'.format(self.eid, self.name, self.age, self.salary, self.address, self.isMarried))

e = Employee(100, 'Fatima', 15, 20000000, 'Nigeria', True)
json_str = jsonpickle.encode(e)
print(json_str)

with open('json_emp', 'w') as f:
    f.write(json_str)

#Deserialization
new_f = jsonpickle.decode(json_str)
#print(new_f)
new_f.display()

#Deserialization from the file
with open('json_emp', 'r') as f:
    json_string = f.readline()
new_f = jsonpickle.decode(json_string)
new_f.display()