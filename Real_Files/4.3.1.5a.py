from os import strerror

try:
    ccnt = lcnt = 0
    s = open('text.txt', 'rt')
    lines = s.readlines(20)
    while len(lines) != 0:
        for line in lines:
            lcnt = lcnt + 1
            for ch in line:
                print(ch, end='')
                ccnt += 1
        lines = s.readlines(10)
    s.close()
    print('\n\nCharacters in file: {}'.format(ccnt))
    print('Lines in file: {}'.format(lcnt))

except IOError as e:
    print('I/O error occurred: {}'.format(e.errno))