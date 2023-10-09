s = input('Enter any string: ')
vowels = {'a', 'e', 'i', 'o', 'u'}
d = {}
for ch in s:
    if ch in vowels:
       # d[ch] = d[ch] + 1
        d[ch] = d.get(ch, 0) + 1
print(d)

for k, v in sorted(d.items()):
    print('{} occurs {} times'.format(k, v))