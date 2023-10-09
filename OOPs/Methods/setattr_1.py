class Person:
    name = 'Fatimah'
    age = 15
    country = 'Nigeria'
obj1 = getattr(Person, 'age')
print('She was {} years old'.format(obj1))
print()
new_age = int(input('How old are you now?: '))
latest_age = Person.age + new_age
setattr(Person, 'age', latest_age)
obj = getattr(Person, 'age')
print('She is now {} years old'.format(latest_age))