a = [12, 20, 30, [33, 2], 67]
b = a.copy()
print('A:',a)
print('B:',b)
print('')
a[0] = 0
a[3][1] = -10
b[3][0] = 'Fine'
print('A:',a)
print('B:',b)
print()
print(id(a[0]), id(b[0]))
print(id(a[3]), id(b[3]))
print(id(a[3][0]), id(b[3][0]))
print()
b[3] = 'python'
print('A:',a)
print('B:',b)