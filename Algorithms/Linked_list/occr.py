sentence = input('Enter a simple sentence: ')
words = sentence.split()
count = dict()
for word in words:
    if word in count:
        count[word] += 1
    else:
        count[word] = 1
print(count)
print('********************')
for key, value in count.items():
    print('{} occurs {} times'.format(key.title(), value))