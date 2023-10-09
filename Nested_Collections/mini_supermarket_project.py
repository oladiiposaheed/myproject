supermarket = {
    'store1': {
        'name': 'Food Store Department',
        'items': [
            {'name': 'Rice', 'quantity': 40},
            {'name': 'Semovita', 'quantity': 72},
            {'name': 'Custard', 'quantity': 145}
        ]
    },

    'store2': {
            'name': 'Provision Store Department',
            'items': [
                {'name': 'Peak milk', 'quantity': 270},
                {'name': 'Milo', 'quantity': 100},
                {'name': 'Dano', 'quantity': 124}
            ]
        },

    'store3': {
            'name': 'Book Store Department',
            'items': [
                {'name': 'Java', 'quantity': 15},
                {'name': 'Django', 'quantity': 134},
                {'name': 'Python', 'quantity': 202},
                {'name': 'Django', 'quantity': 160}
            ]
        }
}
#print(supermarket)
print(supermarket['store1'])
print(supermarket['store1']['name'])
print(supermarket.get('store1')['items'])
print(supermarket.get('store1')['items'][0])
print(supermarket['store1']['items'][2])
print(supermarket.get('store1')['items'][2]['quantity'])
print(supermarket['store1']['items'][2]['name'])

# To print the names of all items present in the store1
print('__________________________')
for name in supermarket['store1']['items']:
    print(name['name'])

print('************************')
for quant in supermarket.get('store1').get('items'):
    print(quant['quantity'])

print('#############################')
#How many python books are available
for item in supermarket['store3']['items']:
    if item['name'] == 'Python':
        print('The Total Number of Python Books:', item['quantity'])
    elif item['name'] == 'Django':
        print('The Total Number of Django Books:', item['quantity'])
    elif item['name'] == 'Java':
        print('The Total Number of Java Books:', item['quantity'])
    else:
        print('Book Not Found!')
