from os import strerror

counters = {chr(ch): 0 for ch in range(ord('a'), ord('z') + 1)}
file_name = input('Enter the name of the file to analyze: ')
try:
    f = open(file_name, 'rt')

