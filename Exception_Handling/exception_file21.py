f = 0
try:
    f = open('xyz.txt')
except ZeroDivisionError:
     print('File Not Found!!!')
else:
    print(f.read())
finally:
    if f != 0:
        f.close()