f = open('email.txt')
line = f.readline()
while line != '':
    print(line, end='')
    line = f.readline()
f.close()