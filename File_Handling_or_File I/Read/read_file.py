f = open('file.txt')
reads = f.readlines()
print(reads)
for read in reads:
    read = read.lstrip()
    print(read.title(), end='')