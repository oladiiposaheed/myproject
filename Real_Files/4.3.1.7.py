from os import strerror
import sys
sys.stderr.write("Error message")
try:
    fo = open('newtext.txt', 'wt')
    for i in range(10):
        s = 'line #' + str(i + 1) + '\n'
        for ch in s:
            fo.write(ch)
    fo.close()
except IOError as e:
    print('I/O error occurred: ', strerror(e.errno))