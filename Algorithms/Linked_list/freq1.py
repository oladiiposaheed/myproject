a = [1, 5, 2, 7, 2, 5, 1, 6]
count = {}
for i in a:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1
#print(count)
print('***************')
for k, v in count.items():
    if v == 1:
        print('{} occur(s) {}'.format(k, v))