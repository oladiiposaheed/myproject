class Person:
    name = 'Fatimah'
    age = 15
    country = 'Nigeria'
obj = getattr(Person, 'age')
print('She is {} years old.'.format(obj))