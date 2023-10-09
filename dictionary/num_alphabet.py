i = 0
d = {}
while i < 26:
    d[chr(i + 65)] = 100 + 10*i
    i = i + 1
#k = d.keys()
for i in d.keys():
    print(i)
print(d)
for v in d.values():
    print(v)

while len(d) != 0:
    print('Processing item', d.popitem())
print(d)