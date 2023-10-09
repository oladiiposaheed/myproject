f = open('file.txt')
line = f.readline()
while line != '':
    if line:
        line = line.lstrip()
        print(line.title(), end='')
    line = f.readline()
f.close()