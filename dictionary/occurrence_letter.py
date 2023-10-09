s = input('Enter any string: ')
d = {}
for ch in s.upper():
    if ch in d:
       # d[ch] = d[ch] + 1
        d[ch] = d.get(ch, 0) + 1
    else:
        d[ch] = 1
print(d)

for k, v in sorted(d.items()):
    print('{} occurs {} times'.format(k, v))