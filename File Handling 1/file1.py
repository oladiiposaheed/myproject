f = open('abc.txt', 'r')
print('File Name:', f.name)
print('File Mode:', f.mode)
print('Is file Readable: ', f.readable())
print('Is file Writable: ', f.writable())
print('Is file closed: ', f.closed)
f.close()
print('Is File Closed: ', f.closed)

print('**************************')
f = open('abc.txt', 'w')
print('File Name:', f.name)
print('File Mode:', f.mode)
print('Is file Readable: ', f.readable())
print('Is file Writable: ', f.writable())
print('Is file closed: ', f.closed)
f.close()
print('Is File Closed: ', f.closed)

print('**************************')
f = open('abcd.txt', 'w')
print('File Name:', f.name)
print('File Mode:', f.mode)
print('Is file Readable: ', f.readable())
print('Is file Writable: ', f.writable())
print('Is file closed: ', f.closed)
f.close()
print('Is File Closed: ', f.closed)

print('**************************')
f = open('abcde.txt', 'w+')
print('File Name:', f.name)
print('File Mode:', f.mode)
print('Is file Readable: ', f.readable())
print('Is file Writable: ', f.writable())
print('Is file closed: ', f.closed)
f.close()
print('Is File Closed: ', f.closed)

print('**************************')
f = open('abcdef.txt', 'a')
print('File Name:', f.name)
print('File Mode:', f.mode)
print('Is file Readable: ', f.readable())
print('Is file Writable: ', f.writable())
print('Is file closed: ', f.closed)
f.close()
print('Is File Closed: ', f.closed)

print('**************************')
f = open('abcdef.txt', 'a')
print('File Name:', f.name)
print('File Mode:', f.mode)
print('Is file Readable: ', f.readable())
print('Is file Writable: ', f.writable())
print('Is file closed: ', f.closed)
f.close()
print('Is File Closed: ', f.closed)

print('**************************')
f = open('abcdefg.txt', 'a+')
print('File Name:', f.name)
print('File Mode:', f.mode)
print('Is file Readable: ', f.readable())
print('Is file Writable: ', f.writable())
print('Is file closed: ', f.closed)
f.close()
print('Is File Closed: ', f.closed)

print('**************************')
f = open('abcdefh.txt', 'xb')
print('File Name:', f.name)
print('File Mode:', f.mode)
print('Is file Readable: ', f.readable())
print('Is file Writable: ', f.writable())
print('Is file closed: ', f.closed)
f.close()
print('Is File Closed: ', f.closed)
