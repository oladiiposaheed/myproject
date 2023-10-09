class Person:
    name = 'Fatimah'
    age = 15
    country = 'Nigeria'
obj = getattr(Person, 'python', 'Wrong Information')
print(obj)