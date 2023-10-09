from os import strerror

try:
    ccnt = lcnt = 0
    s = open('text.txt', 'rt')
    line = s.readline()
    while line != '':
        lcnt += 1
        for ch in line:
            print(ch, end='')
            ccnt += 1
        line = s.readline()
    s.close()
    print('\n\nCharacters in file: {}'.format(ccnt))
    print('Lines in file:     {}'.format(lcnt))

except IOError as e:
    print('I/O error occurred: {}'.format(e.errno))