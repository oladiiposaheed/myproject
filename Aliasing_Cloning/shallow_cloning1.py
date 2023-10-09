import copy
a = [12, 20, 30, [33, 2], 67]
b = copy.copy(a)
a[3][1] = 111
print('A:',a)
print('B:',b)