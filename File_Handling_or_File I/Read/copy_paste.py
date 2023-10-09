inp = open('input2.txt')
outp = open('output2.txt', 'w')
f = inp.readline()
while f != '':
    if f:
        f = f.lstrip()
        print(f.title(), end='')
    f = inp.readline()
    #outp = open('output2.txt', 'w')
    #data = f.read()
    outp.write(f)
    #print(f, end='')
    #outp = open('output2.txt', 'w')
    #outp.write(data)
inp.close()
outp.close()

