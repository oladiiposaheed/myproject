f = open('email.txt')
line = f.readline()
while line != '':
    if line != '\n':
        print(line, end='')
    line = f.readline()
f.close()