f = None
try:
    f = open('xyz.txt')
    print(f.read())
except FileNotFoundError:
    print('Specified File Not Found!!!')
finally:
    if f is not None:
        f.close() #means f is pointing to a file, then close the file
        print('Is Filed Closed: ', f.closed)