from os import strerror

try:
    cnt = 0
    s = open('text.txt', 'rt')
    ch = s.read(1)
    #print(ch)
    while ch != '':
        print(ch, end='')
        cnt += 1
        ch = s.read(2)
    s.close()
    print('\n\nCharacters in file: {}'.format(cnt))

except IOError as e:
    print('I/O error occurred: ',strerror(e.errno))