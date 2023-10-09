d = {
    'phones': ('Samsung', 'Nokia', 'Ericson', 'Techo'),
    'foods': ['Rice', 'Beans', 'Tuwo', 'Semovita']
}
print(d['phones'])
print(d['foods'])
print(d['phones'][2])
print(d['foods'][0].lower())
print(d.get('phones'))
print(d.get('foods'))
print(d.get('phones')[3])

print('**********************')
print('Display All Phone and Food Names')
print('**********************')

for phone in d['phones']:
    print(phone)
print('______________________')
for food in d.get('foods'):
    print(food)