dictionary = { 'a': 'b', 'b': 'c', 'c': 'd' }

key = 'a'
try:
    while True:
        key = dictionary[key]
        print(key)
except KeyError:
    print('No such key:', key)

x = '\''
print(len(x))
print((ord('c') - ord('a')))
print('Mike' > 'Mikyee')
#print(float('2, 5'))