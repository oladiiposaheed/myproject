from os import strerror

try:
    ccnt = lcnt = 0
    for line in open('text.txt', 'rt'):
        lcnt += 1
        for ch in line:
            print(ch, end='')
            ccnt += 1
    print('\n\nCharacters in file: {}'.format(ccnt))
    print('Lines in file: {}'.format(lcnt))

except IOError as e:
    print('I/O error occurred: {}'.format(strerror(e,errno)))